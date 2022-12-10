import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["articles"]

# print(mycol.count_documents({}))

cursor = mycol.find({})
for document in cursor:
    print(document)


x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")