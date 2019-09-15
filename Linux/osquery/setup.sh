#!/bin/bash
curl -L https://pkg.osquery.io/rpm/GPG -o /etc/pki/rpm-gpg/RPM-GPG-KEY-osquery
yum install -y yum-utils
yum-config-manager --add-repo https://pkg.osquery.io/rpm/osquery-s3-rpm.repo
yum-config-manager --enable osquery-s3-rpm
yum install -y osquery
curl https://gitlab.com/jwhite1st/Scripts/raw/master/Linux/osquery/fleetconnect.service -o /etc/systemd/system/fleetconnect.service
read -p "Please enter the hostname/ip of your fleet server. (Include port): " server 
openssl s_client -showcerts -connect $server </dev/null 2>/dev/null|openssl x509 -outform PEM > /var/osquery/server.pem
sed -i -e "s/oldip\b/$server/g" /etc/systemd/system/fleetconnect.service
systemctl daemon-reload
systemctl start fleetconnect.service
systemctl enable fleetconnect.service