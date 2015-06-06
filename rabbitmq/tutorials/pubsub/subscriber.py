#!/usr/bin/env python

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure that the queue exists
queue = channel.queue_declare(exclusive=True)

# Ensure that the exchange exists 
channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

# Bind our temp queue to the exchange
channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

# Define our callback to handle messages
def callback(ch, method, properties, body):
	print '[x] Received %r' % (body,)
	time.sleep(body.count('.'))
	print '[x] Done Working'

# Setup a consumer with our callback on the queue
channel.basic_consume(callback, queue=queue.method.queue, no_ack=True)

# Wait for messages to consume
print '[*] Waiting for messages.'
channel.start_consuming()
