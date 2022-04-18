import discord
from discord.ext import commands
import music
cogs = [music]
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
discord.Intents.all()
for i in range(len(cogs)):
    cogs[i].setup(client)
client.run("OTY1NzA0MDg2NjA1NDE0NDAx.Yl3EBA.UYWXHmd75rGOW2jXRmVsVn-R_uY")