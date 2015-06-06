#!/usr/bin/env python

import pika
import sys
import uuid

# Grab command line input for everity and message
a = sys.argv[1] or "1"
b = sys.argv[2] or "2"

class rpcClient(object):
	def __init__(self):
		# Create a connection to RabbitMQ server
		self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		self.channel = self.connection.channel()

		self.response_queue = self.channel.queue_declare(exclusive=True)
		self.channel.basic_consume(self.response_callback, self.response_queue.method.queue)

	def response_callback(self, ch, method, properties, body):
		if self.id == properties.correlation_id:
			self.response_message = body
			print '[x] Recieved response: %r' % (body,)
	
	def call(self, x, y):
		self.response_message = None
		self.id = str(uuid.uuid4())

		# Send a message using the default exchange, make messages persistent
		self.channel.basic_publish(exchange='', routing_key='rpc', body='%s,%s' % (x, y), properties=pika.BasicProperties(delivery_mode=2, reply_to=self.response_queue.method.queue, correlation_id=self.id))
		print '[x] sent %r + %r = ?' % (a, b)

		while self.response_message == None:
			self.connection.process_data_events()
		return self.response_message

rpcc = rpcClient()

response = rpcc.call(a, b)
print '%r + %r = %r' % (a, b, response)
