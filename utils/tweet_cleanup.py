filename = 'trump_tweets.txt'
file = open(filename)
lines = file.readlines()
file.close()

new_file = open('trump_tweet_cleanup.txt', 'w+')
new_lines = []

for line in lines:
    if 'http' not in line:
        new_file.write(line)

new_file.close()
