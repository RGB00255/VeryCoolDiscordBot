# fun.py handles everything related to fun stuff
# Contains commands: code, coomer, johnfreeman, iq, meme
import discord, random
from discord.ext import commands
from data.reddit.meme import GetNewMeme, GetRandomSubreddit, LoadSubreddits, SubExists

# Fun commands
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="code", help="This is just a link for the bot's code")
    async def code(self, ctx):
        await ctx.channel.send("https://github.com/RGB00255/VeryCoolDiscordBot")
    
    @commands.command(name="coomer", help="This command will return a random Dr. Coomer quote. Very cool!")
    async def coomer(self, ctx):
        coomerQuotes = [line.strip() for line in open("data/CoomerQuotes.txt")]
        await ctx.channel.send(random.choice(coomerQuotes) + " (Very cool)")

    @commands.command(name="johnfreeman", help="You know what to do with this one")
    async def johnfreeman(self, ctx):
        HLFLCQuotes = [line.strip() for line in open("data/HLFLC.txt")]
        await ctx.channel.send(random.choice(HLFLCQuotes) + " (Very cool)")

    @commands.command(name="listsubreddits", help="Lists subreddits that can be chosen with !meme")
    async def listsubreddits(self, ctx):
        await ctx.channel.send("Here's a list of all the very cool subreddits I choose from:\n```{a}```".format(a=", ".join(LoadSubreddits(str(ctx.guild.id)))))

    @commands.command(name="iq", help="Determine your iq")
    async def iq(self, ctx):
        await ctx.channel.send("{c.message.author.mention}, your iq is: {i}, very cool!".format(c=ctx, i=str(random.randrange(-1, 229))))

    @commands.command(name="meme", help="Gets a random meme from a reddit meme subreddit unless specified")
    async def meme(self, ctx, args = None):
        if args is None: # Check if nothing was inputted
            rdmSR = GetRandomSubreddit(str(ctx.guild.id))
            meme = GetNewMeme(rdmSR)
            await ctx.channel.send("\"{a}\" \n{b} from r/{c}, very cool!".format(a=meme.title, b=meme.url, c=rdmSR))
        else:
            if SubExists(args):
                meme = GetNewMeme(args)
                await ctx.channel.send("\"{a}\" \n{b} from r/{c}, very cool!".format(a=meme.title, b=meme.url, c=args))
            else:
                await ctx.channel.send("Subreddit is not in the list of subreddits, very uncool")