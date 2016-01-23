echo 'create database if not exists ycsb;' | mysql -h localhost -u admin -padmin
echo 'drop table if exists usertable;' | mysql -h localhost -u admin -padmin ycsb
echo 'create table if not exists usertable (
	YCSB_KEY varchar(100) primary key,
	FIELD0 varchar(100),
	FIELD1 varchar(100),
	FIELD2 varchar(100)
);' | mysql -h localhost -u admin -padmin ycsb
