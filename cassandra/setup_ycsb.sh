cqlsh -e "create keyspace ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1 };"
cqlsh -k ycsb -e "create table usertable (y_id varchar primary key, field0 varchar, field1 varchar, field2 varchar);"
