# RabbitMQ

RabbitMQ is a message queue framework that allows for setting up a lot of different messaging scenarios like:

* distributed tasks - send tasks into a cluster of workersthat will balance the workload across multiple nodes
* publish/subscribe - publish to a queue and disperse messages to multiple subscribers
* filtered messaging - using routing information to filter which subscribers receive which messages.
* rpc - create an rpc server that will accept requests and send a response

Links
-----
* https://www.rabbitmq.com/

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
    
Running RabbitMQ
----------------
1. Log in to the VM with:

	```sh
	vagrant ssh
	```

2. Start/Stop the RabbitMQ Server with:
	
	```sh
	sudo service rabbitmq-server [start|stop]

3. There are six tutorial programs in the tutorials folder, you can follow the same tutorials at https://www.rabbitmq.com/getstarted.html