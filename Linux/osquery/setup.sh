#!/bin/bash
curl -L https://pkg.osquery.io/rpm/GPG -o /etc/pki/rpm-gpg/RPM-GPG-KEY-osquery
yum install -y yum-utils
yum-config-manager --add-repo https://pkg.osquery.io/rpm/osquery-s3-rpm.repo
yum-config-manager --enable osquery-s3-rpm
yum install -y osquery
curl https://gitlab.com/jwhite1st/Scripts/raw/master/Linux/osquery/fleetconnect.service -o /etc/systemd/system/fleetconnect.service

systemctl daemon-reload
systemctl start fleetconnect.service
systemctl enable fleetconnect.service