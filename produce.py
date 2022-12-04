from json import dumps
from kafka import KafkaProducer
from articles import  postNewsAPI
from time import sleep

keywords = ['bitcoin', 'tesla']

# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

"""
for k in keywords:
    postNewsAPI(k)
    my_producer.send(k, value = k)
    sleep(10)
"""
for n in range(500):
    my_data = {'num':n}
    my_producer.send('testnum', value = my_data)
    sleep(5)