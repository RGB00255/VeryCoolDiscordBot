# sound.py handles everything related to sound
from discord.ext import commands
import discord, os

# Sound commands
class Sound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join", help="Get bot to join your voice channel")
    async def join(self, ctx):
        await ctx.channel.send("{c.message.author.mention}, please wait ~10 seconds before using the play command.".format(c=ctx))
        voice_channel = ctx.author.voice.channel
        
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(voice_channel)
        await voice_channel.connect()

    @commands.command(name="listsounds", help="Lists all available sounds")
    async def listsounds(self, ctx):
        await ctx.channel.send("Here's all of my very cool sounds I can play:\n```{a}```".format(a=", ".join(ListSoundFiles())))

    @commands.command(name="play", help="Plays a sound clip from the sounds folder")
    async def play(self, ctx, args):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("data/sounds/{}.mp3".format(args)))
        ctx.voice_client.play(source)

    @commands.command(name="stop", help="Stops and disconnects the bot from voice")
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

def ListSoundFiles():
    file_list=os.listdir("data/sounds")
    fixed_list=[x.split('.')[0] for x in file_list]
    return fixed_list