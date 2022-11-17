function Stats() 
{
    do
    {
        Clear-Host
        Write-Host "
            #----------------------------------------------------------#
            #                 Enkle cmdlet opgaver                     #
            #                                                          #
            #                                                          #
            #   1. Disk stoerrelse                                     #
            #   2. Liste af logs                                       #
            #   3. Liste med kritiske fejl                             #
            #   4. Uptime                                              #
            #                                                          #
            #   0. Sluk                                                #
            #                                                          #
            #                                                          #
            #----------------------------------------------------------#
            "
             $hovedmenu = read-host "Indtast valgmulighed"

        switch ($hovedmenu)
        {
            1 {disk-str}
            2 {logs}
            3 {errors}
            4 {uptime}
            0 {Sluk}

            default 
            {
                Write-Host -ForegroundColor red "Det dur ikke"
                sleep 1
            }
        }
    } until ($hovedmenu -eq 0)
}

#Henter diskens data
function disk-str()
{
    get-volume | select driveletter, FilesystemLabel, @{L='pct used';E={($_.sizeremaining/$_.size).ToString("P", $nfi)}} | format-table
    Write-Host 'Disk str. - Tast Enter' -NoNewline
    Read-Host
}

#Liste af Logs
function Logs()
{
    $Wmi = Get-WmiObject -Class win32_operatingsystem
    $RebootTime = $Wmi.ConvertToDateTime($Wmi.LastBootUpTime)
    $RebootTime
    $Entry = Get-EventLog -After $RebootTime -LogName Security | Where-Object {($_.EventID -eq '4624') -and ($_.EntryType -eq 'SuccessAudit')}
    $lastLogon = $entry.TimeGenerated
    $lastLogon
        Write-Host 'Liste af logs - Tast Enter' -NoNewline
        Read-Host
}

#Liste af kritiske fejl
function errors()
{
    Get-WinEvent system | Where-Object {$_.LevelDisplayName -eq "Kritisk"} | format-list
    Write-Host 'Kritiske fejl - Tast Enter' -NoNewline
    Read-Host
}

#oppe-tid
function uptime()
{
    (get-date) - (gcim Win32_OperatingSystem).LastBootUpTime | Select-Object Days, hours, Minutes, Seconds | Format-List
    Write-Host 'Oppetid - Tast Enter' -NoNewline
    Read-Host

}

#Lukker for menu'en
function sluk()
{
Write-Host -ForegroundColor Blue 'Moejn' 
    sleep 2
}

stats