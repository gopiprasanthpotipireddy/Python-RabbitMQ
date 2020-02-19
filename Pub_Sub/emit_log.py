import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare('logs',exchange_type='fanout')

msg="Exception in Thread"
channel.basic_publish(exchange='logs',routing_key='',body=msg)

connection.close()