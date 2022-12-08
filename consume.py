from json import loads
from kafka import KafkaConsumer
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["articles"]

# generating the Kafka Consumer
#def consumer(keyword):
my_consumer = KafkaConsumer(
        'iphone',
        bootstrap_servers=['localhost : 9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for message in my_consumer:
        message = message.value
        mycol.insert_one(message)
        print(message)






