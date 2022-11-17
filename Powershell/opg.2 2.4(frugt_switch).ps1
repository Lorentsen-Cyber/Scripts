Clear-Host
Write-Host "Write a number"

$x=Read-Host

Switch($x)
{
    
    #Displayer en frugt ud fra hvilket tal er valgt
    1{"Apple"}
    2{"Pear"}
    3{"Banana"}
    4{"Melon"}
    5{"Tomato"}
    6{"Grape"}
    7{"Mango"}
    8{"Plum"}
    9{"Orange"}
    10{"Lemon"}
    #Hvis der ikke bliver valgt et passende tal svarer den med default 
    default{"A number between 1 and 10"}

}