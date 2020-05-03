import json

def LoadPrefixes():
    with open("data/prefixes.json") as f:
        prefixes = json.load(f)
    return prefixes

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

def WritePrefixJson(prefixes):
    with open("data/prefixes.json", 'w') as f:
        json.dump(prefixes, f)