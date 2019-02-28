#Check to see if there is an old flash
$flashdir = "$env:userprofile\AppData\Local\Google\Chrome\User Data\PepperFlash\27.0.0.170"
$ChkFile = "$flashdir\pepflashplayer.dll"

$FileExists = Test-Path $ChkFile

$url = "https://kb.vmware.com/selfservice/viewAttachment.do?attachID=2151945_pepflashplayer.7z&documentID=2151945"
$output = ".\pepperflash.7z"


function GetPlace {
	#Downloads the file to the current dir, extracts it, moves the .dll to where it needs to be and removes the archive
	set-alias sz "$env:ProgramFiles\7-Zip\7z.exe"

	Invoke-WebRequest -Uri $url -OutFile $output
	sz x $output -r > log #the '> log' only exsists for silent output of 7zip
	Remove-Item -Path log
	Move-Item -Path ".\pepflashplayer.dll" -Destination "$flashdir"
	Remove-Item -Path ".\pepperflash.7z"
}
function End {

}
If ($FileExists -eq $True) {
    #If there is a file there than it checks the verison number at version 27,0,0,159 is the lastest version to work
	$filevir = [int](Get-Item "$ChkFile").VersionInfo.FileVersion
	If ($filevir -gt 2700159) {
		Write-Host "There is a newer verison that is not compatiable. Getting a compatiable verison"
		Rename-Item $ChkFile pepflashplayer.old #Creates a backup of the flash that is there
		GetPlace
	}
	Else {
		Write-Host "There is already a compatiable version of Flash"
	}}


Else {
GetPlace
}

Read-Host -Prompt "By: Jacob White '20 `nPress Enter to exit"