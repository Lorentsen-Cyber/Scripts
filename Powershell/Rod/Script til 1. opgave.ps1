
#Serienummer på disken
Get-WMIObject win32_physicalmedia | Format-List Tag,SerialNumber

#Step 2 liste over de 10 længtse filer
Get-ChildItem -Path c:\ -Recurse -ErrorAction SilentlyContinue | Sort-Object -Descending -Property length | Select-Object -First 10 name, length

#Liste af 10 ældste dll filer
Get-ChildItem  -path C:\ -include *.dll -Recurse -ErrorAction SilentlyContinue | Sort-Object -Descending -Property LastWriteTime | Select-Object -First 10 name, LastWriteTime

#Sortere Hotfixes efter Beskrivelse
Get-HotFix | Sort-Object -Descending -Property description


#lokere hukommelse
Get-WmiObject Win32_operatingsystem | Select freevirtualmemory, freephysicalmemory 

#Viser version
Get-Host | Select-Object version, name | Format-List 
