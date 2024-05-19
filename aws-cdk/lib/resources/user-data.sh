#!/bin/bash

yum update -y
yum install -y httpd

systemctl enable httpd.service
systemctl start httpd.service

usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 2775 {} \; # 0664

# cp -r /tmp/html/* /var/www/html/

echo " <h1>Welcome to my webpage! This is Yuki Mabuchi</h1> " > /var/www/html/index.html