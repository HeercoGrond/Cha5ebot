from discord.ext import commands
from random import randint
import json

class Spells:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def spell(self, ctx, arguments):
        print(arguments)

    @commands.command()
    async def cast(self, ctx, arguments):
        await ctx.send("Casting " + arguments)
        
def setup(client):
    client.add_cog(Spells(client))