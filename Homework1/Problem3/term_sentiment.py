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

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

##def main():
##    sent_file = open(sys.argv[1])
##    tweet_file = open(sys.argv[2])
##    hw()
##    lines(sent_file)
##    lines(tweet_file)

##if __name__ == '__main__':
##    main()

sent_file_path = 'AFINN-111.txt'
data = open('outputtop20.txt','r')

sentiment_dict = get_sentiment_dict(sent_file_path)

for line in data.readlines():
    text_parsed = parse_tweet_text(line)
    score = get_sentiment_score(text_parsed,sentiment_dict)
    print score
