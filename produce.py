from app import keywords
import json
from kafka import KafkaProducer
from articles import postNewsAPI
from articles import find_extract
from articles import names
from time import sleep



# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('ascii')
)

topics = keywords
topics.append('sources_domain_name')
print(topics)
extracts_list = {}

for t in topics:
    if t not in 'sources_domain_name':
        data = postNewsAPI(t)
        sources_names = names(t, data)
        if t not in extracts_list.keys():
            for s in sources_names:
                extract = find_extract(s)
                extracts_list[s] = extract
        my_producer.send(topic=t, value={t: data})
        print("Message for topic " + t + " has send\n")
        sleep(1)
    else:
        print(extracts_list.keys())
        my_producer.send(topic=t, value=json.dumps(extracts_list))
        print("Message for topic " + t + " has send\n")






