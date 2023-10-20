# utility.py will handle all commands that require admin privelages
import discord
from discord.ext import commands

# Utility commands (changeprefix is still in prefix.py)
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
