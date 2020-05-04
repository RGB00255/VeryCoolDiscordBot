# DnD.py will handle anything DnD related
# Contains commands: d4, d6, d8, d10, d20, d100, roll
import random, discord
from discord.ext import commands

# DnD Commands
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="d4", help="Roll a d4")
    async def d4(self, ctx):
        await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=Roll(4)))

    @commands.command(name="d6", help="Roll a d6")
    async def d6(self, ctx):
        await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=Roll(6)))

    @commands.command(name="d8", help="Roll a d8")
    async def d8(self, ctx):
        await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=Roll(8)))

    @commands.command(name="d10", help="Roll a d10")
    async def d10(self, ctx):
        await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=Roll(10)))

    @commands.command(name="d20", help="Roll a d20")
    async def d20(self, ctx):
        await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=Roll(20)))

    @commands.command(name="d100", help="Roll a d100")
    async def d100(self, ctx):
        await ctx.channel.send("{c.author} rolled a {r}".format(c=ctx,r=Roll(100)))

    @commands.command(name="roll", help="Roll XdY")
    async def roll(self, ctx, args):
        await ctx.channel.send("Not implemented yet. Here's ur arg tho: {a}".format(a=args))

# Roll just generates a random number given the range
def Roll(die):
    return random.randrange(1, die + 1)