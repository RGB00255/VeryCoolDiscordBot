#!/usr/bin/env python3
# My first discord bot in python
__author__ = "Ryan Bergeron"

from discord.ext import commands
from prefix import prefixes
import discord, dnd, fun, prefix, sound, utility

# Function will determine server's prefix
def GetPrefix(bot, message):
    return prefix.GetPrefix(bot, message, prefixes)

# Set bot and commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=GetPrefix, intents=intents)
async def setup(bot):
    await bot.add_cog(dnd.DnD(bot))
    await bot.add_cog(fun.Fun(bot))
    await bot.add_cog(prefix.Prefix(bot))
    await bot.add_cog(sound.Sound(bot))
    await bot.add_cog(utility.Utility(bot))

# When the bot is running, output to console and set activity
@bot.event
async def on_ready():
    print("Logged on as {0.user}!".format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep, very cool!"))
    await setup(bot)

# Attempt to read in the token from text file
try:
    f = open("token.txt", 'r')
    bot.run(f.read())
except:
    print("token.txt does not exist!")
    exit()