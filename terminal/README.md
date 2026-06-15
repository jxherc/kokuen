# kokuen for your terminal

The kokuen look for a terminal: JetBrains Mono, grey-on-near-black, a green bar cursor, solid flat
background, padding. Matches the conhost theme and your site. Two setups below —
WezTerm (square corners, no title bar) or Windows Terminal.

## WezTerm

Copy [`kokuen.wezterm.lua`](kokuen.wezterm.lua) to `C:\Users\<you>\.wezterm.lua` and open WezTerm.
That's the whole setup — it launches Windows PowerShell so your kokuen prompt loads too.

`window_decorations = 'RESIZE|INTEGRATED_BUTTONS'` drops the OS title bar (square corners on win11)
but keeps min/max/close in a slim strip, so you can still mouse-close. Close a tab with Ctrl+Shift+W,
the window with Alt+F4. Solid bg, no acrylic.

## do this

1. Install Windows Terminal (one of):
   - `winget install Microsoft.WindowsTerminal`
   - or the Microsoft Store
2. **Open it once** so it writes its `settings.json`.
3. Run the script:
   ```powershell
   & "C:\Users\jxh\kokuen-terminal\apply-kokuen-wt.ps1"
   ```
4. Restart Windows Terminal.

The script backs up your `settings.json` first (`settings.json.kokuen-bak`, keeps the original on
re-runs) and is safe to re-run.

Note: WT can't do square corners (Win11 rounds every window, no setting for it), and focus mode has
no close button. That's why WezTerm above exists. If you stay on WT and want focus mode, add
`"launchMode": "focus"` — close with Alt+F4 / `exit` / Ctrl+Shift+W.

## the prompt + syntax colours

The scheme above only colours the window. For the kokuen *prompt* (muted time + path, a green `>`
that goes red when a command fails) and matching PSReadLine syntax colours, dot-source
[`kokuen-prompt.ps1`](kokuen-prompt.ps1) from your `$PROFILE`:

```powershell
# in $PROFILE (run `notepad $PROFILE`)
. "C:\Users\jxh\kokuen-terminal\kokuen-prompt.ps1"
```

Two gotchas it works around, both of which silently broke an earlier version:
- escape char is `[char]27`, not `` `e `` — `` `e `` doesn't exist in PS 5.1.
- `InlinePrediction` is a PSReadLine 2.1+ colour key; on 2.0 it throws and kills the whole colour
  block (so commands fall back to PSReadLine's default yellow). It's set off on its own here.

## what it sets (in profiles.defaults, so every shell gets it)

| setting | value | why |
|---|---|---|
| colorScheme | kokuen | the grey ramp + green signal |
| font | JetBrains Mono, 12 | ligatures on |
| opacity + useAcrylic | 100 + false | solid flat bg, no transparency |
| padding | 14 | room to breathe; conhost can't pad |
| cursorShape | bar | thin mac-style caret |
| cursorColor | #00FF2A | green = "live", the one signal colour |
| scrollbarState | hidden | keep it clean |
| theme | kokuen | tab/title bar painted #0a0a0a, no grey mica strip |

## tweaks

- green cursor too loud? change `cursorColor` in `kokuen.json` (and the scheme block in the script)
  to `#E8E6E3`.
- default is solid. if you ever want a little transparency, drop `opacity` below 100 — with
  `useAcrylic` false that's clean non-blurred transparency.
- bigger text? bump `font.size`.
- font is JetBrains Mono (ligatures on — `->` `!=` `>=` fuse). want plain SF Mono back? change `font.face`.

## manual way (if you'd rather not run the script)

Open Settings (Ctrl+,) → "Open JSON file". Paste the object from `kokuen.json` into the `"schemes": [ ]`
array, then under `"profiles": { "defaults": { } }` set `"colorScheme": "kokuen"`, the font, opacity,
useAcrylic, padding, cursorShape. Same values as the table above.
