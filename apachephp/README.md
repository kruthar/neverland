# Apache Web Server

Apache is a commonly used web server to serve we applications to clients. This VM also comes with PHP installed so you can run things like Wordpress.

Links
-----
* http://httpd.apache.org/
* http://php.net/

Prerequisites
-------------
1. Install Virtualbox: https://www.virtualbox.org/wiki/Downloads

2. Install Vagrant: http://www.vagrantup.com/downloads.html

3. Install necessary Vagrant plugins:
    
    ```sh
    vagrant plugin install vagrant-hostmanager
    vagrant plugin install vagrant-cachier
    ```

4. Install Ansible

    ```sh
    brew install ansible
    ```
    
Using the Server
----------------
1. Place your web application inside of /var/www/html
2. In a browser you should be able to visit the ap at http://apache.vagrant/[APP]
