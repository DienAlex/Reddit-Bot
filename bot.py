import praw
import random
import datetime
import time

# /FIXME: 
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[Biden] [should] fix our food prices. After all, I am a [robot] who enjoys eating [nuts] and [bolts]. ",
    "[Biden] [should] add dad jokes to their speeches. For example: What do [doggy] [robots] do? They [byte]!",
    "Biden should [enjoy] some [programmed] dad jokes! Why did the [robot] fail his [exam]? He was [a bit] rusty!",
    "[Biden] has just announced [Club Penguin] as game of the year! We should celebrate this occasion with [nuts] and [bolts] for [dinner].",
    "Despite everything, Biden is a [good] president that is meeting [status quo]. [No one] can change my [mind] because I am a [robot]",
    "I can't believe that [Biden] has been [making secret deals] with [Kim Jong Un]. I [don't know] if this is [beneficial] for our nation or not",

    ]

replacements = {
    'programmed' : ['not programmed', 'definitely programmed', 'hilarious', 'enjoyable', 'funny'],
    'I am' : ['We are', 'This bot is', 'This robot is', 'Everyone here is', 'This entire post is'],
    'should' : ['should definitely', 'should definitely not', 'should totally', 'should not', 'should totally not'],
    'nuts' : ['electric', 'watts', 'money', 'metal', 'code'],
    'bolts'  : ['other bots', 'reddit likes', 'capitalism', 'monsters', 'not water'],
    'enjoy' : ['not enjoy', 'definitely enjoy', ' better enjoy', 'laugh at', 'like'],
    'upset' : ['sad', 'angry', 'unhappy', 'miserable', 'uncomfortable'],
    'doggy' : ['dog', 'pet', 'monster', 'children', 'biting'],
    'robots' : ['bots', 'cyborgs', 'machines', 'droids', 'andriods'],
    'exam' : ['test', 'quiz', 'midterm', 'final', 'assessment'],
    'a bit' : ['very', 'extremely', 'awfully', 'excessively', 'terribly'],
    'robot' : ['bot', 'cyborg', 'machine', 'droid', 'andriod'],
    'Club Penguin' : ['Minecraft', 'Pokemon', 'Fortnite', 'GTA', 'Call of Duty'],
    'good' : ['decent', 'amazing', 'great', 'pretty good', 'not bad'],
    'No one' : ['Nobody', 'Not a single soul', 'No human', 'No person on this planet', 'No man or woman'],
    'mind' : ['opinion', 'view', 'belief', 'thinking', 'angle'],
    'everyone' : ['my creator', 'my father', 'my mother', 'my friend', 'my dog'],
    'byte' : ['will byte', 'can byte', 'will byte you', 'might byte you', 'might byte'],
    'status quo' : ['expectations', "people's needs", 'his political agenda', "both parties's agenda", 'social standards'],
    'Biden' : ['AOC', 'Trump', 'Kamala Harris', 'People', 'Obama'],
    'making secret deals' : ['partying', 'drinking', 'hanging out', 'baking cakes', 'secretly making visits to Area 51'],
    'Kim Jong Un' : ['Xi Jinping', 'Vladimir Putin', 'Pope Francis', 'Jeff Bezos', 'Mark Zuckerberg'],
    "don't know" : ['am unsure', 'am not sure', 'am uncertain', 'am doubtful', 'am hesitant to say'],
    'beneficial' : ['terrible', 'bad', 'great', 'amazing', 'good'],
    'dinner' : ['lunch', 'breakfast', 'brunch', 'our next meal', 'linner'],
    }


def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return s

# /FIXME:
# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40')

# /FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r1s3p3/us_blacklists_dozens_of_chinese_tech_firms_citing/'
submission = reddit.submission(url=submission_url)
submission2 = reddit.submission('https://www.reddit.com/user/Extension-Pea4503/comments/r4pmkq/testbot_notification/')

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions


    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = list(submission.comments.list())


    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # /FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not


    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'Totallynotnotabot':
            not_my_comments.append(comment)



    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        # /FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)
        


    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            if comment.author != 'Totallynotnotabot':
                comments_without_replies.append(comment)
                for reply in comment.replies:
                    if str(reply.author) == 'Totallynotnotabot':
                        pass
        print('comments_without_replies=', len(comments_without_replies))

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        comment = random.choice(comments_without_replies)
        try: 
            comment.reply(generate_comment())
        except praw.exceptions.APIException:
            #if error it will notify me here: 
            submission2.reply('Error')
            pass
            

        #this is to notify me if there is an error

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions


    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=50)))
    print ('title=', submission.title)
    print('link=', submission.permalink)
    print('submission=', submission)


    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(50)

