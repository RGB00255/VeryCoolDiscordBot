# dnd.py will handle anything DnD related
# Contains commands: d4, d6, d8, d10, d20, d100, roll
import discord, random, re
from discord.ext import commands

# DnD Commands
class DnD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll", help="Roll XdY[+Z]")
    async def roll(self, ctx, args):
        await ctx.channel.send("{c.message.author.mention}, here's your roll: {r}".format(c=ctx, r=dRoll(args)))

# Roll just generates a random number given the range
def Roll(die):
    return random.randrange(1, die + 1)

# Does a roll given a value like 3d4
def dRoll(roll):
    #rollList = roll.split("d")
    rollList = re.split(r'[d+]+', roll)
    returnString = ""
    total = 0

    if rollList[0] == "1":
        total = Roll(int(rollList[1]))
        returnString += str(total)
    elif int(rollList[0]) > 0:
        for i in range(1, int(rollList[0]) + 1):
            tempRoll = Roll(int(rollList[1]))
            total += tempRoll

            if i == int(rollList[0]): # If i is on its last run, finialize returnString
                returnString += str(tempRoll) + " = " + str(total)
            else: # What normally executes
                returnString += str(tempRoll) + " + "
    if len(rollList) == 3: # If + was in string
        total += int(rollList[2])
        return returnString + " + {s} = {t}, very cool!".format(s=rollList[2], t=total)
    if total == 1: # New return string if total sucks
        return returnString + ", very cool?"
    if total >= int(rollList[1]): # If rolled highest possible
        return returnString + ", very very cool!"
    return returnString + ", very cool!"