#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure that the hello queue exists
channel.queue_declare(queue='hello')

# Define our callback to handle messages
def callback(ch, method, properties, body):
	print '[x] Received %r' % (body,)

# Setup a consumer with our callback on the hello queue
channel.basic_consume(callback, queue='hello', no_ack=True)

# Wait for messages to consume
print '[*] Waiting for messages.'
channel.start_consuming()
