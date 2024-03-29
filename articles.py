from newsapi import NewsApiClient
import requests

# Init
newsapi = NewsApiClient(api_key='4d1d7d11eab64482a94668a4899dfc5e')
#newsapi = NewsApiClient(api_key='995786d01d324334a9dce9b5f8fe405f')
#newsapi = NewsApiClient(api_key='6a232d49d2c44edf848448c31654e4b5')

def postNewsAPI (keyword):

    top_headlines = newsapi.get_top_headlines(q=keyword,
                                              #  sources='bbc-news,the-verge',
                                              language='en')

    # /v2/everything
    all_articles = newsapi.get_everything(q=keyword,
                                          # sources='bbc-news,the-verge',
                                          # domains='bbc.co.uk,techcrunch.com',
                                          # from_param='2022-10-10',
                                          # to='2022-11-01',
                                          language='en',
                                          sort_by='relevancy')
    # /v2/top-headlines/sources
    sources = newsapi.get_sources()

    return all_articles



def names(data):
    #print('Source names for ' + keyword)
    source_names = []
    for i in range(len(data['articles'])):
        name = data['articles'][i]['source']['name']
        if name not in source_names:
            source_names.append(name)

    return source_names


def find_extract(source_name):
    #print(str(source_names))

    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'utf8': 1,
        'srsearch': 'python'
    }


    #print('\n######### Source name for ' + s + ' #############')
    url = ('https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exsentences=10&exlimit=1&titles=') + \
            source_name + ('&explaintext=1&formatversion=2')

    media_wiki = requests.get(url, params=params).json()

    try:
        extract = str(media_wiki['query']['pages'][0]['extract'])
        if extract:
            if extract is None:
                #print('\n######## EXTRACT IS EMPTY ' + s + ' #############')
                return
            else:
                #print(extract +'\n')
                return extract
    except KeyError:
        #print('########## Not found extract for domain name ' + s)
        return