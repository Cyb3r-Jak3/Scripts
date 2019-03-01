$address = Read-Host -Prompt ("Which address?")
New-NetIPAddress -interfaceAlias "Ethernet0" -IPAdress 172.16.150.$address -PrefixLength 24 -DefaultGateway 172.16.150.2
Set-DNSClientServerAddress -interfaceAlias "Ethernet0" -ServerAddresses 172.16.150.2

