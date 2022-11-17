#OS info
###Get-WMIObject win32_operatingsystem


# Patch level[WIP]
###Get-HotFix | Sort-Object -Descending -Property InstalledOn

# IPconfig[WIP]
###ipconfig /all

#
###Get-SmbShare | Select-Object name, Description

#  List of services
###Get-WmiObject win32_service -Filter "startmode = 'Auto'" | Select-Object name,processid | Sort-Object -Property name

# Sidste start af server
###Get-CimInstance -ClassName Win32_OperatingSystem | select csname, lastbootuptime