# getmeme.py returns the url of a randomly picked post from selected subreddit, thanks stackoverflow for praw!!!
import asyncpraw, json, os, random
from asyncprawcore import NotFound

cfgLocation = "data/reddit/config.json"
srLocation = "data/reddit/subreddits/"

# Open and read in super secret api info so I can actually access reddit
with open(cfgLocation) as file:
    cfg = json.load(file)
    reddit = asyncpraw.Reddit(client_id=cfg["client_id"],
                     client_secret=cfg["secret_id"],
                     user_agent=cfg["user_agent"])

# Adds subreddit to server specific subreddits text file
def AddSubreddit(subreddit, id):
    if SubExists(subreddit):
        subreddits = LoadSubreddits(id)
        if subreddit not in subreddits:
            subreddits.append(subreddit)
            SaveSubreddits(subreddits, id)
            return True
    return False

# Used for "!meme <subreddit>"
def SubAdded(subreddit, id):
    if SubExists(subreddit):
        subreddits = LoadSubreddits(id)
        if subreddit in subreddits:
            return True
    return False

# Gets random url from selected subreddit
async def GetNewMeme(subreddit):
    meme_sr = await reddit.subreddit(subreddit)
    subList = []
    async for sub in meme_sr.hot():
        if sub.is_reddit_media_domain and sub.domain == "i.redd.it":
            subList.append(sub)
            #return sub
    return random.choice(subList)
        #submission = next(x for x in sub if x.is_reddit_media_domain and x.domain == "i.redd.it")

# Gets random subreddit from file
def GetRandomSubreddit(id):
    subreddits = LoadSubreddits(id)
    return random.choice(subreddits)

# Returns a list of subreddits in server's subreddits text file
def LoadSubreddits(id):
    fileLocation = srLocation + id + ".txt"
    if os.path.isfile(fileLocation):
        return [line.strip() for line in open(fileLocation)]
    else: # The file is going to start out with dankmemes
        if not os.path.isdir(srLocation): # If subreddits folder doesn't exist
            os.mkdir(srLocation)
        outFile = open(fileLocation, 'w')
        outFile.write("dankmemes")
        outFile.close()
        return [line.strip() for line in open(fileLocation)]

# Removes subreddit from server specific subreddit text file
def RemoveSubreddit(subreddit, id):
    subreddits = LoadSubreddits(id)
    if subreddit in subreddits:
        subreddits.remove(subreddit)
        SaveSubreddits(subreddits, id)
        return True
    return False

# Saves list of subreddits to server's subreddits text file
def SaveSubreddits(subreddits, id):
    with open(srLocation + id + ".txt", 'w') as outFile:
        outFile.write('\n'.join(sorted(subreddits, key=str.casefold)))

# Yoinked this from reddit, u/gavin19, note: thank the kind stranger at some point
def SubExists(subreddit):
    try:
        reddit.subreddits.search_by_name(subreddit, exact=True)
    except NotFound:
        return False
    return True