#!/usr/bin/env python

import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Get the severity to bind to from command line input
routing = sys.argv[1]

# Ensure that the queue exists
queue = channel.queue_declare(exclusive=True)

# Ensure that the exchange exists 
channel.exchange_declare(exchange='topic', exchange_type='topic')

# Bind our temp queue to the exchange
channel.queue_bind(exchange='topic', queue=queue.method.queue, routing_key=routing)

# Define our callback to handle messages
def callback(ch, method, properties, body):
	print '[x] Received %r: %r' % (routing,body)
	time.sleep(body.count('.'))
	print '[x] Done Working'

# Setup a consumer with our callback on the queue
channel.basic_consume(callback, queue=queue.method.queue, no_ack=True)

# Wait for messages to consume
print '[*] Waiting for messages.'
channel.start_consuming()
