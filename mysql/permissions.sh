mysql -u root -e "create user 'admin'@'localhost' identified by 'admin';"
mysql -u root -e "grant all privileges on *.* to 'admin'@'localhost' with grant option;"
mysql -u root -e "create user 'admin'@'%' identified by 'admin';"
mysql -u root -e "grant all privileges on *.* to 'admin'@'%' with grant option;"
