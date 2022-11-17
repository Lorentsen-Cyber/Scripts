function open()
{ 
   do{
    
    
    Clear-Host
    
    $Bogstav = Read-Host -Prompt "Indtast bogstav"
    #Sortere i hvilke tegn er vokaler og hvilke er konsonanter
    $vokaler = @("a","e","i","o","u","æ","ø","å")
    $konsonanter = @("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z")

    #Bygger outputtet for de forskellige udfald
    if($vokaler -contains $Bogstav){   
    
        Write-Host -ForegroundColor red "Vokal"  
    
    }
    elseif($konsonanter -contains $Bogstav){
    
        Write-Host -ForegroundColor DarkCyan "konsonant"
    
    }
    else{Write-Host -ForegroundColor Blue "Tumpe"}

    $stopprogram = Read-Host -Prompt "Færdig?"
    }until($stopprogram -eq "ja")
}
