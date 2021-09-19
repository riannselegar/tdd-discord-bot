from discord.ext import commands
from utils.database import cluster


class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(ctx.guild.id)


def setup(client):
    client.add_cog(Greetings(client))
