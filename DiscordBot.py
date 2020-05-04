#!/usr/bin/env python3
# My first discord bot in python
__author__ = "Ryan Bergeron"

from discord.ext import commands
from PrefixHandler import prefixes
import discord, DnD, Fun, json, PrefixHandler, random

# Open and read in prefixes.json
#prefixes = PrefixHandler.prefixes
default_prefix = "!"

# Function will determine server's prefix
def prefix(bot, message):
    return PrefixHandler.GetPrefix(bot, message, prefixes)

# Set bot and commands
bot = commands.Bot(command_prefix=prefix)
bot.add_cog(DnD.Commands(bot))
bot.add_cog(Fun.Commands(bot))
bot.add_cog(PrefixHandler.Commands(bot))

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

