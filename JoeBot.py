import discord
from discord.ext import commands
import secrets

import music

cogs = [music]

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

for i in range(len(cogs)):
    cogs[i].setup(client)
    print("its alive")



token = secrets.discord_bot_auth_token
client.run(token)
print("Starting")