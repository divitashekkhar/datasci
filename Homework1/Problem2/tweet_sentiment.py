''' Problem 2: Derive the sentiment of each tweet'''

import json
import sys
import string
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

##if __name__ == '__main__':
##    main()

sentiment_file = open('AFINN-111.txt','r')
data = open("outputtop20.txt",'r')


sentiment_dict = dict()
for line in sentiment_file.readlines():
    line_sp =  line[:-1].split("\t")
    try:
        sentiment_dict[line_sp[0]] = int(line_sp[1])
    except ValueError:
        sentiment_dict[line_sp[0]] = 0
        
for line in data.readlines():
    tweet = json.loads(line[:-1],encoding='utf-8')
    try:
        tweet_text = tweet['text']
    except KeyError:
        tweet_text = ""    
    text_parsed = re.sub('[^A-Za-z0-9 ]+','',tweet_text).lower().split(" ")
