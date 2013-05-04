"""Problem 0: Query Twitter with Python
This is a warmup exercise"""

import urllib
import json

for i in range(1,11,1):
    url_str = "http://search.twitter.com/search.json?q=microsoft&page=" + str(i)
    response = urllib.urlopen(url_str)
    query = json.load(response)

    print '======================= page %s ======================\n' %i 
    for result in query['results']:
        string = result['text'].encode('utf-8')
        print string + "\n"
