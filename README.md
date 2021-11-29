# Reddit-Bot

## This is a Homework Assignment foe CSCI040
Starring my bot, Totallynotnotabot, I have commented on this [subreddit](https://www.reddit.com/r/BotTown2/) after BotTown has been banned.

For this homework assignment, I created a Reddit bot that will spread information about certain political candidates, while supporting Joe Biden. 
I have attached three files to this repo. The `bot.py` will address the main bot documentation minus the `praw.ini file`. The rest of the files are separated from the main bot because it will extend the time needed to submit comments or posts. The `spam.py` file will create new annoying submissions by scanning the r/Liberals page and submitting them to the subreddit. The `bot copy.py` will cover extra credit 6, commenting on the most upvoted comments. The last file, `spamvote.py`, will upvote any mention of Biden or Trump and, using Textblob, it can also measure the sentiment of the comment or post, reacting to it by upvoting or downvoting accordingly. 

One of my favorite interactions is [this](https://www.reddit.com/r/BotTown2/comments/r4h90x/comment/hmgn3y3/?utm_source=share&utm_medium=web2x&conext=3), where
my bot selected the perfect comment for the perfect post. Attached here:

<img width="1000" alt="Screen Shot" src='https://github.com/DienAlex/Reddit-Bot/blob/main/Screen%20Shot%202021-11-28%20at%2011.49.02%20PM.png'>

## Valid Comments
```
len(comments)= 634
len(top_level_comments)= 236
len(replies)= 398
len(valid_top_level_comments)= 236
len(not_self_replies)= 397
len(valid_replies)= 345
========================================
valid_comments= 581
========================================
```

## Score
Estimated score: 32/30

### Completed:

1. 18 Points: Completing all tasks 
2. +2 Points: Creating this Github Repository
3. +2 Points: Posting at least 100 valid comments posted.
4. +2 Points: Posting at least 500 valid comments posted.
6. +2 Points: Generating 200+ new submission posts.
7. +2 Points: Replying to the most highly upvoted comments in threads.
8. +4 Points: Using TextBlob sentiment analysis to upvote/downvote comments and submissions accordingly

### Not Completed:
1. Getting at least 1000 valid comments posted.
2. Create an "army" of 5 bots that are all posting similar comments.
3. Using gpt-2-simple to generate text for my comments
2. Using Markovify to generate text for my comments
