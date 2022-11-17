#Denne function er for at organisere hele scriptet, og formatere det til et menu format
function menu() 
{
    do
    {
        #Selve "GUI'et" af menuen
        Clear-Host
        Write-Host "
            #----------------------------------------------------------#
            #                 Enkle cmdlet opgaver                     #
            #                                                          #
            #                                                          #
            #   1. Serienummeret på disken på maskinen                 #
            #   2. De ti største/længste filer på maskinen             #
            #   3. Find de ti ældste dll filer på maskinen             #
            #                                                          #
            #   5. HotFix’es på maskinen sorteret efter Description    #
            #   6. Ledig fysisk hukommelse                             #
            #   7. Ledig virtuel hukommelse                            #
            #                                                          #
            #   8. PowerShell versionen                                #
            #                                                          #
            #   0. Slut                                                #
            #                                                          #
            #                                                          #
            #----------------------------------------------------------#
            "

        $hovedmenu = read-host "Indtast valgmulighed"
        #Switch til køre igennem de forskellige functions i menu'en
        switch ($hovedmenu)
        {
            1 {SerieNummer}
            2 {TiStoerste}
            3 {Aeldste}

            5 {HotFixDesc}
            6 {LedigFysiskHukommelse}
            7 {LedigVirtuelHukommelse}

            8 {PSVersion}

            0 {LukMeny}
            
                default 
                {
                    Write-Host -ForegroundColor red "Forkert valgmulighed"
                    sleep 2
                }
        }
    } until ($hovedmenu -eq 0)
}

#Function til at fremvise Serienummeret på fysisk disk
function SerieNummer
{ 
    Get-WMIObject win32_physicalmedia | Format-List Tag,SerialNumber
    Write-Host 'SerieNummer - Tast Enter' -NoNewline
    Read-Host
}

#Finder de 10 stoerste filer på maskinen
function TiStoerste
{
    Get-ChildItem -Path c:\ -Recurse -ErrorAction SilentlyContinue | Sort-Object -Descending -Property length | Select-Object -First 10 name, length
    Write-Host 'TiStoerste - Tast enter' -NoNewline
    Read-Host
}

#Finder de 10 aeldste .dll filer på maskinen
function Aeldste
{
    Get-ChildItem  -path C:\ -include *.dll -Recurse -ErrorAction SilentlyContinue | Sort-Object -Descending -Property LastWriteTime | Select-Object -First 10 name, LastWriteTime
    Write-Host 'Aeldste - Tast enter' -NoNewline
    Read-Host
}

#Finder hotfix'es på maskinen sorteret efter beskrivelse
function HotFix
{
    Get-HotFix | Sort-Object -Descending -Property description
    Write-Host 'HotFixDesc - Tast enter' -NoNewline
    Read-Host
}

#Viser ledig fysisk hukommelse på disken
function LedigFysiskHukommelse
{
    Get-WmiObject Win32_operatingsystem | Select-Object freephysicalmemory 
    Write-Host 'LedigFysiskHukommelse - Tast enter' -NoNewline
    Read-Host
}

#Viser ledig virtuel hukommelse på disken
function LedigVirtuelHukommelse
{
    Get-WmiObject Win32_operatingsystem | Select freevirtualmemory
    Write-Host 'LedigVirtuelHukommelse - Tast enter' -NoNewline
    Read-Host
}

#Henter PS Versionen
function PSVersion
{
    Get-Host | Select-Object Name, Version | Format-Table
    Write-Host 'PS Version - Tast enter' -NoNewline
    Read-Host
}

#lukker menu'en igen
function LukMeny
{
    Write-Host 'Så lukker vi bixen ;-)' 
    sleep 2
}

menu