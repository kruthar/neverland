This is a list of hostname to IP mappings to keep things straight.
Try to always use these mappings even outside of this repo, the 
vagrant-cachier manager does not do a complete enough job removing
local hosts file additions. That problem can be mitigated if like
hostnames always map to the same IP address, even across projects.

Also try to confirm to these loose categories if possible.

# Clients
www.patheos.com		192.168.56.10

# Data Movement
nifi.vagrant		192.168.56.20
rabbit.vagrant		192.168.56.21

# Web
lamp.vagrant		192.168.56.30
apache.vagrant		192.168.56.31
mysql.vagrant		192.168.56.32
postgres.vagrant	192.168.56.33

# NoSQL
couchbase.vagrant	192.168.56.40
cassandra.vagrant	192.168.56.41
memcached.vagrant	192.168.56.42
mongodb.vagrant		192.168.56.43
orientdb.vagrant	192.168.56.44
redis.vagrant		192.168.56.45

# Search
solr.vagrant		192.168.56.50
fusion.vagrant		192.168.56.51

# Big Data
spark.vagrant		192.168.56.60

# DevOps
docs.oneops.vagrant	192.168.56.70
