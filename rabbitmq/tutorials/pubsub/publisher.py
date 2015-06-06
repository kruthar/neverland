#!/usr/bin/env python

import pika
import sys

# Grab command line input for message
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create our exchange
channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

# Send a message using the default exchange, make messages persistent
channel.basic_publish(exchange='pubsub', routing_key='', body=message, properties=pika.BasicProperties(delivery_mode=2))
print '[x] sent %r' % (message,)

connection.close()

