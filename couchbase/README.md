# Couchbase 4.0.0 - 3 node cluster

Couchbase is a distributed, key-value, document store. It provides a fast a reliable way to store NoSQL content, usually in JSON format (supports other types like serialized POJO's, etc.). At the time of creation this env is using 4.0.0 which added a lot of new features like GA N1QL, as well as a lot of architectural changes around MDS (Multi-Dimensional Scaling), a way to specify which machines of the cluster are running which services to better improve performance and scaling potential.

This env is a single machine install with all services on a single machine.

Links
-----
* https://www.couchbase.com/

Couchbase Interface Locations
----------------
1. Couchbase UI console: 
	
	http://couchbase.vagrant:8091

2. Couchbase Query (cbq) interface:

	```sh
	vagrant ssh
	/opt/couchbase/bin/cbq
	cbq> select * from default limit 5;
	```
	
	cbq is a query interface to send SQL-like queries to N1QL ex. 
