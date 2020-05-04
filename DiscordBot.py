#!/usr/bin/env python3
# My first discord bot in python

# Commands: changeprefix, code, coomer, 
#   d4, d6, d8, d10, d20, d100,
#   johnfreeman, iq, meme
__author__ = "Ryan Bergeron"

from discord.ext import commands
from PrefixHandler import prefixes
import discord, DnD, Fun, json, PrefixHandler, random

# Open and read in prefixes.json
#prefixes = PrefixHandler.prefixes
default_prefix = "!"

def prefix(bot, message):
    return PrefixHandler.GetPrefix(bot, message, prefixes)

#commandPrefix = "!"
bot = commands.Bot(command_prefix=prefix) # CHANGE TO ALLOW different server prefixes in future
bot.add_cog(DnD.Commands(bot))
bot.add_cog(Fun.Commands(bot))
bot.add_cog(PrefixHandler.Commands(bot))

@bot.event
async def on_ready(): # When the bot is ready to be used output to console
    print("Logged on as {0.user}!".format(bot))

# Attempt to read in the token from text file
try:
    f = open("token.txt", 'r')
    bot.run(f.read())
except:
    print("token.txt does not exist!")
    exit()

