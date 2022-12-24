import pymongo
from app import keywords
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

col = mydb["users"]

print("List of databases:")
print(myclient.list_database_names())
print("\n" + "List of collections from database " + mydb.name )
print(mydb.list_collection_names())

# print(mycol.count_documents({}))

cursor = col.find({})
for document in cursor:
    print(document)


"""""
x = col.delete_many({})
print(x.deleted_count, " documents deleted.")
"""""

'''''
for i in keywords:
    col = mydb[i]
    col.drop()
    print(col.name + " droped\n")


col = mydb['sources_domain_name']
col.drop()
print(col.name + " droped\n")

col = mydb['users']
col.drop()
print(col.name + " droped\n")
'''''
