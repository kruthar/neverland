# LAMP Server

LAMP = Linux, Apache, MySQL, PHP - this env is just a combo of the apachephp env and mysql to provide a full functional LAMP server.

Links
-----
* http://httpd.apache.org/
* http://php.net/
* https://www.mysql.com/

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
2. In a browser you should be able to visit the ap at http://lamp.vagrant/[APP]
3. Connect to mysql via command line or application with admin:admin@localhost
