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
        if discord.utils.get(ctx.guild.roles, name="DM") in ctx.message.author.roles:
            with open('./modules/libraries/spells.json') as f:
                spell_data = json.load(f)
                for spell in spell_data:
                    if spell["name"].lower() == arg.lower():
                        spell_description = "Level " + spell["level"] + " " + spell["school"] + " spell."
                        embed_spell = discord.Embed(title=spell["name"], description=spell_description)

                        embed_spell.add_field(name="Duration", value=spell["duration"])

                        embed_spell.add_field(name="Casting Time", value=spell["casting_time"])

                        embed_spell.add_field(name="Components", value=spell["components"]["raw"])

                        embed_spell.add_field(name="Description", value=spell["description"])

                        if "higher_levels" in spell:
                            embed_spell.add_field(name="Higher Levels", value=spell["higher_levels"])

                        if spell["ritual"] == True:
                            embed_spell.add_field(name="Ritual", value="Yes")

                        await ctx.send(embed=embed_spell)
        else:
            await ctx.send("You don't have permission to use that command.")

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