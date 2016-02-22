create keyspace ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1 };
use ycsb;
create table usertable (y_id varchar primary key, field0 varchar, field1 varchar, field2 varchar);
