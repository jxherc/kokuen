-- kokuen for wezterm. square, flat, SF Mono, grey ramp + green signal.
-- drop this at  C:\Users\<you>\.wezterm.lua  (or ~/.config/wezterm/wezterm.lua)
-- the prompt + syntax colours come from the powershell profile (see kokuen-prompt.ps1).

local wezterm = require 'wezterm'
local config = wezterm.config_builder()

-- launch Windows PowerShell so the kokuen profile loads. -NoLogo kills the startup banner
config.default_prog = { 'powershell.exe', '-NoLogo' }

-- font
config.font = wezterm.font 'SF Mono'
config.font_size = 12.0
config.warn_about_missing_glyphs = false

-- window: no OS title bar (square corners on win11), but keep min/max/close in a slim strip
config.window_decorations = 'RESIZE|INTEGRATED_BUTTONS'
config.integrated_title_button_style = 'Windows'
config.window_background_opacity = 1.0           -- solid, no acrylic
config.window_padding = { left = 14, right = 14, top = 10, bottom = 8 }
config.adjust_window_size_when_changing_font_size = false

-- thin green bar cursor (the one signal colour)
config.default_cursor_style = 'SteadyBar'
config.cursor_thickness = '1.5px'

-- slim tab strip, painted kokuen so it blends (it also holds the window buttons)
config.use_fancy_tab_bar = true
config.hide_tab_bar_if_only_one_tab = false
config.tab_max_width = 26
config.window_frame = {
  font = wezterm.font { family = 'SF Mono', weight = 'Medium' },
  font_size = 10.0,
  active_titlebar_bg = '#0a0a0a',
  inactive_titlebar_bg = '#0a0a0a',
}

-- kokuen palette
config.colors = {
  foreground    = '#e8e6e3',
  background    = '#0a0a0a',
  cursor_bg     = '#00ff2a',
  cursor_fg     = '#0a0a0a',
  cursor_border = '#00ff2a',
  selection_bg  = '#2e2e2e',
  selection_fg  = '#e8e6e3',
  scrollbar_thumb = '#2e2e2e',
  split         = '#2e2e2e',
  -- normal:  black     red        green      yellow     blue       magenta    cyan       white
  ansi    = { '#2e2e2e', '#f87171', '#4ade80', '#d6a960', '#5b6bb5', '#9d7bd8', '#3fb8a8', '#e8e6e3' },
  brights = { '#6e6e6e', '#fca5a5', '#00ff2a', '#f5c451', '#818cf8', '#c084fc', '#5eead4', '#f5f4f1' },
  tab_bar = {
    background = '#0a0a0a',
    active_tab         = { bg_color = '#0a0a0a', fg_color = '#e8e6e3' },
    inactive_tab       = { bg_color = '#0a0a0a', fg_color = '#6e6e6e' },
    inactive_tab_hover = { bg_color = '#0e0e0e', fg_color = '#e8e6e3' },
    new_tab            = { bg_color = '#0a0a0a', fg_color = '#6e6e6e' },
    new_tab_hover      = { bg_color = '#0e0e0e', fg_color = '#e8e6e3' },
  },
}

-- quiet + tidy
config.audible_bell = 'Disabled'
config.window_close_confirmation = 'NeverPrompt'
config.enable_scroll_bar = false
config.scrollback_lines = 10000

return config
