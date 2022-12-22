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

topics = keywords
#topics.append('sources_domain_name')
print(topics)
extracts_list = []
for t in keywords:
    data = postNewsAPI(t)
    #json_object = json.dumps(data)
    my_producer.send(topic=t, value={t: data})
    #extracts_list.append(find_extract(t, data))
    #print(extracts_list)
    print("Message for topic " + t + " has send\n")
    sleep(1)


#json_object = json.dumps(extracts_list)
#print(extracts_list)
#my_producer.send(topic='sources_domain_name', value=json_object)
#print("Message for topic " + t + " has send\n")



