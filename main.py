import os
import discord

client = discord.Client()
token = os.environ['TOKEN']


@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  
  if msg.content.startswith('$hello'):
    await msg.channel.send("Hello!")

client.run(token)