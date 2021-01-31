#$Hello = "Hello, Powershell!"
#Write-host($Hello)
function getIP{
    (Get-NetIPAddress).IPv4address | select-string "192*"
}
$IP = getIP
write-host("This machine's IP is {0}" -f $IP)
write-host("User is $env:username")
$HOSTNAME = hostname
write-host("Hostname is $HOSTNAME")
$version = $PSVersionTable.PSVersion | Sort-Object major | foreach-object {$_.major}
write-host("Powershell Version $version")
$DATE = Get-Date -Format "dddd MMMM/dd/yyyy"
write-host("Today's date is $DATE")