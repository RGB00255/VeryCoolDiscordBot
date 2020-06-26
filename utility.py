# utility.py will handle all commands that require admin privelages
import discord
from discord.ext import commands
from data.reddit.meme import AddSubreddit, RemoveSubreddit

# Utility commands (changeprefix is still in prefix.py)
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addsubreddit", help="Adds subreddit to list of subreddits")
    @commands.has_permissions(administrator=True)
    async def addsubreddit(self, ctx, args):
        if AddSubreddit(args):
            await ctx.channel.send("Subreddit added successfully")
        else:
            await ctx.channel.send("Subreddit not added")
    
    @commands.command(name="removesubreddit", help="Removes subreddit from list of subreddits")
    @commands.has_permissions(administrator=True)
    async def removesubreddit(self, ctx, args):
        if RemoveSubreddit(args):
            await ctx.channel.send("Subreddit removed successfully")
        else:
            await ctx.channel.send("Subreddit doesn't exist/isn't in subreddits.txt")