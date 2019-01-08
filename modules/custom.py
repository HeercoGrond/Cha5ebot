from discord.ext import commands
import discord
from random import randint
from modules.libraries.roll import roll_dice

class Custom:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")
    
    @commands.command()
    async def lick(self, ctx, *, args):
        await ctx.send("Harkh likt " + args)

    @commands.command()
    async def sneakattack(self, ctx):
        diceamount = str(randint(3, 100)) + "d6"
        totaldmg = roll_dice(diceamount)
        await ctx.send("SNEAK ATTACK!" + /n + "Ethearia rollt " + diceamount + " voor " + totaldmg + " damage.")

def setup(client):
    client.add_cog(Custom(client))