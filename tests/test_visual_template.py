#!/usr/bin/env python3
"""Rendered interaction regression for the KOKUEN v5 universal UI template."""

from __future__ import annotations

import os
from pathlib import Path

from playwright.sync_api import Page, expect, sync_playwright

BASE_URL = os.environ.get(
    "KOKUEN_BASE_URL",
    "http://127.0.0.1:4312/designs/kokuen-visual-template/Universal%20UI%20Template.html",
)
ARTIFACT_DIR = Path(os.environ.get("KOKUEN_ARTIFACT_DIR", "/tmp/kokuen-v5-artifacts"))


def assert_no_small_targets(page: Page) -> None:
    failures = page.locator(
        "button, a, input, textarea, [role=slider], [tabindex='0']"
    ).evaluate_all(
        """
        (elements) => elements
          .filter((element) => element.getClientRects().length && getComputedStyle(element).visibility !== 'hidden')
          .filter((element) => !(element.classList.contains('spec-skip') && document.activeElement !== element))
          .map((element) => {
            const box = element.getBoundingClientRect();
            return {
              label: element.getAttribute('aria-label') || element.textContent.trim().slice(0, 60) || element.id,
              tag: element.tagName,
              id: element.id,
              width: box.width,
              height: box.height
            };
          })
          .filter((item) => item.width < 43.5 || item.height < 43.5)
        """
    )
    assert not failures, f"interactive targets below 44px: {failures}"


def assert_focus(page: Page, selector: str) -> None:
    try:
        expect(page.locator(selector)).to_be_focused(timeout=1500)
    except AssertionError as error:
        active = page.evaluate("document.activeElement.outerHTML.slice(0, 180)")
        raise AssertionError(f"expected focus on {selector}, got {active}") from error


def run_interactions(page: Page) -> None:
    expect(page.locator("html")).to_have_attribute("data-theme", "dark")
    assert page.evaluate("getComputedStyle(document.documentElement).getPropertyValue('--k-target').trim()") == "44px"
    assert page.evaluate("getComputedStyle(document.body).backgroundColor") == "rgb(10, 10, 10)"
    assert_no_small_targets(page)

    page.get_by_role("button", name="Light proof").click()
    expect(page.locator("html")).to_have_attribute("data-theme", "light")
    assert page.evaluate("getComputedStyle(document.body).backgroundColor") == "rgb(247, 246, 242)"
    page.get_by_role("button", name="Dark default").click()

    busy = page.locator("#busy-action")
    busy.click()
    busy.dispatch_event("click")
    expect(page.locator("#action-status")).to_contain_text("Check 1 is running")
    expect(page.locator("#action-status")).to_contain_text("Check 1 completed", timeout=2500)

    page.locator("#field-clear").click()
    page.locator("#field-validate").click()
    assert_focus(page, "#project-name")
    expect(page.locator("#project-name")).to_have_attribute("aria-invalid", "true")
    expect(page.locator("#project-name")).to_have_attribute("aria-describedby", "project-error")
    expect(page.locator("#project-error")).to_be_visible()
    page.locator("#project-name").fill("Keyboard review")
    page.locator("#field-validate").click()
    expect(page.locator("#project-name")).to_have_attribute("aria-invalid", "false")

    checkbox = page.get_by_role("checkbox", name="Include archived work")
    checkbox.click()
    expect(checkbox).to_have_attribute("aria-checked", "true")
    switch = page.get_by_role("switch", name="Review mode")
    switch.focus()
    switch.press("Space")
    expect(switch).to_have_attribute("aria-checked", "true")

    radios = page.get_by_role("radio")
    radios.nth(0).focus()
    radios.nth(0).press("ArrowRight")
    expect(radios.nth(1)).to_have_attribute("aria-checked", "true")
    assert_focus(page, "#density-radios [role=radio]:nth-of-type(2)")
    radios.nth(1).press("ArrowLeft")
    expect(radios.nth(0)).to_have_attribute("aria-checked", "true")

    slider = page.locator("#volume-slider")
    slider.focus()
    slider.press("End")
    expect(slider).to_have_attribute("aria-valuenow", "100")
    slider.press("Home")
    expect(slider).to_have_attribute("aria-valuenow", "0")

    select = page.locator("#scope-trigger")
    select.focus()
    select.press("ArrowDown")
    expect(select).to_have_attribute("aria-expanded", "true")
    expect(select).to_have_attribute("aria-activedescendant", "scope-all")
    select.press("ArrowDown")
    expect(select).to_have_attribute("aria-activedescendant", "scope-notes")
    select.press("Escape")
    expect(select).to_have_attribute("aria-expanded", "false")
    expect(page.locator("#scope-value")).to_have_text("Everything")
    select.press("End")
    select.press("Enter")
    expect(page.locator("#scope-value")).to_have_text("任务和截止日期")
    assert_focus(page, "#scope-trigger")

    first_tab = page.locator("#tab-recent")
    first_tab.focus()
    first_tab.press("ArrowRight")
    expect(page.locator("#tab-pinned")).to_have_attribute("aria-selected", "true")
    expect(page.locator("#panel-pinned")).to_be_visible()

    menu_trigger = page.locator("#menu-trigger")
    menu_trigger.focus()
    menu_trigger.press("ArrowDown")
    assert_focus(page, "#action-menu [role=menuitem]:first-of-type")
    page.keyboard.press("End")
    assert_focus(page, "#action-menu [role=menuitem]:last-of-type")
    page.keyboard.press("Escape")
    assert_focus(page, "#menu-trigger")
    expect(menu_trigger).to_have_attribute("aria-expanded", "false")

    page.get_by_role("button", name="Error", exact=True).click()
    expect(page.locator("#state-preview")).to_contain_text("Could not load projects")

    page.get_by_role("button", name="Page 2", exact=True).click()
    toast = page.locator(".k-toast")
    expect(toast).to_have_text("Page 2 selected.")
    toast_edges = toast.evaluate(
        """
        (element) => {
          const style = getComputedStyle(element);
          return {
            widths: [style.borderTopWidth, style.borderRightWidth, style.borderBottomWidth, style.borderLeftWidth],
            colors: [style.borderTopColor, style.borderRightColor, style.borderBottomColor, style.borderLeftColor]
          };
        }
        """
    )
    assert len(set(toast_edges["widths"])) == 1, f"toast edge widths differ: {toast_edges}"
    assert len(set(toast_edges["colors"])) == 1, f"toast edge colors differ: {toast_edges}"

    tooltip_trigger = page.locator("#tooltip-trigger")
    tooltip_trigger.focus()
    expect(page.locator("#tooltip-content")).to_be_visible()
    tooltip_trigger.press("Escape")
    expect(page.locator("#tooltip-content")).to_be_hidden()

    popover_trigger = page.locator("#popover-trigger")
    popover_trigger.click()
    expect(page.locator("#popover-content")).to_be_visible()
    assert_focus(page, "#popover-close")
    page.keyboard.press("Escape")
    assert_focus(page, "#popover-trigger")

    dialog_open = page.locator("#dialog-open")
    dialog_open.click()
    expect(page.locator("#dialog-overlay")).to_be_visible()
    assert_focus(page, "#dialog-note")
    page.keyboard.press("Shift+Tab")
    assert_focus(page, "#dialog-save")
    page.keyboard.press("Tab")
    assert_focus(page, "#dialog-note")
    page.keyboard.press("Escape")
    assert_focus(page, "#dialog-open")

    delete_open = page.locator("#delete-open")
    delete_open.click()
    assert_focus(page, "#confirm-cancel")
    page.keyboard.press("Shift+Tab")
    assert_focus(page, "#confirm-delete")
    page.keyboard.press("Escape")
    assert_focus(page, "#delete-open")

    command_trigger = page.locator("#command-trigger")
    command_trigger.click()
    command_input = page.locator("#command-input")
    assert_focus(page, "#command-input")
    expect(command_input).to_have_attribute("aria-activedescendant", "command-option-new-note")
    command_input.press("End")
    expect(command_input).to_have_attribute("aria-activedescendant", "command-option-export")
    command_input.fill("offline")
    expect(page.locator("#command-status")).to_contain_text("unavailable")
    assert command_input.get_attribute("aria-activedescendant") is None
    command_input.fill("admin")
    expect(page.locator("#command-status")).to_contain_text("owner access")
    command_input.fill("no result exists")
    expect(page.locator("#command-status")).to_contain_text("No results")
    command_input.fill("")
    command_input.press("End")
    command_input.press("Enter")
    expect(page.locator("#command-overlay")).to_be_hidden()
    assert_focus(page, "#command-trigger")
    expect(page.locator("#command-result")).to_contain_text("Export current view selected")

    page.keyboard.press("Control+k")
    expect(page.locator("#command-overlay")).to_be_visible()
    page.keyboard.press("Escape")

    ai_send = page.locator("#ai-send")
    ai_send.click()
    expect(page.locator("#ai-stop")).to_be_visible()
    expect(page.locator("#ai-status")).to_contain_text("Streaming", timeout=1500)
    page.locator("#ai-stop").click()
    expect(page.locator("#ai-status")).to_contain_text("Stopped")
    expect(page.locator("#ai-output")).not_to_have_text("No generated content yet.")
    ai_send.click()
    expect(page.locator("#ai-status")).to_contain_text("Completed", timeout=4500)
    expect(page.locator("#ai-sources")).to_be_visible()

    focus_button = page.locator("#field-validate")
    focus_button.focus()
    outline_width = focus_button.evaluate("element => getComputedStyle(element).outlineWidth")
    assert float(outline_width.removesuffix("px")) >= 2


def main() -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    console_errors: list[str] = []
    page_errors: list[str] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 1000}, reduced_motion="no-preference")
        page = context.new_page()
        page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")
        run_interactions(page)
        page.reload()
        page.wait_for_load_state("networkidle")
        page.screenshot(path=str(ARTIFACT_DIR / "desktop-dark.png"), full_page=True)
        page.locator("#command-trigger").click()
        page.screenshot(path=str(ARTIFACT_DIR / "command-open.png"), full_page=False)
        page.keyboard.press("Escape")
        page.locator("#dialog-open").click()
        page.screenshot(path=str(ARTIFACT_DIR / "dialog-open.png"), full_page=False)
        page.keyboard.press("Escape")
        page.get_by_role("button", name="Page 2", exact=True).scroll_into_view_if_needed()
        page.get_by_role("button", name="Page 2", exact=True).click()
        page.screenshot(path=str(ARTIFACT_DIR / "toast-whole-silhouette.png"), full_page=False)

        page.set_viewport_size({"width": 390, "height": 844})
        page.reload()
        page.wait_for_load_state("networkidle")
        assert_no_small_targets(page)
        overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        overflowing = page.locator("body *").evaluate_all(
            """
            (elements) => elements
              .filter((element) => element.getClientRects().length)
              .map((element) => ({
                tag: element.tagName,
                id: element.id,
                className: typeof element.className === 'string' ? element.className : '',
                left: element.getBoundingClientRect().left,
                right: element.getBoundingClientRect().right,
                width: element.getBoundingClientRect().width
              }))
              .filter((item) => item.right > document.documentElement.clientWidth + 1 || item.left < -1)
              .slice(0, 20)
            """
        )
        assert overflow <= 1, f"narrow page horizontal overflow: {overflow}px; elements: {overflowing}"
        page.screenshot(path=str(ARTIFACT_DIR / "narrow-dark.png"), full_page=True)

        page.set_viewport_size({"width": 640, "height": 900})
        page.reload()
        page.wait_for_load_state("networkidle")
        zoom_overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        assert zoom_overflow <= 1, f"200% zoom horizontal overflow: {zoom_overflow}px"
        page.screenshot(path=str(ARTIFACT_DIR / "zoom-200-equivalent.png"), full_page=True)

        page.emulate_media(reduced_motion="reduce", forced_colors="active")
        page.reload()
        page.wait_for_load_state("networkidle")
        assert_no_small_targets(page)
        page.screenshot(path=str(ARTIFACT_DIR / "forced-colors-reduced-motion.png"), full_page=True)

        context.close()
        browser.close()

    assert not console_errors, f"browser console errors: {console_errors}"
    assert not page_errors, f"browser page errors: {page_errors}"
    print(f"Visual template interaction tests passed. Screenshots: {ARTIFACT_DIR}")


if __name__ == "__main__":
    main()
