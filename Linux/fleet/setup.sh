#!/bin/bash
yum install -y wget unzip > /dev/null

#Gets and copies the fleet binary
wget https://github.com/kolide/fleet/releases/latest/download/fleet.zip 
unzip fleet.zip 'linux/*' -d fleet > /dev/null
cp fleet/linux/fleet* /usr/bin/ > /dev/null

# Gets an installs mysql
wget https://repo.mysql.com/mysql57-community-release-el7.rpm 
rpm -i mysql57-community-release-el7.rpm > /dev/null
yum update -y > /dev/null
yum install -y mysql-server > /dev/null
systemctl start mysqld 
random_password=$(strings -n 1 < /dev/urandom | tr -d '[:space:] &' | head -c30)
echo "$random_password"
#Sets up mysql
temp_pass=`awk '/A temporary password is generated for/ {a=$0} END{ print a }' /var/log/mysqld.log | awk '{print $(NF)}'`
echo "$temp_pass"
mysqladmin -u root --password=${temp_pass} password $random_password
#echo "ALTER USER 'root'@'localhost' IDENTIFIED BY '$random_password';" | mysql -u root -p$password_match  --connect-expired-password
#echo "flush privileges;" | mysql -u root -p$random_password
echo "CREATE DATABASE kolide;" | mysql -u root -p$random_password

#Installs redis
rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm > /dev/null
yum install -y redis > /dev/null
systemctl enable redis
systemctl start redis

#Prepares the database
/usr/bin/fleet prepare db --mysql_address=127.0.0.1:3306 --mysql_database=kolide --mysql_username=root --mysql_password=$random_password

# Generates certificates
openssl genrsa -out /tmp/server.key 4096
openssl req -new -key /tmp/server.key -out /tmp/server.csr
openssl x509 -req -days 366 -in /tmp/server.csr -signkey /tmp/server.key -out /tmp/server.cert

# Generates random string for auth_jwt_key
random_string=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 20)
#Gets Fleet service file
curl https://gitlab.com/jwhite1st/Scripts/raw/master/Linux/fleet/fleet.service -o /etc/systemd/system/fleet.service

#Changes the BAD string the the randomstring
sed -i -e "s/BADSTRING\b/$random_string/g" /etc/systemd/system/fleet.service

#Changes database password
sed -i -e "s/toor\b/$random_password/g" /etc/systemd/system/fleet.service

#Starts and enables fleet
systemctl daemon-reload
systemctl start fleet.service
systemctl enable fleet.service