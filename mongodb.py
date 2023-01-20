import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print("List of databases:")
print(myclient.list_database_names())
print("\n" + "List of collections from database " + mydb.name)
print(mydb.list_collection_names())


col = mydb['users']

cursor = col.find({})
print('\nList of users')
for document in cursor:
    print(document)



"""""

keywords = ['iphone', 'android', 'cars', 'intel', 'microsoft', 'sony', 'java', 'python',
'pop', 'greece', 'gaming', 'xbox', 'marketing']

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
"""""


