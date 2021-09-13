import os
import discord
from datetime import datetime

client = discord.Client()
token = os.environ['TOKEN']


@client.event
async def on_ready():
    print("Logged in. Listening... {0.user}".format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('$hello'):
        await msg.channel.send("Hello novo!")


@client.event
async def on_typing(channel, user, when):
    print(channel, user, when)


@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None or after.channel is None:
        print("O usuário {user} {acao} {servidor} às {hora}"
              .format(
                user=member,
                acao="saiu do" if after.channel is None else "entrou no",
                servidor=before.channel.guild if after.channel is None else after.channel.guild,
                hora=datetime.now().strftime("%H:%M:%S")))


client.run(token)
