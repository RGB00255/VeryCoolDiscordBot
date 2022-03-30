# sound.py handles everything related to sound
from discord.ext import commands
import discord, os, youtube_dl
from youtube_dl.utils import DownloadError

# Sound commands
class Sound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Add support for server specific sound files and ability to remove them
    @commands.command(name="addsound", help="Adds a cool sound given a youtube link")
    @commands.has_permissions(administrator=True)
    async def addsound(self, ctx, url, fileName):
        if IsSupported(url):
            # Download and convert to mp3, move file
            if DownloadYoutubeMP3(url, fileName):
                await ctx.channel.send("Cool sound added by {c.message.author.mention}.".format(c=ctx))
            else:
                await ctx.channel.send("Epic download fail, {c.message.author.mention} loser.".format(c=ctx))
        else:
            await ctx.channel.send("Link not supported")
            return True

    @commands.command(name="join", help="Get bot to join your voice channel")
    async def join(self, ctx):
        await ctx.channel.send("I have been summoned at the request of {c.message.author.mention}.".format(c=ctx))
        voice_channel = ctx.author.voice.channel
        
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(voice_channel)
        await voice_channel.connect()

    @commands.command(name="listsounds", help="Lists all available sounds")
    async def listsounds(self, ctx):
        await ctx.channel.send("Here's all of my very cool sounds I can play:\n```{a}```".format(a=", ".join(GetSoundFiles())))

    @commands.command(name="play", help="Plays a sound clip from the sounds folder")
    async def play(self, ctx, args):
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("data/sounds/{}.mp3".format(args)))
        ctx.voice_client.play(source)

    @commands.command(name="stop", help="Stops and disconnects the bot from voice")
    async def stop(self, ctx):
        await ctx.voice_client.disconnect()

def DownloadYoutubeMP3(url, fileName):
    # Don't allow characters other than Aa-Zz, 0-9
    if not fileName.isalnum() and fileName not in GetSoundFiles():
        return False

    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'data/sounds/{0}.%(ext)s'.format(fileName),
        'noplaylist' : True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [my_hook],
    }

    # IsSupported() doesn't catch incomplete youtube urls
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except DownloadError:
        return False

def GetSoundFiles():
    file_list = os.listdir("data/sounds")
    fixed_list = [x.split('.')[0] for x in file_list]
    return fixed_list

# Credit to m8factorial on StackOverflow
def IsSupported(url):
    extractors = youtube_dl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(url) and e.IE_NAME != 'generic':
            return True
    return False
