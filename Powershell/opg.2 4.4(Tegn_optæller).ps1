clear-host

#Her åbner den filen op tæller alle vokalerne op
$vocal=(Get-Content C:\Users\Administrator\Desktop\Test.txt | Select-String -Pattern "a|e|i|o|u" -AllMatches).matches.count
#Og her tæller den alle konsonanterne op
$consonant=(Get-Content C:\Users\Administrator\Desktop\Test.txt | Select-String -Pattern "b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|z" -AllMatches).matches.count
#Her tæller den alt andet op og trækker de tidligere variabler fra, minus mellemrum
$TotalChars=(Get-Content C:\Users\Administrator\Desktop\Test.txt | Measure-Object -ignorewhitespace -Character).Characters 
$sign = $TotalChars - $vocal -$consonant
  Write-Host "Vokaler: $vocal Konsonanter: $consonant Tegn: $sign"