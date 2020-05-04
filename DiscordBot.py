#!/usr/bin/env python3
# My first discord bot in python

# Commands: changeprefix, code, coomer, 
#   d4, d6, d8, d10, d20, d100,
#   johnfreeman, iq, meme
__author__ = "Ryan Bergeron"

from discord.ext import commands
from reddit.GetMeme import GetNewMeme, GetRandomSubreddit
from PrefixHandler import WritePrefixJson
import discord, json, PrefixHandler, random, DnD

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
    await ctx.channel.send("Prefix changed to \"{p}\" very cool!".format(p=args))

@bot.command(name="code", help="This is just a link for the bot's code")
async def code(ctx):
    await ctx.channel.send("https://github.com/RGB00255/VeryCoolDiscordBot")

@bot.command(name="coomer", help="This command will return a random Dr. Coomer quote. Very cool!")
async def coomer(ctx):
    coomerQuotes = [line.strip() for line in open("data/CoomerQuotes.txt")]
    await ctx.channel.send(random.choice(coomerQuotes) + " (Very cool)")

@bot.command(name="d4", help="Roll a d4")
async def d4(ctx):
    await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=DnD.Roll(4)))

@bot.command(name="d6", help="Roll a d6")
async def d6(ctx):
    await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=DnD.Roll(6)))

@bot.command(name="d8", help="Roll a d8")
async def d8(ctx):
    await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=DnD.Roll(8)))

@bot.command(name="d10", help="Roll a d10")
async def d10(ctx):
    await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=DnD.Roll(10)))

@bot.command(name="d20", help="Roll a d20")
async def d20(ctx):
    await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=DnD.Roll(20)))

@bot.command(name="d100", help="Roll a d100")
async def d100(ctx):
    await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=DnD.Roll(100)))

@bot.command(name="johnfreeman", help="You know what to do with this one")
async def johnfreeman(ctx):
    HLFLCQuotes = [line.strip() for line in open("data/HLFLC.txt")]
    await ctx.channel.send(random.choice(HLFLCQuotes) + " (Very cool)")

@bot.command(name="iq", help="Determine your iq")
async def iq(ctx):
    await ctx.channel.send("{c.author}, your iq is: {i}, very cool!".format(c=ctx, i=str(random.randrange(-1, 229))))

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