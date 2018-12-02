from discord.ext import commands
from random import randint

class Spells:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def spell(self, ctx, arguments):
        print(arguments)
        
def setup(client):
    client.add_cog(Spells(client))