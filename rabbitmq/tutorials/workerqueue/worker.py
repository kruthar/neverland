#!/usr/bin/env python

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure that the worker queue exists
channel.queue_declare(queue='worker', durable=True)

# Define our callback to handle messages
def callback(ch, method, properties, body):
	print '[x] Received %r' % (body,)
	time.sleep(body.count('.'))
	print '[x] Done Working'
	ch.basic_ack(delivery_tag=method.delivery_tag)

# Setup a consumer with our callback on the worker queue
channel.basic_consume(callback, queue='worker')

# Wait for messages to consume
print '[*] Waiting for messages.'
channel.start_consuming()
