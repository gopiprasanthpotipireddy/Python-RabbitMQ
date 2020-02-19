import pika
import sys
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare('topic_logs',exchange_type='topic')

msg="Exception in Thread"
severity=sys.argv[1]
channel.basic_publish(exchange='topic_logs',routing_key=severity,body=msg)

connection.close()

