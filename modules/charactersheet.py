import discord
from discord.ext import commands
import os 
import inspect

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))[:-8] 

class CharacterSheet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def charsheet(self, ctx):
        if ctx.guild != None:
            currentGuildPath = currentPath + "/guilds/" + str(ctx.guild.id)
            print(currentGuildPath)

            if not os.path.exists(currentGuildPath):
                os.makedirs(currentGuildPath)

            currentUserPath = currentGuildPath + "/user/" + str(ctx.author.id)
            if not os.path.exists(currentUserPath):
                os.makedirs(currentUserPath)
                print("Created charsheet folder for user " + str(ctx.author.id))

def setup(client):
    client.add_cog(CharacterSheet(client))