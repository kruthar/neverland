#!/usr/bin/env python

import pika
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure that the queue exists
channel.queue_declare(queue='rpc', durable=True)

# Define our callback to handle messages
def callback(ch, method, properties, body):
	print '[x] Received %r' % (body)
	nums = body.split(',')
	sum = int(nums[0]) + int(nums[1])
	print '[x] Response sent: %r + %r = %r' % (nums[0], nums[1], str(sum))
	channel.basic_publish(exchange='', routing_key=properties.reply_to, body=str(sum), properties=pika.BasicProperties(delivery_mode=2,correlation_id=properties.correlation_id))
	ch.basic_ack(delivery_tag=method.delivery_tag)

# Setup a consumer with our callback on the queue
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='rpc')

# Wait for messages to consume
print '[*] Waiting for messages.'
channel.start_consuming()
