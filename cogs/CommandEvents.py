from discord.ext import commands
from datetime import datetime
from utils.database import cluster


def updateXp(user, guildId, value):
    db = cluster[str(guildId)]
    col = db["UserData"]

    col.update({
        "_id": user.id,
        "name": user.name
    }, {
        '$inc': {"xp": value}
    },
        upsert=True)

    print(col.find_one({"_id": user.id}))


class CommandEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

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

    @commands.Cog.listener()
    async def on_message(self, message):
        ctx = await self.client.get_context(message)
        if ctx.valid:
            return
        else:
            if message.author.id != self.client.user.id:
                updateXp(message.author, message.guild.id, 10)


def setup(client):
    client.add_cog(CommandEvents(client))
