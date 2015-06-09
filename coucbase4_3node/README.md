# Couchbase 4.0.0 - 3 node cluster

Couchbase is a distributed, key-value, document store. It provides a fast a reliable way to store NoSQL content, usually in JSON format (supports other types like serialized POJO's, etc.). At the time of creation this env is using 4.0.0-beta which added a lot of new features like GA N1QL, as well as a lot of architectural changes around MDS (Multi-Dimensional Scaling), a way to specify which machines of the cluster are running which services to better improve performance and scaling potential.

This env is simply a multi-machine vagrant boot with 3 machines, one each for the data, query and index services.

Links
-----
* https://www.couchbase.com/

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
    
Booting the Cluster
-------------------
This environment takes a little cross machine coordination to setup so you must run a bash script instead of doing the usual vagrant up:

```sh
./initialize_couchbase_cluster.sh
```
    
Couchbase Interface Locations
----------------
1. Couchbase UI console: 
	
	http://couchbase.vagrant:8091

2. Couchbase Query (cbq) interface:

	```sh
	vagrant ssh query.couchbase.vagrant
	/opt/couchbase/bin/cbq
	cbq> select * from default limit 5;
	```
	
	cbq is a query interface to send SQL-like queries to N1QL ex. 