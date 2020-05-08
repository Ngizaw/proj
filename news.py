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

list = []

src = ['WSJ','BBC','BB','AJ']

for i in range(4):
       sources[i] = src[i]

hDict = dict()
i = 1
for source in src:
    for hLine in headlines[source]:
        tup = (hLine, source)
        hDict[i] = (tup)
        i += 1

for j in hDict:
    print(j,hDict[j][0], "({})".format(hDict[j][1]))

art1, art2, art3, art4, art5 = input("Pick 5 articles: ").split()
choices = [art1, art2, art3, art4, art5]

j=1
for choice in choices:
    print("{}.".format(j), hDict[int(choice)][0], "({})".format(hDict[int(choice)][1]))
    j+=1

# # i = 1
# #
# # for tup in hLines:
# #     hDict[i] = tup
# #     #print (tup[0], tup[1])
#
# # for source in sources:
# #     for article in headlines[source]:
# #         tup = (article,source)
# #         list.append(tup)
# # print( list)
# #
# # for source in sources:
# #        if source == 'AJ':
# #               tup = (random.sample(headlines[source],1),source)
# #               list.append(tup)
# #        else:
# #               tup = (random.sample(headlines[source],random.randint(1,2)),source)
# #               list.append(tup)
# j=1
# for tup in list:
#        for article in tup[0]:
#               print("{}. {} ({})".format(j,article,tup[1]))
#               j += 1
