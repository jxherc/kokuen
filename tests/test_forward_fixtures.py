#!/usr/bin/env python3
"""Rendered proof that KOKUEN contracts do not impose one product theme."""

from __future__ import annotations

import os
from pathlib import Path

from playwright.sync_api import Page, expect, sync_playwright

ROOT_URL = os.environ.get("KOKUEN_ROOT_URL", "http://127.0.0.1:4312")
ARTIFACT_DIR = Path(
    os.environ.get("KOKUEN_FORWARD_ARTIFACT_DIR", "/tmp/kokuen-v5-forward-tests")
)

FIXTURES = {
    "writer": "/tests/forward-fixtures/writer.html",
    "operations": "/tests/forward-fixtures/operations.html",
    "media": "/tests/forward-fixtures/media.html",
}


def assert_no_small_targets(page: Page) -> None:
    failures = page.locator(
        "button, a[href], input, textarea, [role=slider], [tabindex='0']"
    ).evaluate_all(
        """
        (elements) => elements
          .filter((element) => element.getClientRects().length)
          .filter((element) => getComputedStyle(element).visibility !== 'hidden')
          .map((element) => {
            const box = element.getBoundingClientRect();
            return {
              label: element.getAttribute('aria-label') || element.textContent.trim().slice(0, 50),
              id: element.id,
              width: box.width,
              height: box.height
            };
          })
          .filter((item) => item.width < 43.5 || item.height < 43.5)
        """
    )
    assert not failures, f"interactive targets below 44px: {failures}"


def assert_no_page_overflow(page: Page, label: str) -> None:
    overflow = page.evaluate(
        "document.documentElement.scrollWidth - document.documentElement.clientWidth"
    )
    offenders = page.locator("body *").evaluate_all(
        """
        (elements) => elements
          .filter((element) => element.getClientRects().length)
          .map((element) => {
            const box = element.getBoundingClientRect();
            return {
              tag: element.tagName,
              id: element.id,
              className: typeof element.className === 'string' ? element.className : '',
              left: box.left,
              right: box.right,
              width: box.width,
              scrollWidth: element.scrollWidth,
              clientWidth: element.clientWidth
            };
          })
          .filter((item) => item.right > document.documentElement.clientWidth + 1 || item.left < -1)
          .slice(0, 12)
        """
    )
    containers = page.locator("html, body, .ops-shell, .ops-main, .ledger-wrap").evaluate_all(
        """
        (elements) => elements.map((element) => {
          const box = element.getBoundingClientRect();
          const style = getComputedStyle(element);
          return {
            tag: element.tagName,
            className: typeof element.className === 'string' ? element.className : '',
            left: box.left,
            right: box.right,
            width: box.width,
            scrollWidth: element.scrollWidth,
            clientWidth: element.clientWidth,
            overflowX: style.overflowX,
            contain: style.contain
          };
        })
        """
    )
    assert overflow <= 1, (
        f"{label} has {overflow}px viewport overflow; offenders: {offenders}; "
        f"containers: {containers}"
    )


def assert_focused(page: Page, selector: str) -> None:
    try:
        expect(page.locator(selector)).to_be_focused(timeout=1500)
    except AssertionError as error:
        active = page.evaluate("document.activeElement.outerHTML.slice(0, 180)")
        raise AssertionError(f"expected focus on {selector}, got {active}") from error


def exercise_writer(page: Page) -> None:
    expect(page.locator("body")).to_have_css("background-color", "rgb(234, 241, 237)")
    trigger = page.locator("#open-command")
    trigger.click()
    assert_focused(page, "#command-input")
    page.keyboard.press("Shift+Tab")
    assert_focused(page, "#writer-command-export")
    page.keyboard.press("Escape")
    assert_focused(page, "#open-command")
    page.keyboard.press("Control+k")
    expect(page.locator("#command-overlay")).to_be_visible()
    page.keyboard.press("Escape")


def exercise_operations(page: Page) -> None:
    expect(page.locator("body")).to_have_css("background-color", "rgb(21, 18, 14)")
    third_check = page.locator(".row-check").nth(2)
    third_check.click()
    expect(third_check).to_have_attribute("aria-checked", "true")
    third_check.click()
    expect(third_check).to_have_attribute("aria-checked", "false")

    filter_field = page.locator("#event-filter")
    filter_field.fill("payment")
    page.locator("#clear-filter").click()
    expect(filter_field).to_have_value("")
    assert_focused(page, "#event-filter")

    page.locator("#open-confirm").click()
    assert_focused(page, "#cancel-close")
    page.keyboard.press("Shift+Tab")
    assert_focused(page, "#confirm-close")
    page.locator("#confirm-close").click()
    expect(page.locator("#confirm-close")).to_have_attribute("aria-busy", "true")
    expect(page.locator("#operation-status")).to_contain_text(
        "EVT-2041 and EVT-2038 closed", timeout=2000
    )
    assert_focused(page, "#open-confirm")


def exercise_media(page: Page) -> None:
    expect(page.locator("body")).to_have_css("background-color", "rgb(23, 13, 17)")
    programs = page.locator(".program-art")
    programs.nth(1).click()
    expect(programs.nth(0)).to_have_attribute("aria-pressed", "false")
    expect(programs.nth(1)).to_have_attribute("aria-pressed", "true")
    expect(page.locator("#player-title")).to_have_text("Blue hour bus")

    play = page.locator("#play-toggle")
    play.click()
    expect(play).to_have_attribute("aria-pressed", "false")
    expect(play).to_have_attribute("aria-label", "Play Blue hour bus")

    page.locator("#open-search").click()
    assert_focused(page, "#search-input")
    page.keyboard.press("Shift+Tab")
    assert_focused(page, "#media-search-last")
    page.keyboard.press("Escape")
    assert_focused(page, "#open-search")


def main() -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    console_errors: list[str] = []
    page_errors: list[str] = []
    exercise = {
        "writer": exercise_writer,
        "operations": exercise_operations,
        "media": exercise_media,
    }

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 1000})
        page = context.new_page()
        page.on(
            "console",
            lambda message: console_errors.append(message.text)
            if message.type == "error"
            else None,
        )
        page.on("pageerror", lambda error: page_errors.append(str(error)))

        for name, path in FIXTURES.items():
            page.goto(ROOT_URL + path)
            page.wait_for_load_state("networkidle")
            assert_no_small_targets(page)
            assert_no_page_overflow(page, f"{name} desktop")
            exercise[name](page)
            page.screenshot(
                path=str(ARTIFACT_DIR / f"{name}-desktop.png"), full_page=True
            )

            page.set_viewport_size({"width": 390, "height": 844})
            page.reload()
            page.wait_for_load_state("networkidle")
            assert_no_small_targets(page)
            assert_no_page_overflow(page, f"{name} narrow")
            page.screenshot(
                path=str(ARTIFACT_DIR / f"{name}-narrow.png"), full_page=True
            )

            page.set_viewport_size({"width": 640, "height": 900})
            page.emulate_media(reduced_motion="reduce")
            page.reload()
            page.wait_for_load_state("networkidle")
            assert_no_small_targets(page)
            assert_no_page_overflow(page, f"{name} 200-percent equivalent")
            page.screenshot(
                path=str(ARTIFACT_DIR / f"{name}-reduced-motion.png"), full_page=True
            )
            page.emulate_media(reduced_motion="no-preference")
            page.set_viewport_size({"width": 1440, "height": 1000})

        context.close()
        browser.close()

    assert not console_errors, f"browser console errors: {console_errors}"
    assert not page_errors, f"browser page errors: {page_errors}"
    print(
        "Forward fixtures passed: 3 distinct product directions, wide/narrow/"
        f"200-percent-equivalent checks, screenshots in {ARTIFACT_DIR}"
    )


if __name__ == "__main__":
    main()
