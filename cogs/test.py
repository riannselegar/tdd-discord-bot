import discord
from discord.ext import commands
from datetime import datetime


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Listening... {self.client.user}")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None or after.channel is None:
            print("O usuário {user} {acao} {servidor} às {hora}".format(
                user=member,
                acao="saiu do" if after.channel is None else "entrou no",
                servidor=before.channel.guild if after.channel is None else after.channel.guild,
                hora=datetime.now().strftime("%H:%M:%S")))

    # Commands
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello")


def setup(client):
    client.add_cog(Test(client))
