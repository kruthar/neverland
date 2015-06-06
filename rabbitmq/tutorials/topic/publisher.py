#!/usr/bin/env python

import pika
import sys

# Grab command line input for everity and message
routing = sys.argv[1] or "anonymous.info"
message = ' '.join(sys.argv[2:]) or "Hello World!"

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create our exchange
channel.exchange_declare(exchange='topic', exchange_type='topic')

# Send a message using the default exchange, make messages persistent
channel.basic_publish(exchange='topic', routing_key=routing, body=message, properties=pika.BasicProperties(delivery_mode=2))
print '[x] sent %r: %r' % (routing,message)

connection.close()

