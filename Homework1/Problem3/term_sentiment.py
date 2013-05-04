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

def get_all_tweets_scored_and_terms_used(tweet_file_path, sentiment_dict):
    tweets_scored = []
    terms_all = []
    data = open(tweet_file_path,'r')
    for line in data.readlines():
        text_parsed = parse_tweet_text(line)
        for word in text_parsed:
            terms_all.append(word)
            score = get_sentiment_score(text_parsed,sentiment_dict)   
        tweets_scored.append( (text_parsed, score) )
    return ( tweets_scored, terms_all )

def main():
    sent_file_path = (sys.argv[1])
    tweet_file_path = (sys.argv[2])

    sentiment_dict = get_sentiment_dict(sent_file_path)

    tweets_and_terms = get_all_tweets_scored_and_terms_used(tweet_file_path, sentiment_dict)

    tweets_scored = tweets_and_terms[0]
    terms_all = tweets_and_terms[1]

    terms_all = set(terms_all)
    terms_old = [key for key in sentiment_dict]
    terms_new = terms_all.difference(terms_old)
    terms = { item: [0,0] for item in terms_new} 

    for tweet in tweets_scored:
        for word in tweet[0]:
            try:
                terms[word][0] += tweet[1]
                terms[word][1] += 1
            except KeyError:
                pass

    for key in terms:
        term_sentiment = terms[key][0]/terms[key][1]
        print key , term_sentiment 

if __name__ == '__main__':
    main()
