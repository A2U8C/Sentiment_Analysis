import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import time

import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize'] = 12, 8

config = pd.read_csv("./config.csv")
twitterApiKey = config['twitterApiKey'][0]
twitterApiSecret = config['twitterApiSecret'][0]
twitterApiAccessToken = config['twitterApiAccessToken'][0]
twitterApiAccessTokenSecret = config['twitterApiAccessTokenSecret'][0]

# Authenticate
auth = tweepy.OAuthHandler(twitterApiKey, twitterApiSecret)
auth.set_access_token(twitterApiAccessToken, twitterApiAccessTokenSecret)
twetterApi = tweepy.API(auth, wait_on_rate_limit = True)

def cleanUpTweet(txt):
    txt = re.sub(r'@[A-Za-z0-9_]+', '', txt)
    txt = re.sub(r'#', '', txt)
    txt = re.sub(r'RT : ', '', txt)
    txt = re.sub(r'https?:\/\/[A-Za-z0-9\.\/]+', '', txt)

    return txt


def getTextSubjectivity(txt):
    return TextBlob(txt).sentiment.subjectivity

def getTextPolarity(txt):
    return TextBlob(txt).sentiment.polarity

def getTextAnalysis(a):
    if a < 0:
        return "Negative"
    elif a == 0:
        return "Neutral"
    else:
        return "Positive"

def usernameOnly(text):
    twitterAccount = text
    tweets = tweepy.Cursor(twetterApi.user_timeline,
                           screen_name=twitterAccount,
                           count=None,
                           since_id=None,
                           max_id=None,
                           trim_user=True,
                           exclude_replies=True,
                           contributor_details=False,
                           include_entities=False
                           ).items(50);

    #print(len(tweets))
    df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweet'])
    df['Tweet'] = df['Tweet'].apply(cleanUpTweet)
    df['Subjectivity'] = df['Tweet'].apply(getTextSubjectivity)
    df['Polarity'] = df['Tweet'].apply(getTextPolarity)
    df['Score'] = df['Polarity'].apply(getTextAnalysis)
    name=DataAnalyse(df)
    sub_polar_name=Subj_Polarity(df)
    return df,name,sub_polar_name,twitterAccount


def topicOnly(text):
    clean_text=cleanUpTweet(text)
    text_subjective=getTextSubjectivity(text)
    text_polarity=getTextPolarity(text)
    text_score=getTextAnalysis(text_polarity)
    return clean_text,text_subjective,text_polarity,text_score,text

def DataAnalyse(df):
    #import matplotlib
    # The important line!
    #matplotlib.use('Agg')
    plt.clf()
    ts = time.time()
    ts = int(ts)
    name = "plot" + str(ts) + ".png"
    Final_name = "website/static/Image_Uploads/Bar_Graphs/" + name
    print(Final_name)
    labels = df.groupby('Score').count().index.values
    values = df.groupby('Score').size().values
    plt.bar(labels, values)
    plt.savefig(Final_name)
    return name

def Subj_Polarity(df):
    plt.clf()
    ts2 = time.time()
    ts2 = int(ts2)
    name2 = "plot_" + str(ts2) + ".png"
    Final_name2 = "website/static/Image_Uploads/Scatter_Graphs/" + name2
    print(Final_name2)
    for index, row in df.iterrows():
        if row['Score'] == 'Positive':
            plt.scatter(row['Polarity'], row['Subjectivity'], color="green")
        elif row['Score'] == 'Negative':
            plt.scatter(row['Polarity'], row['Subjectivity'], color="red")
        elif row['Score'] == 'Neutral':
            plt.scatter(row['Polarity'], row['Subjectivity'], color="blue")

    plt.title('Twitter Sentiment Analysis')
    plt.xlabel('Polarity')
    plt.ylabel('Subjectivity')
    plt.savefig(Final_name2)
    return name2