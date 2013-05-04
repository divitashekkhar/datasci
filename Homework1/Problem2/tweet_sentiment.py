''' Problem 2: Derive the sentiment of each tweet'''

import json
import sys
import string
import re

sentiment_file_path ='AFINN-111.txt'

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def get_sentiment_dict(sentiment_file_path)
    sentiment_file = open(sentiment_file_path,'r')
    sentiment_dict = dict()
    for line in sentiment_file.readlines():
        line_sp =  line[:-1].split("\t")
        try:
            sentiment_dict[line_sp[0]] = int(line_sp[1])
        except ValueError:
            sentiment_dict[line_sp[0]] = 0
    return sentiment_dict

    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

##if __name__ == '__main__':
##    main()

data = open("outputtop20.txt",'r')

sentiment_dict = get_sentiment_dict(sentiment_file_path)

for line in data.readlines():
    tweet = json.loads(line[:-1],encoding='utf-8')
    try:
        tweet_text = tweet['text']
    except KeyError:
        tweet_text = ""    
    text_parsed = re.sub('[^A-Za-z0-9 ]+','',tweet_text).lower().split(" ")

tot_sentiment = 0
for word in text_parsed:
    tot_sentiment += sentiment_dict[word]

