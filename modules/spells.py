from discord.ext import commands
from random import randint
import json
from modules.libraries.roll import roll_dice

class Spells:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def spell(self, ctx, *, arg):
        with open('./modules/libraries/spells.json') as f:
            spell_data = json.load(f)
        await ctx.send(spell_data[arg])

    @commands.command()
    async def cast(self, ctx, *, arg):
        await ctx.send("Casting " + arg)
        hit = roll_dice("d20")
        await ctx.send("Rolled " + hit + " + spellcasting mod to hit!")
        # if hit + spellcasting mod <= enemy AC, then continue casting. Else half damage or miss.

        with open('./modules/libraries/spells.json') as f:
            spells = json.load(f)

            for spell in spells:
                if spell["name"].lower() == arg.lower():
                    dmg = spell["damage"]
                    message = roll_dice(dmg)
                    await ctx.send(message)

def setup(client):
    client.add_cog(Spells(client))