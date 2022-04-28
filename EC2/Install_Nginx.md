# Requirement
1. AWS account access
2. Running EC2 instance
3. SSH access to EC2 instance

# Installing NGINX

Step 1:

Make a ssh connection to your instance

Step 2:

Update apt by running the following command

```
sudo apt update
```

Step 3:

Now install NGINX with the following command
```
sudo apt install nginx -y
```

Step 4:

After installation, start the nginx service with the following command
```
sudo systemctl start nginx
```

Step 5:
To start nginx at boot, run the following command
```
sudo systemctl enable nginx
```


# Hosting a simple HTML file

Step 1:

Create a simple html file named index.html

```
echo -e "<html>\n\t<h1>Hello World</h1>\n</html>" > index.html
```

Step 2:

Move index.html to /var/www/html directory
```
sudo mv index.html /var/www/html/index.html
```