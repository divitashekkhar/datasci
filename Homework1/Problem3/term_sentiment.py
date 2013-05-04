"""Problem 3: Derive the sentiment of new terms
Your script should print to stdout each term-sentiment pair, one pair per line, in the following format:<term:string> <sentiment:float>
"""
import sys
import string
import re
import json

from tweet_sentiment import get_sentiment_score
from tweet_sentiment import get_sentiment_dict
from tweet_sentiment import parse_tweet_text

def get_tweets_scored(tweet_file_path, sentiment_dict):
    tweets_scored = []
    data = open(tweet_file_path,'r')
    for line in data.readlines():
        text_parsed = parse_tweet_text(line)
        for word in text_parsed:
            score = get_sentiment_score(text_parsed,sentiment_dict)   
        tweets_scored.append( (text_parsed, score) )
    return tweets_scored

def get_terms_used(tweets):
    terms_all = []
    for tweet in tweets:
        for word in tweet[0]:
            terms_all.append(word)
    terms_used = set(terms_all)
    return terms_used

def exclude_old_terms(terms,sentiment_dict):
    terms_old = [key for key in sentiment_dict]
    terms_new = terms.difference(terms_old)
    return terms_new   

def score_terms(terms,tweets_scored):
    terms_observed = { item: [0,0] for item in terms} 
    for tweet in tweets_scored:
        for word in tweet[0]:
            try:
                terms_observed[word][0] += tweet[1]
                terms_observed[word][1] += 1
            except KeyError:
                pass
    terms_scored = { key:  terms_observed[key][0]/terms_observed[key][1] for key in terms_observed }
    return terms_scored
    
def main():
    sent_file_path = (sys.argv[1])
    tweet_file_path = (sys.argv[2])

    sentiment_dict = get_sentiment_dict(sent_file_path)
    tweets_scored = get_tweets_scored(tweet_file_path, sentiment_dict)

    terms_all = get_terms_used(tweets_scored)
    terms_new = exclude_old_terms(terms_all,sentiment_dict)
    res = score_terms(terms_new, tweets_scored)

    for key in res:
        print key, res[key]
                     
if __name__ == '__main__':
    main()
