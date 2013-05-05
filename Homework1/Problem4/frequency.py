'''Problem 4: Compute Term Frequency
Write a Python script, frequency.py, to compute the term frequency histogram of the livestream data you harvested from Problem 1.'''

import sys
import re
import string
import json

def parse_tweet_text(line):
    tweet = json.loads(line[:-1],encoding='utf-8')
    try:
        tweet_text = tweet['text']
    except KeyError:
        tweet_text = ""    
    text_parsed = re.sub('[^A-Za-z0-9 ]+','',tweet_text).lower().split(" ")
    return text_parsed

def get_tweets_parsed(tweet_file_path):
    tweets_parsed = []
    data = open(tweet_file_path,'r')
    for line in data.readlines():
        text_parsed = parse_tweet_text(line)
        tweets_parsed.extend( text_parsed )
    return tweets_parsed

def get_terms_used(tweets):
    terms_used = set(tweets)
    return terms_used

def count_terms(terms,tweets_parsed):
    terms_observed = { item: 0.0 for item in terms}
    tot_count = 0.0
    
    try:
        del terms_observed['']
    except:
        pass

    for word in tweets_parsed:
        try:
            terms_observed[word] += 1
            tot_count += 1
        except KeyError:
            pass
    terms_frequency = { key:  terms_observed[key]/tot_count for key in terms_observed }
    return terms_frequency
    
def main():

    tweet_file_path = (sys.argv[1])

    tweets_parsed = get_tweets_parsed(tweet_file_path)

    terms_all = get_terms_used(tweets_parsed)

    res = count_terms(terms_all, tweets_parsed)

    for key in res:
        print key, res[key]

if __name__ == '__main__':
    main()
