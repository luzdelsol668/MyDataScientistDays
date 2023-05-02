import collections
import itertools
import re
from datetime import datetime
import os

import pandas as pd
import tweepy as tw
import matplotlib.pyplot as plt

# import pandas as pd
from art import *

consumer_key = 'umZfX0dvbbdPIv6ZN2*****'
consumer_secret = 'B6JKvGPxxdXVqfSceaKdj2vX6df1y586PiCV1RBgy******'
access_token = '1041754028001120256-OsXJLPpEqmdZaYW6V3tJAb******'
access_token_secret = '57kgIzZK2cofa5wGoAWfyfZii52o5EhW4ol*****'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())


stop_words =['forme', 'argent', '12', 'depuis', '2021', 'aidelfitr2023', '2021', 'charles',
             'dont', 'reoit', 'team228', 'nous', 'sommes', 'centaine', 'un', 'sattendre',
             'doivent', 'dont', 'problmes', 'un', 'li', 'plusieurs', 'gorg', 'moteur', 'fitr',
             'lhydre', 'fronti', 'que', 'font', 'rgionale', 'long', 'mais', 'si', 'aura', 'dans',
             'mon', 'pays', 'pour', '40', 'et', 'voici', 'tu', 'as', 'foison', 'voque', 'gravit',
             'selon', 'source', 'qui', 'bout', 'tne', 'rfrence', 'fin', 'touch', 'prfecture', 'au',
             'subit', 'n', 'ont', 'd', 'c',' est', 'comme', 'locomotive', 'sans', 'sur', '6', 'tt228',
             'pm', 'tus', 'par', 'ce', 'sur', 'ces', 'de', 'le', 'une', 'les', 'en', 'des', 'la', 'a', 'du',
             'si', 'se', 'puisse', 'dj', 'il', 'parle', 'te', 'dieu', 'charlesmichel', 'ue', 'cadres',
             'vont', 'musulmans', 'michel', 'i', 'y', 'plus', 'bunker', 'ne', 'rien', 'sert', 'cette',
             'foisci', '150', 'dd', 'stratgie', 'da', 'manire', 'nest', 'pas', 'dattendre', 'protger',
             'nouveau', 'avant', 'l', 'tous', 'instants', 'effective', 'concentre', 'aux', 'manifeste',
             'livre', 'bien', 'sauvages', 'vaut', 'bien', 'entorses', 'quelques', 'liberts', 'ditesvous',
             'tiens', 'donc', 'avant', 'tous', 'fegnassingbe', 'quarantaine', 'inflation', 'fauregnassingbe',
             'contagion']

while True:

    tprint("Python Data Mining from Tweeter\nMade By Luz DeMars",   font="small")

    tweeter_tags = input("Please Enter Tags to search")

    if tweeter_tags:
        search_query = str(tweeter_tags) + " -filter:retweets"
        search_result = api.search_tweets(
            q=search_query,
            until=str(datetime.strftime(datetime.today(), '%Y-%m-%d')),
            count=2500
        )

        search_result_without_url = [remove_url(tweet.text) for tweet in search_result]
        tg_tweets_splited = [tweet.lower().split() for tweet in search_result_without_url]
        clean_tweets = [[word for word in tweet_words if not word in stop_words]
                        for tweet_words in tg_tweets_splited]

        all_words = list(itertools.chain(*clean_tweets))
        collection_words = collections.Counter(all_words)
        clean_tweets_tabled = pd.DataFrame(collection_words.most_common(),
                                           columns=['mot utilisé', 'nombre de fois'])

        fig, ax = plt.subplots(figsize=(20, 20))
        ax.set_title("Common Words Found in Tweets (During Terrorism Attack in the north of Togo )")
        clean_tweets_tabled.sort_values(by='nombre de fois').plot.barh(x='mot utilisé',
                                                                       y='nombre de fois',
                                                                       ax=ax,
                                                                       color="purple")

        plt.show()

        input("Press any key to exit")
        plt.close(fig)
        break




