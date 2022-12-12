from app import keywords
import json
from kafka import KafkaProducer
from articles import postNewsAPI
from articles import find_extract
from time import sleep


# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topics = keywords
topics.append('sources domain name')
extracts_list = []
for t in keywords:
    if t != 'sources domain name':
        data = postNewsAPI(t)
        my_producer.send(topic=t, value=data)
        extracts_list.append(find_extract(t, data))
    else:
        my_producer.send(topic=t, value=extracts_list)
    print("Message for topic " + t + " has send\n")
    # sleep(1)



