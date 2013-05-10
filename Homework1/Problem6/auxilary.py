import json
import sys
import string
import re

tweet_file_path = 'output.txt'

data = open(tweet_file_path,'r') 
for line in data.readlines():
    tweet = json.loads(line[:-1],encoding='utf-8')
    try:
        l = tweet['entities']['hashtags']
        if len(l) > 0:
            break
        else:
            pass
    except KeyError:
        pass
