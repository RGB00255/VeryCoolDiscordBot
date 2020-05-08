#!/usr/bin/env python3
# My first discord bot in python
__author__ = "Ryan Bergeron"

from discord.ext import commands
from prefix import prefixes
import discord, dnd, fun, prefix, sound

# Function will determine server's prefix
def GetPrefix(bot, message):
    return prefix.GetPrefix(bot, message, prefixes)

# Set bot and commands
bot = commands.Bot(command_prefix=GetPrefix)
bot.add_cog(dnd.DnD(bot))
bot.add_cog(fun.Fun(bot))
bot.add_cog(prefix.Utility(bot))
bot.add_cog(sound.Sound(bot))

# When the bot is running, output to console
@bot.event
async def on_ready():
    print("Logged on as {0.user}!".format(bot))



# Attempt to read in the token from text file
try:
    f = open("token.txt", 'r')
    bot.run(f.read())
except:
    print("token.txt does not exist!")
    exit()