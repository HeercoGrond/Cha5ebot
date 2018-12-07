from discord.ext import commands
from random import randint
import json
from modules.libraries.roll import roll_dice

class Attack:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def attack(self, ctx, *, arg):
        with open('./modules/libraries/weapons.json') as f:
            weapons = json.load(f)
            hit = roll_dice("d20")
            await ctx.send("Attacking with " + arg + " for " + hit + " + attack mod to hit!")

            for weapon in weapons:
                if weapon["name"].lower() == arg.lower():
                    dmg = roll_dice(weapon["damage"])
                    await ctx.send("Doing " + dmg + " (+ dmg mod) damage!")

def setup(client):
    client.add_cog(Attack(client))