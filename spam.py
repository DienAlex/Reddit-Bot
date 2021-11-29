import praw
import random
import datetime
import time

reddit = praw.Reddit('bot', user_agent='cs40')
count = 0

while True:
    for i in random.choices(list(reddit.subreddit("Liberal").hot(limit=1000))):
        a = (i.title)
        b = (i.url)
        c = (i.selftext)
        print("="*40)
        print (reddit.subreddit("Liberal").hot(limit=1000))
        print ('title=', a)
        print ('URL=', b)
        print ('text=', c)

        #Uncomment for just URL
        # reddit.subreddit("BotTown2").submit(a, url=b)


        #Uncomment for just text
        reddit.subreddit("BotTown2").submit(a, selftext=c)




        count += 1
        print (count)
        time.sleep(50)
