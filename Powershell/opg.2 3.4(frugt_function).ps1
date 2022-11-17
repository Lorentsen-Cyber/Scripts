#Har valgt "Do until" Fordi det var den eneste funktion jeg kendte til


#Her er "Switchen" blevet smidt i en en function for mere kontrol 
function Fruit()
{
    do
    {
        Clear-Host
        Write-Host "Write a number"

        $x=Read-Host

        switch($x)
        {
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
            default{"A number between 1 and 10"}
         } 
         $sluk = Read-Host 

      } until($sluk -eq "nej")
}