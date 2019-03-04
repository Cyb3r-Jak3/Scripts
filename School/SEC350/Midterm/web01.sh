#!/bin/bash

useradd -G wheel j

##Setting IP
echo "IPADDR=172.16.50.3" >> /etc/sysconfig/network-scripts/ifcfg-ens192
echo "PREFIX=29" >> /etc/sysconfig/network-scripts/ifcfg-ens192
echo "GATEWAY=172.16.50.2" >> /etc/sysconfig/network-scripts/ifcfg-ens192
echo "DNS1=172.16.50.2" >> /etc/sysconfig/network-scripts/ifcfg-ens192
systemctl restart network.service

## Adding Firewall port 80 for http
firewall-cmd --add-port 80/tcp --permanent
firewall-cmd --reload

## Setting up logging
echo user.notice @172.16.150.7 > /etc/rsyslog.d/sec350.sec
echo user.authpriv* @172.16.150.7 >> /etc/syslog.d/sec350.sec
systemctl restart rsyslog


##Editing index.html
rm -f /var/www/html/index.html
cat /var/www/html/index.html <<EOF
<pre>
_________                    __________________ _______                    _______  ______   _______  __   
\__    _/  |\     /||\     /|\__   __/\__   __/(  ____ \         |\     /|(  ____ \(  ___ \ (  __   )/  \  
   )  (    | )   ( || )   ( |   ) (      ) (   | (    \/         | )   ( || (    \/| (   ) )| (  )  |\/) ) 
   |  |    | | _ | || (___) |   | |      | |   | (__       _____ | | _ | || (__    | (__/ / | | /   |  | | 
   |  |    | |( )| ||  ___  |   | |      | |   |  __)     (_____)| |( )| ||  __)   |  __ (  | (/ /) |  | | 
   |  |    | || || || (   ) |   | |      | |   | (               | || || || (      | (  \ \ |   / | |  | | 
|\_)  )    | () () || )   ( |___) (___   | |   | (____/\         | () () || (____/\| )___) )|  (__) |__) (_
(____/     (_______)|/     \|\_______/   )_(   (_______/         (_______)(_______/|/ \___/ (_______)\____/
</pre> 
EOF

##Wrap up

echo "Remember to set a password for j"
