sudo rm -rf /opt/ycsb-0.5.0-SNAPSHOT*
sudo tar -xvf /vagrant/deps/ycsb-0.5.0-SNAPSHOT.tar.gz -C /opt/
mysql -h 192.168.56.32 -u admin -padmin ycsb < mysql/configure_mysql.sql
