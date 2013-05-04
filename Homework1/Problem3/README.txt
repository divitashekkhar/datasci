In order to run program you shold write the following comand in cmd

python term_sentiment.py <sentiment_file> <tweet_file>

As the result you would get sentiment score for each term whice were not observed in sentiment dictionary ( e.g AFINN-111.txt). Those results are printed to stdout.

Term sentimetns is calculated via the following algortihm:
1) Estimate score sentiment for each tweet <tweet_file> accordingly to sentiment dictionary <sentiment_file>
2) Find all tweets wherer particular terms occured
3) Take average sentiment score as estimate for term score 

Additioinal files:
output.txt, outputtop20.txt is sample data used from previous task.