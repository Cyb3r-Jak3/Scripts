#!/bin/bash
yum install -y wget unzip

#Gets and copies the fleet binary
wget https://github.com/kolide/fleet/releases/latest/download/fleet.zip
unzip fleet.zip 'linux/*' -d fleet
cp fleet/linux/fleet* /usr/bin/

# Gets an installs mysql
wget https://repo.mysql.com/mysql57-community-release-el7.rpm
rpm -i mysql57-community-release-el7.rpm
yum update -y
yum install -y mysql-server
systemctl start mysqld
#Sets up mysql
password_match=`awk '/A temporary password is generated for/ {a=$0} END{ print a }' /var/log/mysqld.log | awk '{print $(NF)}'`
mysql -u root -p$password_match "ALTER USER 'root'@'localhost' IDENTIFIED BY '$password_match';"
mysql -u root -p$password_match "flush privileges;"
mysql -u root -p$password_match "CREATE DATABASE kolide;"

#Installs redis
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
yum install -y redis
systemctl enable redis
systemctl start redis

#Prepares the database
/usr/bin/fleet prepare db --mysql_address=127.0.0.1:3306 --mysql_database=kolide --mysql_username=root --mysql_password=$password_match

# Generates certificates
openssl genrsa -out /tmp/server.key 4096
openssl req -new -key /tmp/server.key -out /tmp/server.csr
openssl x509 -req -days 366 -in /tmp/server.csr -signkey /tmp/server.key -out /tmp/server.cert

# Generates random string for auth_jwt_key
$random_string=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 20)
#Gets Fleet service file
curl https://gitlab.com/jwhite1st/Scripts/raw/master/Linux/fleet/fleet.service -o /etc/systemd/system/fleet.service

#Changes the BAD string the the randomstring
sed -i -e "s/BADSTRING\b/$random_string/g" /etc/systemd/system/fleet.service

#Changes database password
sed -i -e "s/toor\b/$password_match/g" /etc/systemd/system/fleet.service

#Starts and enables fleet
systemctl daemon-reload
systemctl start fleet.service
systemctl enable fleet.service