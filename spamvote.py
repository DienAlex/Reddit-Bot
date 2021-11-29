import praw
import random
import datetime
import time
from praw.reddit import Subreddit
from textblob import TextBlob

reddit = praw.Reddit('bot', user_agent='cs40')
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r4ep50/the_justice_department_puts_states_on_notice/'
submission = reddit.submission(url=submission_url)

while True:
    submission.comments.replace_more(limit=None)

    for submission in list(reddit.subreddit("BotTown2").new(limit=500)):
    # Uncomment next 7 lines to Upvote/Downvote on submissions
    #     if 'trump' in submission.title.lower():
    #         submission.downvote()
    #         print('Downvoted')
    # for submission in list(reddit.subreddit("BotTown2").new(limit=500)):
    #     if 'biden' in submission.title.lower():
    #         submission.upvote()
    #         print('Upvoted')

        for comment in submission.comments:

            commenttext = (TextBlob(comment.body).lower())
            if ("biden" in commenttext and commenttext.sentiment.polarity>0.5) or ("trump" in commenttext and commenttext.sentiment.polarity<-0.5):
                comment.upvote()
                print('Upvoted2')
                print('comment_body=',comment.body)
                print('link=',submission.permalink)

            elif ("biden" in commenttext and commenttext.sentiment.polarity<-0.5) or ("trump" in commenttext and commenttext.sentiment.polarity>0.5):
                comment.downvote()
                print('Downvoted2')
                print('link=',submission.permalink)

            else:
                pass
    print ('sleeping')
    time.sleep(25)

