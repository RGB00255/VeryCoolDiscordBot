# GetMeme.py returns the url of a randomly picked post from selected subreddit, thanks stackoverflow for praw!!!
import praw, random, json

with open("reddit/config.json") as file:
    cfg = json.load(file)
    reddit = praw.Reddit(client_id=cfg["client_id"],
                     client_secret=cfg["secret_id"],
                     user_agent=cfg["user_agent"])

# Gets random url from selected subreddit
def GetNewMeme(subreddit):
    memes_submissions = reddit.subreddit(subreddit).hot()
    post_to_pick = random.randint(1, 50)
    for _ in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied and not x.is_video and not x.is_self)
    return submission

# Gets random subreddit from file
def GetRandomSubreddit():
    subreddits = [line.strip() for line in open("data/subreddits.txt")]
    return random.choice(subreddits)