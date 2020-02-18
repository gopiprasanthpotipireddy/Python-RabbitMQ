import pika
import sys
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.queue_declare('workqueue')

msg=''.join(sys.argv[1:])
channel.basic_publish(exchange='',routing_key='workqueue',body=msg)

connection.close()