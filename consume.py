import json
from kafka import KafkaConsumer
import pymongo
from app import keywords

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

# generating the Kafka Consumer
topics = keywords
topics.append('sources_domain_name')
print(topics)
my_consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=['localhost : 9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

my_consumer.subscribe(topics=topics)

for message in my_consumer:
        if message.topic != 'sources_domain_name':
                print("Consumer reads message from topic " + message.topic)
                if message.topic in mydb.list_collection_names():
                        print("Topic " + message.topic + ' already exist in database as collection\n')
                else:
                        col = mydb[message.topic]
                        col.insert_one(message.value)
                        print("Topic " + message.topic + " insert to collection " + col.name + "\n")
        else:
                col = mydb[message.topic]
                print("Consumer reads message from topic " + message.topic)
                col.insert_one(message.value)
                print("Topic " + message.topic + " insert to collection " + col.name + "\n")









