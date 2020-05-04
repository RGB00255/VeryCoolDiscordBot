# PrefixHandler.py will handle everything related to prefixes
# Contains command changeprefix
import discord, json
from discord.ext import commands

# Commands class for changeprefix
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="changeprefix", help="Changes your server's prefix")
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, args):
        prefixes[str(ctx.guild.id)] = args
        WritePrefixJson(prefixes)
        await ctx.channel.send("Prefix changed to \"{p}\" very cool!".format(p=args))

# Loads all prefixes from prefixes.json
def LoadPrefixes():
    with open("data/prefixes.json") as f:
        prefixes = json.load(f)
    return prefixes

# Gets prefix that should be used on a specific server
def GetPrefix(bot, message, prefixes):
    default_prefix = "!"
    try:
        id = str(message.guild.id)
        if id not in prefixes: # If the server doesnt have a prefix defined already...
            prefixes[id] = default_prefix
            WritePrefixJson(prefixes) # ... write default prefix to prefixes.json
        return prefixes.get(id, default_prefix)
    except: # Must be a dm
        return default_prefix

# Writes prefixes dictionary to prefixes.json
def WritePrefixJson(prefixes):
    with open("data/prefixes.json", 'w') as f:
        json.dump(prefixes, f)

prefixes = LoadPrefixes()