import matplotlib.pyplot as plt
import pandas as pd
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

def numb_articles_by_coll(date,col_name):

    # articles from collection
    articles_by_coll = []
    # collection
    col = mydb[col_name]
    cursor = col.find({})
    for document in cursor:
        count = 0
        # for each date check how many articles published
        for d in date:
            for i in range(len(document.get('articles'))):
                if (d in document.get('articles')[i]['publishedAt']):
                    count += 1
            print('Collection ' + col.name + ' has ' + str(count) + ' articles' + ' published at ' + d)
            articles_by_coll.append(count)

    print('\n')
    return articles_by_coll


date = ['2022-12-15', '2022-12-16', '2022-12-17', '2022-12-18', '2022-12-19']
# store number of articles from collections
articles = []
# store name of collections
collections = []

for col_name in mydb.list_collection_names():
    # search all collections except domain name and users
    if col_name != 'sources_domain_name' and col_name != 'users':
        # find and store the number of articles from collection for these dates
        articles.append(numb_articles_by_coll(date, col_name))
        # find and store the collections names that have articles with these dates
        collections.append(col_name)


# create dataframe
df = pd.DataFrame(data={'date': date, collections[0]: articles[0], collections[1]: articles[1], collections[2]: articles[2]
                        , collections[3]: articles[3], collections[4]: articles[4], collections[5]: articles[5]
                        , collections[6]: articles[6], collections[7]: articles[7], collections[8]: articles[8]})

print(df)

# plot
df.plot(x='date', kind='bar', stacked=True)
plt.ylabel("Number of articles")
plt.title('Articles published by category')
plt.show()














