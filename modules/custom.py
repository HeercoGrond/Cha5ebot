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
        await ctx.send("SNEAK ATTACK!\nEthearia rollt %s voor %s damage." % (diceamount, totaldmg[0]))

    @commands.command()
    async def fireball(self, ctx):
        enemies = randint(3, 65)
        leach = 12
        health = enemies * leach
        await ctx.send("FIREBALL!\nFreyja gooit een fireball op %s enemies en krijgt %s temporary hitpoints." % (enemies, health))

    @commands.command()
    async def disappoint(self, ctx):
        disappointment = roll_dice("d20")
        await ctx.send(ctx.author.name + " is %s disappoint.\nShame on you, shame on your mother, shame on your cow." % (disappointment[0]))

    @commands.command()
    async def narcian(self, ctx):
        await ctx.send("ICE KNIFE")

    @commands.command()
    async def throw(self, ctx, arg):
        distance = randint(1, 150)
        await ctx.send(ctx.author.name + " throws %s %s feet away.\nYEEEEEEEEEEEEET!" % (arg, distance))

def setup(client):
    client.add_cog(Custom(client))