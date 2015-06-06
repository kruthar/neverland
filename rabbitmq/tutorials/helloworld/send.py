#!/usr/bin/env python

import pika

# Create a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create our queue
channel.queue_declare(queue='hello')

# Send a message using the default exchange
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print '[x] sent "Hello World!"'

connection.close()

