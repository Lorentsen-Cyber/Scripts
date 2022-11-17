Clear-Host


$vm = Read-Host -Prompt "Indtast navn på maskine"
#skriv stien til iso fil i image variablen
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