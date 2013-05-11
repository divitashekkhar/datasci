'''Problem 4: Compute Term Frequency
Write a Python script, frequency.py, to compute the term frequency histogram of the livestream data you harvested from Problem 1.'''

import sys
import re
import string
import json

def parse_tweet_text(line):
    tweet = json.loads(line[:-1],encoding='utf-8')
    res =[]
    try:
        tags = tweet['entities']['hashtags']
    except KeyError:
        return res

    for tag in tags:
        res.append( tag['text'].encode('utf-8')  )

    return res


def get_tweets_parsed(tweet_file_path):
    tweets_parsed = []
    data = open(tweet_file_path,'r')
    for line in data.readlines():
        tags = parse_tweet_text(line)
        if len(tags) > 0:
            tweets_parsed.extend( tags )
    return tweets_parsed

def get_tags_used(tweets):
    tags_used = set(tweets)
    return tags_used

def count_tags(tags,tweets_parsed):
    tags_observed = { item: 0.0 for item in tags}
    tot_count = 0.0
    
    try:
        del tags_observed['']
    except:
        pass

    for word in tweets_parsed:
        try:
            tags_observed[word] += 1
        except KeyError:
            pass
    tags_count = { key:  tags_observed[key] for key in tags_observed }
    return tags_count
    
def main():

    tweet_file_path = (sys.argv[1])

    tweets_parsed = get_tweets_parsed(tweet_file_path)

    tags_all = get_tags_used(tweets_parsed)

    res = count_tags(tags_all, tweets_parsed)

    for key in res:
        print key, res[key]

if __name__ == '__main__':
    main()
