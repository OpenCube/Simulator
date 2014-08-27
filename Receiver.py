import pika

#Get connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='ISS_Position')

#Display initial message
print ' [*] Waiting for messages. To exit press CTRL+C'

#Define action when a message is received
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

#Define action
channel.basic_consume(callback,
                      queue='ISS_Position',
                      no_ack=True)
#Start receiving
channel.start_consuming()
