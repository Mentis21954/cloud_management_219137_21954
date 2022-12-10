import json
from json import loads
from kafka import KafkaConsumer
from app import keywords
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["articles"]

# generating the Kafka Consumer
topics = keywords
my_consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=['localhost : 9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

my_consumer.subscribe(topics=topics)

for message in my_consumer:
        print("Consumer reads message from topic " + message.topic)
        message = message.value
        mycol.insert_one(message)
        #print(message)









