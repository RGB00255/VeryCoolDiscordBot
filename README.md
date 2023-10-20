# VeryCoolDiscordBot
This is the code I use for "Ryan's Very Cool Bot"

This is my first bot for Discord, it is a WIP as I learn more about making bots.

discord.py documentation: https://discordpy.readthedocs.io/en/latest/index.html

# Requirements:
  For the meme command to work you need to have a Reddit account. Create an app and put your "client_id", "secret_id", and "user_agent" in data/reddit/config.json. 

  config.json is in this format:
    
    {
      "client_id":"",
      "secret_id":"",
      "user_agent":""
    }

  Create token.txt, place only your bot token in it with no whitespace.
  
  Run "pip3 install -r requirements.txt" to install all the python requirements.

  Other required packages:

    ffmpeg

# Features:
  
  So far, this bot's main uses are: doing a basic roll in DnD, posting random memes from random, server specified subreddits, and playing sounds through voice channels (not really a defining feature, but it's there so w/e). 

  Below are the commands this bot can do.

  DnD:
  
    roll <XdY[+Z]> - Rolls a dice of Y sides X times (i.e. !roll 3d4 "<user>, here's your roll: 4 + 3 + 2 = 9")
    
  Fun:
  
    code - Displays a link to this github repo
    coomer - Displays a random Dr. Coomer quote from the "HLVR but the AI is self-aware" series
    johnfreeman - Displays a random line from the "Halflife: Fulllife Consequences" fan fiction
    listsubreddits - Lists subreddits that can be chosen with !meme
    iq - Gives you your iq (generates a random number from -1 - 228)
    
   Sound:
 
    addsound - Adds a cool sound given a youtube link and sound name (!addsound <youtube link> <sound name>) sound name is alphanumeric
    join - Get bot to join your voice channel
    listsounds - Lists all available sounds
    play - Plays a sound clip from the sounds folder
    stop - Stops and disconnects the bot from voice
  
  Utility:
  
    Nothing as of yet.