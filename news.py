from newsapi import NewsApiClient
import random

# Init
newsapi = NewsApiClient(api_key='71253741f1b64ba0adb6c07eab951843')


sources = [   'the-wall-street-journal',
              'bbc-news',
              'bloomberg',
              'al-jazeera-english']

headlines = dict()

abv = dict()
abv['the-wall-street-journal'] = 'WSJ'
abv['bbc-news'] = 'BBC'
abv['bloomberg'] = 'BB'
abv['al-jazeera-english'] = 'AJ'

for source in sources:
       top_headlines = newsapi.get_top_headlines(sources=source,language='en')
       headline = []
       for article in top_headlines['articles']:
              headline.append(article['title'])

       headlines[abv[source]] = headline

#print(headlines)


list = []

src = ['WSJ','BBC','BB','AJ']

for i in range(4):
       sources[i] = src[i]

for source in sources:
       if source == 'AJ':
              tup = (random.sample(headlines[source],1),source)
              list.append(tup)
       else:
              tup = (random.sample(headlines[source],random.randint(1,2)),source)
              list.append(tup)
j=1
for tup in list:
       for article in tup[0]:
              print("{}. {} ({})".format(j,article,tup[1]))
              j += 1

