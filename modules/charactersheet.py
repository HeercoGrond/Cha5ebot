import discord
from discord.ext import commands
import os 
import inspect
import json

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))[:-8] 

class CharacterSheetCog:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def charsheet(self, ctx):
        if ctx.guild != None:
            currentGuildPath =  "/guilds/" + str(ctx.guild.id)
            if not os.path.exists(currentPath + currentGuildPath):
                os.makedirs(currentPath + currentGuildPath)

            currentUserPath = currentGuildPath + "/user/" + str(ctx.author.id)
            if not os.path.exists(currentPath + currentUserPath):
                os.makedirs(currentPath + currentUserPath)
                print("Created charsheet folder for user " + str(ctx.author.id))

                with open("." + currentUserPath + "/charactersheet.json", 'w') as fp:
                    data = self.make_charsheet()
                    data["key"] = 'value'
                    json.dump(data, fp)
             
            with open("." + currentUserPath + "/charactersheet.json") as file:
                data = json.load(file)
                print(data)

                await ctx.send(data["key"])

    def make_charsheet(self):
        return {}

def setup(client):
    client.add_cog(CharacterSheetCog(client))