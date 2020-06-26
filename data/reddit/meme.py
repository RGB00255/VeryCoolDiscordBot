# getmeme.py returns the url of a randomly picked post from selected subreddit, thanks stackoverflow for praw!!!
import praw, random, json
from prawcore import NotFound

cfgLocation = "data/reddit/config.json"
srLocation = "data/reddit/subreddits.txt"

# Open and read in super secret api info so I can actually access reddit
with open(cfgLocation) as file:
    cfg = json.load(file)
    reddit = praw.Reddit(client_id=cfg["client_id"],
                     client_secret=cfg["secret_id"],
                     user_agent=cfg["user_agent"])

# Adds subreddit to subreddits.txt
# In the future, add support for server specific setups
def AddSubreddit(subreddit):
    if SubExists(subreddit):
        subreddits = LoadSubreddits()
        if subreddit not in subreddits:
            subreddits.append(subreddit)
            SaveSubreddits(subreddits)
            return True
    return False

# Gets random url from selected subreddit
def GetNewMeme(subreddit):
    memes_submissions = reddit.subreddit(subreddit).hot()
    post_to_pick = random.randint(1, 50)
    for _ in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied and not x.is_video and not x.is_self)
    return submission

# Gets random subreddit from file
def GetRandomSubreddit():
    subreddits = LoadSubreddits()
    return random.choice(subreddits)

# Returns a list of subreddits in subreddits.txt
def LoadSubreddits():
    return [line.strip() for line in open(srLocation)]

# Saves list of subreddits to subreddits.txt
def SaveSubreddits(subreddits):
    with open(srLocation, 'w') as outFile:
        outFile.write('\n'.join(sorted(subreddits)))

# Removes subreddit from subreddits.txt
# In the future, add support for server specific setups
def RemoveSubreddit(subreddit):
    subreddits = LoadSubreddits()
    if subreddit in subreddits:
        subreddits.remove(subreddit)
        SaveSubreddits(subreddits)
        return True
    return False

# Yoinked this from reddit, u/gavin19, note: thank the kind stranger at some point
def SubExists(subreddit):
    exists = True
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except NotFound:
        exists = False
    return exists