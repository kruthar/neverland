second star on the right and straight on til' morning...

A place for my introductory and test environments in Vagrant with Ansible.

General Prerequisites
---------------------
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

Environments
------------

## Apache & PHP
A general purpose Apache webserver with PHP installed: https://github.com/kruthar/neverland/tree/master/apachephp

## Cassandra
A single node instance of Datastax Distro Cassandra: https://github.com/kruthar/neverland/tree/master/cassandra

## Couchbase
A single node Couchbase 4 server with data, index, and query services installed: https://github.com/kruthar/neverland/tree/master/couchbase

## RabbitMQ
under construction
