#Fjerner valgte VM fra maskinen


$navn = Read-Host -Prompt "Navn Paa den VM du vil fjerne"

Remove-VM -Name $navn

$dest = "C:\Users\Administrator\Desktop\Powershell_test\*"

Remove-Item -path $dest -Recurse