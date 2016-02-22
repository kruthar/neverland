create database if not exists ycsb;
use ycsb;
drop table if exists usertable;
create table if not exists usertable (
	YCSB_KEY varchar(100) primary key,
	FIELD0 varchar(100),
	FIELD1 varchar(100),
	FIELD2 varchar(100)
);
