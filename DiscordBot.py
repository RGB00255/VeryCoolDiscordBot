# My first discord bot in python
# Commands: code, coomer, johnfreeman, iq, meme
__author__ = "Ryan Bergeron"

from discord.ext import commands
from reddit.GetMeme import GetNewMeme, GetRandomSubreddit
from PrefixHandler import WritePrefixJson
import discord, json, PrefixHandler, random

# Open and read in prefixes.json
prefixes = PrefixHandler.LoadPrefixes()
default_prefix = "!"

def prefix(bot, message):
    return PrefixHandler.GetPrefix(bot, message, prefixes)

#commandPrefix = "!"
bot = commands.Bot(command_prefix=prefix) # CHANGE TO ALLOW different server prefixes in future

@bot.event
async def on_ready(): # When the bot is ready to be used output to console
    print("Logged on as {0.user}!".format(bot))

@bot.command(name="changeprefix", help="Changes your server's prefix")
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, args):
    prefixes[str(ctx.guild.id)] = args
    WritePrefixJson(prefixes)

@bot.command(name="code", help="This is just a link for the bot's code")
async def code(ctx):
    await ctx.channel.send("https://github.com/RGB00255/VeryCoolDiscordBot")

@bot.command(name="coomer", help="This command will return a random Dr. Coomer quote. Very cool!")
async def coomer(ctx):
    coomerQuotes = [line.strip() for line in open("data/CoomerQuotes.txt")]
    await ctx.channel.send(random.choice(coomerQuotes) + " (Very cool)")

@bot.command(name="johnfreeman", help="You know what to do with this one")
async def johnfreeman(ctx):
    HLFLCQuotes = [line.strip() for line in open("data/HLFLC.txt")]
    await ctx.channel.send(random.choice(HLFLCQuotes) + " (Very cool)")

@bot.command(name="iq", help="Determine your iq")
async def iq(ctx):
    await ctx.channel.send("{a.author}, your iq is: {i}, very cool!".format(a=ctx, i=str(random.randrange(-1, 229))))

@bot.command(name="meme", help="Gets a random meme from a reddit meme subreddit")
async def meme(ctx):
    rdmSR = GetRandomSubreddit()
    meme = GetNewMeme(rdmSR)
    await ctx.channel.send("\"{a}\" \n{b} from r/{c}, very cool!".format(a=meme.title, b=meme.url, c=rdmSR))

# Attempt to read in the token from text file
try:
    f = open("token.txt", 'r')
    bot.run(f.read())
except:
    print("token.txt does not exist!")