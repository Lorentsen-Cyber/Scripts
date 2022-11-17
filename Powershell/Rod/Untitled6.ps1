{
$Wmi = Get-WmiObject -Class win32_operatingsystem
$RebootTime = $Wmi.ConvertToDateTime($Wmi.LastBootUpTime)
$RebootTime
$Entry = Get-EventLog -After $RebootTime -LogName Security | Where-Object {($_.EventID -eq '4624') -and ($_.EntryType -eq 'SuccessAudit')}
$lastLogon = $entry.TimeGenerated
$lastLogon
}