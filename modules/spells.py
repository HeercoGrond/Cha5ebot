from discord.ext import commands
from random import randint
import json
import sys
sys.path.append('./modules/libraries')
import roll

class Spells:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def spell(self, ctx, *, arg):
        with open('./modules/libraries/spell_library.json') as f:
            spell_data = json.load(f)
        await ctx.send(spell_data[arg])

    @commands.command()
    async def cast(self, ctx, *, arg):
        await ctx.send("Casting " + arg)
        with open('./modules/libraries/spell_library.json') as f:
            spell = json.load(f)

        # await ctx.send(">roll " + spell[arg]["damage"])
        
def setup(client):
    client.add_cog(Spells(client))