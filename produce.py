from app import keywords
import json
from kafka import KafkaProducer
from articles import postNewsAPI
from articles import find_extract
from time import sleep


# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('ascii')
)


extracts_list = []
for t in keywords:
    data = postNewsAPI(t)
    #extracts_list.append(find_extract(t, data))
    my_producer.send(topic=t, value=data)
    print("Message for topic " + t + " has send\n")
    sleep(1)

sleep(1)
#my_producer.send(topic='sources domain name', value=extracts_list)
print("Message for topic sources domain name has send\n")

