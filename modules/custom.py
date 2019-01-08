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
        await ctx.send("SNEAK ATTACK!\nEthearia rollt " + diceamount + " voor " + str(totaldmg[0]) + " damage.")

    @commands.command()
    async def fireball(self, ctx):
        enemies = randint(3, 65)
        leach = 12
        health = enemies * leach
        await ctx.send("FIREBALL!\nFreyja gooit een fireball op " + str(enemies) + " enemies en krijgt " + str(health) + " temporary hitpoints.")

    @commands.command()
    async def disappoint(self, ctx):
        disappointment = roll_dice("d20")
        await ctx.send(ctx.author.name + " is " + str(disappointment[0]) + " disappoint.\nShame on you, shame on your mother, shame on your cow.")

    @commands.command()
    async def narcian(self, ctx):
        await ctx.send("ICE KNIFE")

    @commands.command()
    async def throw(self, ctx, arg):
        distance = randint(1, 150)
        await ctx.send(ctx.author.name + " throws " + arg + " " + str(distance) + " feet away.\nYEEEEEEEEEEEEET!")

def setup(client):
    client.add_cog(Custom(client))