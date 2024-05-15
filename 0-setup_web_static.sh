#!/usr/bin/env bash
#Bash script that sets up your web servers

#install nginx
sudo apt-get update -y > /dev/null 2>&1
sudo apt-get install nginx -y > /dev/null 2>&1

#create folders and file
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "hello mom" > /data/web_static/releases/test/index.html

#Create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current;

# Give ownership to the ubuntu user AND group
chown -R ubuntu:ubuntu /data/;

# Update the Nginx configuration
sed -i '/^\tserver_name.*/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default;

# restart nginx
sudo service nginx restart > /dev/null 2>&1
