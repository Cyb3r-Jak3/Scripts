#!/bin/vbash
source /opt/vyatta/etc/functions/script-template

if [ "$(id -g -n)" != 'vyattacfg' ] ; then
    exec sg vyattacfg -c "/bin/vbash $(readlink -f $0) $@"
fi

configure
## Setting up interfaces
set system host-name fw1-jake
set system gateway-address 10.0.17.2
set system name-server 10.0.17.2
set interfaces ethernet eth0 description SEC350-WAN
set interfaces ethernet eth1 description DMZ
set interfaces ethernet eth2 description LAN
delete interfaces ethernet eth0 address dhcp
set interfaces ethernet eth0 address 10.0.17.125/24
set interfaces ethernet eth1 address 172.16.50.2/24
set interfaces ethernet eth2 address 172.16.150.2/24
commit
save
## Settings firewalls and zones
set zone-policy zone WAN interface eth0
set zone-policy zone DMZ interface eth1
set zone-policy zone LAN interface eth2
for x in "WAN-to-DMZ" "DMZ-to-WAN" "WAN-to-LAN" "LAN-to-WAN" "DMZ-to-LAN" "LAN-to-DMZ"
do
set firewall name $x default-action drop
set firewall name $x enable-default-log
done
commit
save
## Settings interzone firewalls
set zone-policy zone DMZ from WAN firewall name WAN-to-DMZ
set zone-policy zone DMZ from LAN firewall name LAN-to-DMZ
set zone-policy zone WAN from DMZ firewall name DMZ-to-WAN
set zone-policy zone WAN from LAN firewall name LAN-to-WAN
set zone-policy zone LAN from DMZ firewall name DMZ-to-LAN
set zone-policy zone LAN from WAN firewall name WAN-to-LAN
commit
save
## Set connection establied
for zone in "DMZ-to-WAN" "DMZ-to-LAN" "WAN-to-LAN"
do
  for i in "action accept" "state establisted enable"
  do
  set firewall name $zone rule 1 $i
  done
done

## LAN to Web01
for i in "action accept" "destination address 172.16.50.3" "destitnation port 80" "protocol tcp" "description 'Allow LAN access to WEB01'"
do
set firewall name LAN-to-DMZ rule 10 $i
done

## Logs to syslog01
for i in "action accept" "destination address 172.16.150.7" "destitnation port 514" "protocol tcp_udp" "description 'Log from DMZ to syslog01"
do
set firewall name DMZ-to-LAN rule 10 $i
done

## WAN to web01
for i in "description 'Port Forwarding HTTP WAN to Web01'" "destination port 80" "inbound-interface eth0" "protocol tcp" "translation address 172.16.50.3"
do
set nat destination rule 10 $i
done

##Nat Masquerade
for i in "description 'NAT FROM LAN to WAN'" "outbound-interface eth0" "source address 172.16.150.0/24" "translation address masquerade"
do
set nat source rule 10 $i
done
commit
save
