Clear-Host

Write-Host "Sidste reboot"

$wmi = Get-WmiObject -Class Win32_OperatingSystem
$rebootTime = $wmi.ConvertToDateTime($wmi.LastBootUpTime)
$rebootTime