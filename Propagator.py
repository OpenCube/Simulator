from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
import urllib2
from datetime import datetime
import time
import pika

#Get connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='ISS_Position')

#Get the most recent ISS TLE
response = urllib2.urlopen('http://www.celestrak.com/NORAD/elements/stations.txt')
TLEs = response.read().splitlines()
response.close()
ISS_TLE = TLEs[0:3]

#Load satellite
satellite = twoline2rv(ISS_TLE[1], ISS_TLE[2], wgs72)

while True:
	#Get current time
	now = datetime.now()
	#Compute position and velocity
	position, velocity = satellite.propagate(now.year, now.month, now.day, now.hour, now.minute, now.second)
	time.sleep(1)
	#Publish ISS position
	channel.basic_publish(exchange='',
                      routing_key='ISS_Position',
                      body=str(position))
	#Print results
	print(position)
	print(velocity)

#Close connection
connection.close()

