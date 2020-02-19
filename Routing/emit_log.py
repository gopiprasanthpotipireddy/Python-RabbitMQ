import pika
import sys
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare('direct_logs',exchange_type='direct')

msg="Exception in Thread"
severity=sys.argv[1]
channel.basic_publish(exchange='direct_logs',routing_key=severity,body=msg)

connection.close()

