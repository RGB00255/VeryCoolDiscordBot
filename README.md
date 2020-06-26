# VeryCoolDiscordBot
This is the code I use for "Ryan's Very Cool Bot"

This is my first bot for Discord, it is a WIP as I learn more about making bots.

discord.py documentation: https://discordpy.readthedocs.io/en/latest/index.html

# Requirements:
  Run "pip3 install -r requirements.txt" to install all the requirements installable from pip3

  Other required packages:

    ffmpeg

# Features:
   
  DnD:
  
    roll <XdY[+Z]> - Rolls a dice of Y sides X times (i.e. !roll 3d4 "<user>, here's your roll: 4 + 3 + 2 = 9")
    
  Fun:
  
    code - Displays a link to this github repo
    coomer - Displays a random Dr. Coomer quote from the "HLVR but the AI is self-aware" series
    johnfreeman - Displays a random line from the "Halflife: Fulllife Consequences" fan fiction
    listsubreddits - Lists subreddits that can be chosen with !meme
    iq - Gives you your iq (generates a random number from -1 - 228)
    meme - Displays a random meme from a random subreddit defined in subreddits.txt
    
   Sound:
 
    join - Get bot to join your voice channel
    listsounds - Lists all available sounds
    play - Plays a sound clip from the sounds folder
    stop - Stops and disconnects the bot from voice
  
  Utility:
  
    addsubreddit - Adds subreddit to list of subreddits
    changeprefix - Changes the prefix for your server
    removesubreddit - Removes subreddit from list of subreddits