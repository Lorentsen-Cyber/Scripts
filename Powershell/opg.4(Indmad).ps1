
#Henter diskens data
get-volume | select driveletter, FilesystemLabel, @{L='pct used';E={($_.sizeremaining/$_.size).ToString("P", $nfi)}}


<#Liste af Logs
$Wmi = Get-WmiObject -Class win32_operatingsystem
$RebootTime = $Wmi.ConvertToDateTime($Wmi.LastBootUpTime)
$RebootTime
$Entry = Get-EventLog -After $RebootTime -LogName Security | Where-Object {($_.EventID -eq '4624') -and ($_.EntryType -eq 'SuccessAudit')}
$lastLogon = $entry.TimeGenerated
$lastLogon
#>

#Liste af kritiske fejl
#Get-WinEvent system | Where-Object {$_.LevelDisplayName -eq "Kritisk"}

#oppe-tid
#get-date -gcim (Win32_OperatingSystem).LastBootUpTime | Select-Object Days, hours, Minutes, Seconds | Format-List 

#"oppe-tid" mangler stadig arbejde
