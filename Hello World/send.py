# -*- coding: utf-8 -*-
import pika

#establishing a connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#creating a queue
channel.queue_declare(queue="hello")

#publishing message
channel.basic_publish(exchange="",routing_key="hello",body="Hello RabbitMQ")
print("Sent Hello to RabbitMQ")

connection.close()
