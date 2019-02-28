##Lines used for Reference.
# Get-AppxPackage *3dbuilder* | Remove-AppxPackage
# Get-AppxPackage *windowsalarms* | Remove-AppxPackage
# Get-AppxPackage *windowscalculator* | Remove-AppxPackage
# Get-AppxPackage *windowscamera* | Remove-AppxPackage
# Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage
# Get-AppxPackage *officehub* | Remove-AppxPackage
# Get-AppxPackage *getstarted* | Remove-AppxPackage
# Get-AppxPackage *solit* | Remove-AppxPackage
# Get-AppxPackage *skypeapp* | Remove-AppxPackage
# Get-AppxPackage *zunemusic* | Remove-AppxPackage
# Get-AppxPackage *solitairecollection* | Remove-AppxPackage
# Get-AppxPackage *windowsmaps* | Remove-AppxPackage
# Get-AppxPackage *bingfinance* | Remove-AppxPackage
# Get-AppxPackage *zunevideo* | Remove-AppxPackage
# Get-AppxPackage *onenote* | Remove-AppxPackage
# Get-AppxPackage *bingnews* | Remove-AppxPackage
# Get-AppxPackage *people* | Remove-AppxPackage
# Get-AppxPackage *windowsphone* | Remove-AppxPackage
# Get-AppxPackage *photos* | Remove-AppxPackage
# Get-AppxPackage *windowsstore* | Remove-AppxPackage
# Get-AppxPackage *bingsports* | Remove-AppxPackage
# Get-AppxPackage *soundrecorder* | Remove-AppxPackage
# Get-AppxPackage *bingweather* | Remove-AppxPackage
# Get-AppxPackage *xboxapp* | Remove-AppxPackage
$Choice = "*xboxapp*", "*bing*", "*soundrecorder*", "*windowsstore*", "*windowsphone*", "*windows*", "*zunevideo", "*3dbuilder*", "*getstarted*", "*officehub*", "*solitairecollection*", "*solit*"
foreach($selction in $Choice) {
    Get-AppxPackage $selction -allusers | Remove-AppxPackage
    Write-Host "Removed $Selection"
}