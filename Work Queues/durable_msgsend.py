import pika
import sys
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.queue_declare('taskqueue',durable=True)

msg=''.join(sys.argv[1:])
channel.basic_publish(exchange='',routing_key='taskqueue',body=msg,properties=pika.BasicProperties(delivery_mode=2))

connection.close()