from app import keywords
import json
from kafka import KafkaProducer
from articles import postNewsAPI
from time import sleep


# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('ascii')
)

for t in keywords:
    data = postNewsAPI(t)
    my_producer.send(topic=t, value=data)
    print("Message for topic " + t + " has send\n")
    sleep(1)
