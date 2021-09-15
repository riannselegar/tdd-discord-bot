import os
import discord

client = discord.Client()
token = os.environ['TOKEN']


@client.event
async def on_ready():
    print("Logged in. Listening... {0.user}".format(client))

client.run(token)
