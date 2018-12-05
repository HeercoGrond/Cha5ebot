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
        with open('./libraries/spell_library.json') as f:
            spell_data = json.load(f)
        await ctx.send(spell_data[arguments])

    @commands.command()
    async def cast(self, ctx, *, arg):
        await ctx.send("Casting " + arg)
        
def setup(client):
    client.add_cog(Spells(client))