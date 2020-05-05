# DnD.py will handle anything DnD related
# Contains commands: d4, d6, d8, d10, d20, d100, roll
import discord, random, re
from discord.ext import commands

# DnD Commands
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll", help="Roll XdY")
    async def roll(self, ctx, args):
        await ctx.channel.send("{c.message.author.mention}, here's your roll: {r}".format(c=ctx, r=dRoll(args)))

# Roll just generates a random number given the range
def Roll(die):
    return random.randrange(1, die + 1)

# Does a roll given a value like 3d4
def dRoll(roll):
    rollList = roll.split("d")
    returnString = ""
    total = 0

    if rollList[0] == "1":
        returnString += str(Roll(int(rollList[1])))
    elif int(rollList[0]) > 0:
        for i in range(1, int(rollList[0]) + 1):
            tempRoll = Roll(int(rollList[1]))
            total += tempRoll

            if i == int(rollList[0]): # If I is on its last run, finialize returnString
                returnString += str(tempRoll) + " = " + str(total)
            else: # What normally executes
                returnString += str(tempRoll) + " + "
    return returnString