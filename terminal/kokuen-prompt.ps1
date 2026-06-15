# kokuen prompt + syntax colours for Windows PowerShell 5.1 / PowerShell 7.
# dot-source it from your $PROFILE:   . "C:\path\to\kokuen-prompt.ps1"
#
# notes from the road:
#  - colours use [char]27 for ESC, NOT `e — `e doesn't exist in PS 5.1 and renders as literal junk.
#  - InlinePrediction is a PSReadLine 2.1+ colour key; on 2.0 it throws and takes the whole
#    Set-PSReadLineOption call down with it. so it's set separately in its own try.

$script:kk = @{ Text = 'e8e6e3'; Muted = '6e6e6e'; Faint = '2e2e2e'; Signal = '00ff2a'; Danger = 'f87171' }

function script:Ansi([string]$hex) {
  $r = [Convert]::ToInt32($hex.Substring(0,2),16)
  $g = [Convert]::ToInt32($hex.Substring(2,2),16)
  $b = [Convert]::ToInt32($hex.Substring(4,2),16)
  "$([char]27)[38;2;$r;$g;${b}m"
}

function script:ShortPath {
  $p = (Get-Location).Path
  $home = [Environment]::GetFolderPath('UserProfile')
  if ($p.StartsWith($home,[StringComparison]::OrdinalIgnoreCase)) { return '~' + $p.Substring($home.Length) }
  $p
}

if (Get-Module -ListAvailable -Name PSReadLine) {
  Import-Module PSReadLine -ErrorAction SilentlyContinue
  Set-PSReadLineOption -EditMode Windows
  $e = [char]27
  Set-PSReadLineOption -Colors @{
    Command   = "${e}[38;2;232;230;227m"   # text
    Parameter = "${e}[38;2;110;110;110m"   # muted
    Operator  = "${e}[38;2;110;110;110m"
    Variable  = "${e}[38;2;232;230;227m"
    String    = "${e}[38;2;0;255;42m"      # signal green
    Number    = "${e}[38;2;0;255;42m"
    Type      = "${e}[38;2;212;210;206m"
    Comment   = "${e}[38;2;110;110;110m"
    Keyword   = "${e}[38;2;232;230;227m"
    Error     = "${e}[38;2;248;113;113m"   # error red
    Selection = "${e}[48;2;46;46;46m"      # faint bg
    Default   = "${e}[38;2;232;230;227m"
  }
  try { Set-PSReadLineOption -Colors @{ InlinePrediction = "${e}[38;2;46;46;46m" } } catch {}
}

# muted time + path on one line, a dim grey > on the next
function global:prompt {
  $reset = "$([char]27)[0m"
  $muted = Ansi $script:kk.Muted
  $text  = Ansi $script:kk.Text
  "$muted$(Get-Date -Format HH:mm)$reset $text$(ShortPath)$reset`n$muted>$reset "
}
