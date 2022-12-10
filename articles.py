from newsapi import NewsApiClient
import json

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

    return all_articles

def names(keyword):
    data = postNewsAPI(keyword)
    print(data.find('url'))


