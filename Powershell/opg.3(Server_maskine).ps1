function Server() 
{
    do
    {
        Clear-Host
        Write-Host "
            #----------------------------------------------------------#
            #                 Enkle cmdlet opgaver                     #
            #                                                          #
            #                                                          #
            #   1. Operativ system info                                #
            #   2. Patch level                                         #
            #   3. IPv4 adresser, Subnet maske, Default gateway,       #
            #      DNS server                                          #
            #   4. Alle shares med rettigheder i alfabetisk orden.     #
            #   5. Liste over alle services som starter                #
            #      automatisk i Windows.                               #
            #   6. Dato og klokkeslæt for sidste genstart af serveren. #                              
            #   7. Opret virtuel maskine                               #
            #   8. Fjern valgte VM                                     #
            #   0. Sluk                                                #
            #                                                          #
            #                                                          #
            #----------------------------------------------------------#
            "
             $hovedmenu = read-host "Indtast valgmulighed"

        switch ($hovedmenu)
        {
            1 {System}
            2 {patch}
            3 {IP}
            4 {Shares}
            5 {List}
            6 {Dato}
            7 {Create_VM}
            8 {remove-VM}
            0 {Sluk}

            default 
            {
                Write-Host -ForegroundColor red "Det dur ikke"
                sleep 1
            }
        }
    } until ($hovedmenu -eq 0)
}

#Fremviser systen info
function System()
{
    Get-WMIObject win32_operatingsystem
    Write-Host 'System info - Tast Enter' -NoNewline
    Read-Host
}

#Henter patches
function Patch()
{
    Get-HotFix | Sort-Object -Descending -Property InstalledOn | format-table
    Write-Host 'Patch level - Tast Enter' -NoNewline
    Read-Host
}

#Fremviser NIC konfiguration
function IP()
{
    netsh interface ip show config name="vEthernet (Internet)" | Format-Table | Sort-Object -Descending
    Write-Host 'ipconfig - Tast Enter' -NoNewline
    Read-Host
}

#Fremviser Shares på maskinen
function Shares()
{
    Get-SmbShare | Select-Object name, Description | format-table
    Write-Host 'Shares - Tast Enter' -NoNewline
    Read-Host

}

#Liste af alle aktive tjenester
function List()
{
    Get-WmiObject win32_service -Filter "startmode = 'Auto'" | Select-Object name,processid | Sort-Object -Property name | format-table
    Write-Host 'Liste af services - Tast Enter' -NoNewline
    Read-Host
}

#Viser sidste genstart af maskinen
function dato()
{
    Get-CimInstance -ClassName Win32_OperatingSystem | select csname, lastbootuptime | format-table
    Write-Host 'sidste reboot - Tast Enter' -NoNewline
    Read-Host
}

#7(Husk at opdatere paths)
function Create_VM()
{
    $vm = Read-Host -Prompt "Indtast navn på maskine"
    $image = "C:\Users\Administrator\Downloads\17763.737.190906-2324.rs5_release_svc_refresh_SERVER_EVAL_x64FRE_en-us_1.iso"
    $vmswitch = "Intranet"
    $port = "port1"
    $Vlan = 210
    $cpu =2
    $ram = Read-Host -Prompt "antal ram"
    $path_to_disk = "C:\Users\Administrator\Desktop\Powershell_test"
    $disk_size = Read-Host -Prompt "Size af disk"

    New-VM $vm -Generation 2 -Path $path_to_disk
    Set-VM $vm -ProcessorCount $cpu -MemoryStartupBytes (Invoke-Expression $ram)
    New-VHD -Path $path_to_disk\$vm-disk1.vhdx -SizeBytes (Invoke-Expression $disk_size)
    Add-VMHardDiskDrive -VMName $vm -Path $path_to_disk\$vm-disk1.vhdx
    Set-VMDvdDrive -VMName $vm -Path $image
    Remove-VMNetworkAdapter -VMName $vm
    Add-VMNetworkAdapter -VMName $vm -Name $port

    $startvm = Read-Host -Prompt "Vil du starte maskinen? Y/N"
    If($startvm -eq "Y")
    {
        Start-VM $vm
    }
    Write-Host 'VM Oprettet - Tast Enter' -NoNewline
    Read-Host
}

#Fjerner valgte VM fra maskinen
function remove-VM()
{
    $navn = Read-Host -Prompt "Navn Paa den VM du vil fjerne"

    Remove-VM -Name $navn

    $dest = "C:\Users\Administrator\Desktop\Powershell_test\*"

    Remove-Item -path $dest -Recurse
    Write-Host 'sidste reboot - Tast Enter' -NoNewline
    Read-Host
}

#lukker menu'en
function sluk()
{
Write-Host -ForegroundColor Blue 'Moejn' 
    sleep 2
}

Server