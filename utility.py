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
        if AddSubreddit(args, str(ctx.guild.id)):
            await ctx.channel.send("Subreddit added successfully, very cool!")
        else:
            await ctx.channel.send("Subreddit not added, very uncool")
    
    @commands.command(name="removesubreddit", help="Removes subreddit from list of subreddits")
    @commands.has_permissions(administrator=True)
    async def removesubreddit(self, ctx, args):
        if RemoveSubreddit(args, str(ctx.guild.id)):
            await ctx.channel.send("Subreddit removed successfully, very cool!")
        else:
            await ctx.channel.send("Subreddit is not in the list of subreddits, very uncool")