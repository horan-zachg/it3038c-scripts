##manually set the location to a location on your computer that you want the log file to go to.
$Location = "R:\Log"
$Desktop = Get-CimInstance -ClassName Win32_Desktop
$BIOS = Get-CimInstance -ClassName Win32_BIOS
$Processor = Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property SystemType
$OS = Get-CimInstance -ClassName Win32_ComputerSystem| Select-Object -Property BuildNumber, OSType
$USER = Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -Property Status,Name

$info = "$($Location)\Information.log"
New-Item $info -ItemType File -Value "~~~~~~~~~~~~~~~~~Desktop Information~~~~~~~~~~~~~~~~~"
Add-Content $info "~~~~~~~~~~~~~~~~~Desktop info~~~~~~~~~~~~~~~~~"
Add-Content $info $Desktop

Add-Content $info "~~~~~~~~~~~~~~~~~BIOS info~~~~~~~~~~~~~~~~~"
Add-Content $info $BIOS

Add-Content $info "~~~~~~~~~~~~~~~~~Processor info~~~~~~~~~~~~~~~~~"
Add-Content $info $Processor

Add-Content $info "~~~~~~~~~~~~~~~~~Operating System info~~~~~~~~~~~~~~~~~"
Add-Content $info $OS

Add-Content $info "~~~~~~~~~~~~~~~~~User info~~~~~~~~~~~~~~~~~"
Add-Content $info $USER

##I decided to go with learning how to create a script that outputs a log to run on remote machines that uses active directory
##This script can be used on remote machines to find info that is put into a log that can then be used for another script.