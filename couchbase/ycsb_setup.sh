/opt/couchbase/bin/couchbase-cli bucket-create -c 127.0.0.1:8091 -u couchbase -p couchbase --bucket=usertable --bucket-type=couchbase --bucket-ramsize=512 --bucket-replica=0

curl -XPUT http://localhost:8092/usertable/_design/ycsb_ddoc -H 'Content-Type: application/json' -d @ycsb_ddoc.json 
