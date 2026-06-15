# applies the kokuen look to Windows Terminal.
# install WT, launch it once (that creates settings.json), then run this.
# safe to re-run. backs up settings.json first.

$ErrorActionPreference = 'Stop'

# find the settings.json (store, preview, or unpackaged)
$cands = @(
  "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json",
  "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json",
  "$env:LOCALAPPDATA\Microsoft\Windows Terminal\settings.json"
)
$path = $cands | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $path) {
  Write-Host "couldn't find Windows Terminal settings.json." -ForegroundColor Yellow
  Write-Host "install Windows Terminal, open it once, then run this again." -ForegroundColor Yellow
  return
}

if (-not (Test-Path "$path.kokuen-bak")) { Copy-Item $path "$path.kokuen-bak" -Force; Write-Host "backup -> $path.kokuen-bak (original)" }
else { Write-Host "keeping existing pristine backup: $path.kokuen-bak" }

# read + strip // and /* */ comments (WT ships a JSONC file; 5.1's parser hates comments)
$raw = Get-Content $path -Raw
$noComments = [Text.RegularExpressions.Regex]::Replace(
  $raw,
  '("(?:\\.|[^"\\])*")|//[^\r\n]*|/\*[\s\S]*?\*/',
  { param($m) if ($m.Groups[1].Success) { $m.Groups[1].Value } else { '' } }
)
$cfg = $noComments | ConvertFrom-Json

function setp($o, $n, $v) {
  if ($o.PSObject.Properties[$n]) { $o.$n = $v } else { $o | Add-Member -NotePropertyName $n -NotePropertyValue $v -Force }
}

# --- the kokuen colour scheme ---
$scheme = [pscustomobject]@{
  name='kokuen'; background='#0A0A0A'; foreground='#E8E6E3'; cursorColor='#00FF2A'; selectionBackground='#2E2E2E'
  black='#2E2E2E'; red='#F87171'; green='#4ADE80'; yellow='#D6A960'; blue='#5B6BB5'; purple='#9D7BD8'; cyan='#3FB8A8'; white='#E8E6E3'
  brightBlack='#6E6E6E'; brightRed='#FCA5A5'; brightGreen='#00FF2A'; brightYellow='#F5C451'; brightBlue='#818CF8'; brightPurple='#C084FC'; brightCyan='#5EEAD4'; brightWhite='#F5F4F1'
}
if (-not $cfg.PSObject.Properties['schemes']) { setp $cfg 'schemes' @() }
$cfg.schemes = @($cfg.schemes | Where-Object { $_.name -ne 'kokuen' }) + $scheme

# --- defaults that apply to every profile (the mac look) ---
if (-not $cfg.PSObject.Properties['profiles']) { setp $cfg 'profiles' ([pscustomobject]@{}) }
if ($cfg.profiles -is [array]) { $cfg.profiles = [pscustomobject]@{ list = $cfg.profiles } }   # old array form -> object
if (-not $cfg.profiles.PSObject.Properties['defaults']) { setp $cfg.profiles 'defaults' ([pscustomobject]@{}) }
$d = $cfg.profiles.defaults
setp $d 'colorScheme' 'kokuen'
setp $d 'font' ([pscustomobject]@{ face='SF Mono'; size=12; weight='normal' })
setp $d 'padding' '14'
setp $d 'cursorShape' 'bar'
setp $d 'opacity' 100                  # solid, fully opaque
setp $d 'useAcrylic' $false            # no blur/transparency — kokuen is flat
setp $d 'antialiasingMode' 'grayscale'
setp $d 'scrollbarState' 'hidden'     # kokuen keeps scrollbars out of the way
setp $d 'intenseTextStyle' 'bold'

# --- app theme so the tab/title bar matches the bg (no grey mica strip) ---
$theme = [pscustomobject]@{
  name='kokuen'
  window=[pscustomobject]@{ applicationTheme='dark' }
  tabRow=[pscustomobject]@{ background='#0A0A0A'; unfocusedBackground='#0A0A0A' }
}
if (-not $cfg.PSObject.Properties['themes']) { setp $cfg 'themes' @() }
$cfg.themes = @($cfg.themes | Where-Object { $_.name -ne 'kokuen' }) + $theme
setp $cfg 'theme' 'kokuen'
# leave launchMode default (normal window with a close button). WT can't do square corners or a
# clean closable borderless window — use the WezTerm config for that.

$cfg | ConvertTo-Json -Depth 32 | Set-Content $path -Encoding UTF8
Write-Host "kokuen applied. restart Windows Terminal to see it." -ForegroundColor Green
Write-Host "tip: Ctrl+Shift+P -> 'Toggle focus mode' hides the tab bar for the cleanest look."
