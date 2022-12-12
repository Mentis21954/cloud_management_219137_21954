from newsapi import NewsApiClient
import pandas as pd
import json
import requests

# Init
newsapi = NewsApiClient(api_key='4d1d7d11eab64482a94668a4899dfc5e')
#newsapi = NewsApiClient(api_key='995786d01d324334a9dce9b5f8fe405f')

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


def names(keyword, data):
    print('Source names for ' + keyword)
    source_names = []
    for i in range(len(data['articles'])):
        name = data['articles'][i]['source']['name']
        if name not in source_names:
            source_names.append(name)

    return source_names


def find_extract(keyword, data):
    #data = postNewsAPI(keyword)
    source_names = names(keyword, data)
    print(str(source_names))

    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'utf8': 1,
        'srsearch': 'python'
    }

    extract_list = []
    for s in source_names:
        #print('\n######### Source name for ' + s + ' #############')
        url = ('https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=') + \
              s + ('&explaintext=1&formatversion=2')

        media_wiki = requests.get(url, params=params).json()

        try:
            extract = media_wiki['query']['pages'][0]['extract']
            if extract:
                if extract is '':
                    print('\n######## EXTRACT IS EMPTY ' + s + ' #############')
                    continue
                else:
                    # print(extract +'\n')
                    extract_list.append(extract)
            else:
                continue
        except KeyError:
            print('Not found extract for domain name ' + s)
            continue


    return extract_list

# find_extract('iphone')