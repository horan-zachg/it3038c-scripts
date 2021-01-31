#$Hello = "Hello, Powershell!"
#Write-host($Hello)
function getIP{
    (Get-NetIPAddress).IPv4address | select-string "192*"
}
#$credential = Get-Credential
$IP = getIP
$DATE = Get-Date -Format "dddd MMMM/dd/yyyy"
$HOSTNAME = hostname
$version = $PSVersionTable.PSVersion | Sort-Object major | foreach-object {$_.major}
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $HOSTNAME. Powershell Version $version. Today's date is $DATE."
write-host($body)
#Send-MailMessage -From "zachglosson@gmail.com" -To "glossozj@mail.uc.edu" -Subject "IT3038C Windows Sysinfo" -Body $Body -SmtpServer "smtp.google.com" -port 587 -UseSSL -Credential $credential