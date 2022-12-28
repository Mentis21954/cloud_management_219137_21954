from app import keywords
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print("List of databases:")
print(myclient.list_database_names())
print("\n" + "List of collections from database " + mydb.name )
print(mydb.list_collection_names())


source_names_db = mydb["sources_domain_name"]
extracts = {}
source_names = []
cursor = source_names_db.find({})
for document in cursor:
    for key in document.keys():
        value = document.get(key)
        source_names.append(key)
        if value is not None:
            extracts[key] = str(value)

articles = {}

for s in source_names:
    col = mydb['iphone']
    cursor = col.find({})
    documents = []
    extracts2 = []
    for document in cursor:
        for i in range(len(document.get('articles'))):
            if s == document.get('articles')[i]['source']['name']:
                documents.append(document.get('articles')[i])
                if s in extracts.keys():
                    extracts2.append(extracts.get(value))

    articles[s] = documents


print(articles.keys())

"""""
x = col.delete_many({})
print(x.deleted_count, " documents deleted.")
"""""

"""""
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


