import pika
import time
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare('logs',exchange_type='fanout')

result=channel.queue_declare('',exclusive=True)
queue_name=result.method.queue

channel.queue_bind(queue=queue_name,exchange='logs')

def callback(ch,method,properties,body):
    print(str(time.localtime()))
    print(body)
    
channel.basic_consume(queue_name,on_message_callback=callback,auto_ack=True)

channel.start_consuming()