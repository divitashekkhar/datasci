import json
import sys
import string
import re

tweet_file_path = 'output.txt'

data = open(tweet_file_path,'r') 
line = data.readline()
tweet = json.loads(line[:-1],encoding='utf-8')
tweet["user"]
