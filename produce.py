from app import keywords
from json import dumps
from kafka import KafkaProducer
from articles import  postNewsAPI
from time import sleep

# initializing the Kafka producer
my_producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

"""
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092"
)

topic_list = []

for k in keywords:
    for t in admin_client.list_topics():
        if (k != t):
            topic_list.append(NewTopic(name=k, num_partitions=1, replication_factor=1))


admin_client.create_topics(new_topics=topic_list, validate_only=False)


for t in admin_client.list_topics():
    data = postNewsAPI(t)
    my_producer.send(topic = t, value=data)
    sleep(5)
"""
for t in keywords:
    data = postNewsAPI(t)
    my_producer.send(topic = t, value=data)
    sleep(5)
