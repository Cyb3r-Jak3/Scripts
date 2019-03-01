#!/bin/bash

useradd -G wheel j

##Setting IP
echo "IPADDR=172.16.150.7" >> /etc/sysconfig/network-scripts/ifcfg-ens192
echo "PREFIX=29" >> /etc/sysconfig/network-scripts/ifcfg-ens192
echo "GATEWAY=172.16.150.2" >> /etc/sysconfig/network-scripts/ifcfg-ens192
echo "DNS1=172.16.150.2" >> /etc/sysconfig/network-scripts/ifcfg-ens192
systemctl restart network.service

## Adding Firewall port 514 for syslog
firewall-cmd --add-port 514/udp --permanent
firewall-cmd --reload

## Setting up logging


cat /etc/rsyslog.d/03-sec350.conf << EOF
module(load="imudp")
input(type="imudp" port="514" ruleset="RemoteDevice")
template(name="DynFile" type="string"
    string="/var/log/remote-syslog/%HOSTNAME%/%$YEAR%.%$MONTH%.%$DAY%.%PROGRAMNAME%.log"
)
ruleset(name="RemoteDevice"){
    action(type="omfile" dynaFile="DynFile")
}
EOF


echo "Remember to set a password for j"
