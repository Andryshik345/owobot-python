# -*- coding: utf-8 -*-

import random
import praw, boards

# Limits maximum posts count
LIMIT = 6

# Maximum random retries of submissions
RETRYMAX = 3

def Session(client_id, client_secret, user_agent):
    global session
    session = praw.Reddit(client_id=client_id,
                          client_secret=client_secret,
                          user_agent=user_agent)

def GetPicSFW():
    if not session:
        return False

    subreddit = session.subreddit(random.choice(boards.SFW))
    
    submission = subreddit.new(limit=LIMIT)
    for i in range(0, RETRYMAX):
        urls = []
        for s in submission:
            if ".jpg" in s.url or ".png" in s.url:
                urls.append(s.url)
        if not len(urls) is 0:
            break
    return random.choice(urls)

def GetPicNSFW():
    if not session:
        return False

    subreddit = session.subreddit(random.choice(boards.NSFW))
    
    submission = subreddit.new(limit=LIMIT)
    for i in range(0, RETRYMAX):
        urls = []
        for s in submission:
            if ".jpg" in s.url or ".png" in s.url:
                urls.append(s.url)
        if not len(urls) is 0:
            break
    return random.choice(urls)
