import pika
import time
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.queue_declare('workqueue')

def callback(ch,method,properties,body):
    print("Job %r"%body)
    time.sleep(body.count(b'.'))
    print('Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='workqueue',on_message_callback=callback)
channel.start_consuming()
