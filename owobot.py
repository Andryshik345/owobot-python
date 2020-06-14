# -*- coding: utf-8 -*-

import random
import praw, boards

# Limits maximum posts count
limit = 6

def Session(client_id, client_secret, user_agent):
    global session
    session = praw.Reddit(client_id=client_id,
                          client_secret=client_secret,
                          user_agent=user_agent)

def GetPicSFW():
    if session:
        subreddit = session.subreddit(boards.SFW[random.randrange(len(boards.SFW) + 1)])

        submission = subreddit.new(limit=limit)
        for s in submission:
            if ".jpg" in s.url or ".png" in s.url:
                return s.url
                break
            else:
                continue
    else:
        return False
            
def GetPicNSFW():
    if session:
        subreddit = session.subreddit(boards.NSFW[random.randrange(len(boards.NSFW) + 1)])

        submission = subreddit.new(limit=limit)
        for s in submission:
            if ".jpg" in s.url or ".png" in s.url:
                return s.url
                break
            else:
                continue
    else:
        return False
