vagrant up
vagrant ssh -c "/opt/couchbase/bin/couchbase-cli cluster-init -c 127.0.0.1:8091 --cluster-init-username=couchbase --cluster-init-password=couchbase --cluster-init-port=8091 --cluster-init-ramsize=796 --services=data" couchbase.vagrant
vagrant ssh -c "/opt/couchbase/bin/couchbase-cli server-add -c 127.0.0.1:8091 -u couchbase -p couchbase --server-add=query.couchbase.vagrant:8091 --server-add-username=couchbase --server-add-password=couchbase --services=query" couchbase.vagrant
vagrant ssh -c "/opt/couchbase/bin/couchbase-cli server-add -c 127.0.0.1:8091 -u couchbase -p couchbase --server-add=index.couchbase.vagrant:8091 --server-add-username=couchbase --server-add-password=couchbase --services=index" couchbase.vagrant
vagrant ssh -c "/opt/couchbase/bin/couchbase-cli rebalance -c 127.0.0.1:8091 -u couchbase -p couchbase" couchbase.vagrant
