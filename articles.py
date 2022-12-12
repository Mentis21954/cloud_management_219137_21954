from newsapi import NewsApiClient
import pandas as pd
import json
import requests

# Init
#newsapi = NewsApiClient(api_key='4d1d7d11eab64482a94668a4899dfc5e')
newsapi = NewsApiClient(api_key='995786d01d324334a9dce9b5f8fe405f')

def postNewsAPI (keyword):

    top_headlines = newsapi.get_top_headlines(q=keyword,
                                              #  sources='bbc-news,the-verge',
                                                language='en')

    # /v2/everything
    all_articles = newsapi.get_everything(q=keyword,
                                             # sources='bbc-news,the-verge',
                                             # domains='bbc.co.uk,techcrunch.com',
                                            #  from_param='2022-10-10',
                                            #  to='2022-11-01',
                                              language='en',
                                              sort_by='relevancy')
    # /v2/top-headlines/sources
    sources = newsapi.get_sources()

    # Serializing JSON
    # json_object = json.loads(postNewsAPI('iphone'))
    return all_articles

"""""
print('Source name for iphone')
data = postNewsAPI('iphone')
source_names = []
for i in range(len(data['articles'])):
    name = data['articles'][i]['source']['name']
    if name not in source_names:
        source_names.append(name)

print(source_names)
"""""
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=YouTube&explaintext=1&formatversion=2'
params = {
    'action':'query',
    'format':'json',
    'list':'search',
    'utf8':1,
    'srsearch':'python'
}
media_wiki = requests.get(url, params=params).json()
# media_wiki = json.dumps(media_wiki)
extract = media_wiki['query']['pages'][0]['extract']
if extract is '':
    print('exract is empty')
else:
    print(extract)

def names(keyword, data):
    #data = postNewsAPI('iphone')
    source_names = []
    for i in range(len(data['articles'])):
        name = data['articles'][i]['source']['name']
        if name not in source_names:
            source_names.append(name)

    print(source_names)
    return source_names


