from discord.ext import commands
import discord
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
            for spell in spell_data:
                if spell["name"].lower() == arg.lower():
                    spell_description = "Level " + spell["level"] + " " + spell["school"] + " Spell."
                    embed_spell = discord.Embed(title=spell["name"], description=spell_description)

                    embed_spell.add_field(name="Duration", value=spell["duration"])

                    embed_spell.add_field(name="Components", value=spell["components"]["raw"])

                    embed_spell.add_field(name="Description", value=spell["description"])

                    await ctx.send(embed=embed_spell)

    @commands.command()
    async def cast(self, ctx, *, arg):
        await ctx.send("Casting " + arg)
        with open('./modules/libraries/spells.json') as f:
            spells = json.load(f)

            for spell in spells:
                if spell["name"].lower() == arg.lower():
                    dmg = spell["damage"]
                    message = roll_dice(dmg)
                    await ctx.send(message)

def setup(client):
    client.add_cog(Spells(client))