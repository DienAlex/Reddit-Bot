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


    #Extra Credit

def score_comment(comment):
    comment = random.choice(comments_without_replies)
    highest_comment = comment.score
    return highest_comment



reddit = praw.Reddit('bot', user_agent='cs40')


submission_url = 'https://www.reddit.com/r/BotTown2/comments/r1s3p3/us_blacklists_dozens_of_chinese_tech_firms_citing/'
submission = reddit.submission(url=submission_url)
submission2 = reddit.submission('https://www.reddit.com/user/Extension-Pea4503/comments/r4pmkq/testbot_notification/')


while True:


    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)




    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = list(submission.comments.list())



    print('len(all_comments)=',len(all_comments))




    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'Totallynotnotabot':
            not_my_comments.append(comment)




    print('len(not_my_comments)=',len(not_my_comments))


    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:

        text = generate_comment()
        submission.reply(text)
        


    else:

        comments_without_replies = []
        for comment in not_my_comments:
            if comment.author != 'Totallynotnotabot':
                comments_without_replies.append(comment)
                for reply in comment.replies:
                    if str(reply.author) == 'Totallynotnotabot':
                        pass
        print('comments_without_replies=', len(comments_without_replies))

        print('len(comments_without_replies)=',len(comments_without_replies))






        # comment = random.choice(comments_without_replies)





        try: 
            # comment.reply(generate_comment())


            #Extra Credit

            comment=sorted(comments_without_replies,key=lambda comments: comments.score,reverse=True)[0]
            comment.reply(generate_comment())
            print('score=', comment.score)
            print('author=', comment.author)



        except praw.exceptions.APIException:
            #if error it will notify me here: 
            submission2.reply('Error')
            pass
        except AttributeError:
            submission2.reply('Error')
            print ('error reply')

        except TypeError:
            submission2.reply('Error')
            print ('error reply')





    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=50)))
    print ('title=', submission.title)
    print('link=', submission.permalink)
    print('submission=', submission)



    time.sleep(50)

