import json
from kafka import KafkaConsumer
from app import keywords
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

# generating the Kafka Consumer
topics = keywords
my_consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=['localhost : 9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

my_consumer.subscribe(topics=topics)

for message in my_consumer:
        col = mydb[message.topic]
        print("Consumer reads message from topic " + message.topic + "\n")
        message = message.value
        #col.insert_one(message)
        #print(message)









