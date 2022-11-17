#Opg. 7 

#function for at hente systen-info på systemet
function System()
{
    Get-WMIObject win32_operatingsystem | format-table
    Write-Host 'System info - Tast Enter' -NoNewline
    Read-Host
}

#Henter Status på NIC
function IP()
{
    netsh interface ip show config name="vEthernet (Internet)" | Format-Table | Sort-Object -Descending
    Write-Host 'ipconfig - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
}

#Sidste genstart af maskinen
function last-boot()
{
    Get-CimInstance -ClassName Win32_OperatingSystem | select csname, lastbootuptime | format-table
    Write-Host 'sidste reboot - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
}

#Viser ledig disk-plads
function view-space()
{
    get-volume | select driveletter, FilesystemLabel, @{L='pct used';E={($_.sizeremaining/$_.size).ToString("P", $nfi)}} | Format-Table
    Write-Host 'Ledig disk plads - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
}

#Opretter Virtuel Maskine
function Create-VM()
{

Clear-Host


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
    Write-Host 'VM installeret - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
}

#Fjerner valgte VM fra maskinen
function delete-VM()
{
    $navn = Read-Host -Prompt "Navn Paa den VM du vil fjerne"

    Remove-VM -Name $navn

    $dest = "C:\Users\Administrator\Desktop\Powershell_test\*"

    Remove-Item -path $dest -Recurse
    Write-Host 'VM Fjernet - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
}

#Viser de 20 Største filer
function StoersteFiler()
{
    Clear-Host
    Write-Host "10 stoerste Userfiler" -ForegroundColor Red

    Get-ChildItem -Path C:\Users -Recurse -ErrorAction SilentlyContinue | Sort-Object -Descending -Property Length | Select-Object -First 20 name, Length, LastWriteTime  | Format-Table -AutoSize

    Write-Host "10 stoerste Systemfiler" -ForegroundColor Red
    Get-ChildItem -Path C:\Windows -Recurse -ErrorAction SilentlyContinue | Sort-Object -Descending -Property Length | Select-Object -First 20 name, Length, LastWriteTime  | Format-Table -AutoSize

    Write-Host '20 stoerste filer - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
    }

#Viser shares på maskinen
function Shares()
{
    Get-SmbShare | Select-Object name, Description | format-table
    Write-Host 'Shares - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
}

#Serienummer på disken
function SerieNummer
{
    Get-WMIObject win32_physicalmedia | Format-List Tag,SerialNumber
    Write-Host 'SerieNummer - Tast Enter' -NoNewline
    Read-Host
    Clear-Host
}