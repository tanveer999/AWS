#!/bin/bash
apt update
apt install nginx -y
systemctl start nginx
systemctl enable nginx
echo -e "<html>\n\t<h1>Hello $(hostname -f)</h1>\n</html>" > /var/www/html/index.html