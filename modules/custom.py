from discord.ext import commands
import discord
from random import randint
import random
import datetime
import json
from modules.libraries.roll import roll_dice

class Custom:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")
    
    @commands.command()
    async def lik(self, ctx, *, args):
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
        await ctx.send("_Ik heb superior darkvision..._")

    @commands.command()
    async def throw(self, ctx, arg):
        distance = randint(1, 150)
        await ctx.send(ctx.author.name + " throws %s %s feet away.\nYEEEEEEEEEEEEET!" % (arg, distance))

    @commands.command()
    async def toot(self, ctx):
        await ctx.send("**TÚÚÚÚÚÚÚÚÚÚT!**")

    @commands.command()
    async def woordspreek(self, ctx):
        await ctx.send("**WOORDPSREEEEEEEK. HEUY HEUY HEUY HEUY.**")

    @commands.command()
    async def woensdag(self, ctx):
        today = datetime.datetime.today().weekday()
        if today == 2:
            await ctx.send("It is wednesday, my dudes! :tada:")
        else:
            await ctx.send("It is not wednesday, my dudes!")

    @commands.command()
    async def tijd(self, ctx):
        dice = randint(2, 50)
        total = 0
        for x in range(1, dice):
            outcome = randint(1, 4)
            total += outcome
        await ctx.send("Harkh vraagt zich af wat tijd is en krijgt %s psychic damage." % (total))

    @commands.command()
    async def snowball(self, ctx):
        colors = ["rode", "blauwe", "groene", "gele",
                  "paarse", "zwarte", "cyane", "regenboog kleurige"]
        choice = randint(0, len(colors))
        hit = randint(1, 20)
        await ctx.send("Stoz gooit een %s sneeuwbal naar je, %s to hit." % (colors[choice], hit))

    @commands.command()
    async def pannekoek(self, ctx):
        await ctx.send("Ik heb een boek!")

    @commands.command()
    async def polymorph(self, ctx):
        with open("./modules/libraries/polymorph.json") as f:
            polymorph = json.load(f)
            animal = random.choice(polymorph)
            await ctx.send("Leander cast polymorph en verandert in een %s." % (animal))

    @commands.command()
    async def metabird(self, ctx):
        await ctx.send("KAH KAH _poof_ It gone")

    @commands.command()
    async def watdoejehier(self, ctx):
        await ctx.send("HEY, WAT DOE JE HIER?!")

def setup(client):
    client.add_cog(Custom(client))