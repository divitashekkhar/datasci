'''Problem 4: Compute Term Frequency
Write a Python script, frequency.py, to compute the term frequency histogram of the livestream data you harvested from Problem 1.'''

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

def parse_tweet_text(line):
    tweet = json.loads(line[:-1],encoding='utf-8')
    try:
        tweet_text = tweet['text']
    except KeyError:
        tweet_text = ""    
    text_parsed = re.sub('[^A-Za-z0-9 ]+','',tweet_text).lower().split(" ")
    return text_parsed
    
def main():
    sent_file_path = (sys.argv[1])
    tweet_file_path = (sys.argv[2])

    sentiment_dict = get_sentiment_dict(sent_file_path)
    tweets_scored = get_tweets_scored(tweet_file_path, sentiment_dict)

    terms_all = get_terms_used(tweets_scored)
    terms_new = exclude_old_terms(terms_all,sentiment_dict)
    res = score_terms(terms_new, tweets_scored)

    del res['']
    for key in res:
        print key, res[key]

if __name__ == '__main__':
    main()
