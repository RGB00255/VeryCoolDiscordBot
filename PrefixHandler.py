# PrefixHandler.py will handle everything related to prefix.json
import json

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