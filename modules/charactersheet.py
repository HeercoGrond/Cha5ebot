import discord
from discord.ext import commands
from enum import Enum
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
    async def charsheet(self, ctx, argument):
        if ctx.guild != None:
            currentGuildPath =  "/guilds/" + str(ctx.guild.id)
            if not os.path.exists("." + currentGuildPath):
                os.makedirs("." + currentGuildPath)
                print("This path doesn't exist")

            currentUserPath = currentGuildPath + "/user/" + str(ctx.author.id)
            if not os.path.exists("." + currentUserPath):
                os.makedirs("." + currentUserPath)
                print("Created charsheet folder for user " + str(ctx.author.id))

            if not os.path.exists("." + currentUserPath + "/" + argument + ".json"):
                with open("." + currentUserPath + "/" + argument + ".json", 'w') as fp:
                    data = self.make_charsheet(argument, ctx.guild.id, ctx.author.id)
                    json.dump(data, fp)
                    await ctx.send("Found charactersheet with the name: " + data["name"])
             
            # with open("." + currentUserPath + "/" + argument + ".json") as file:
            #     data = json.load(file)
            #     await ctx.send("Found charactersheet with the name: " + data["name"])

    def make_charsheet(self, sheetname, guild_id, user_id):
        charactersheet = {}

        charactersheet["name"] = sheetname
        charactersheet["guild_id"] = guild_id
        charactersheet["user_id"] = user_id

        charactersheet["class"] = "undefined"
        charactersheet["level"] = 1

        charactersheet["attributes"] = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

        charactersheet["saving_throws"] = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }

        charactersheet["skills"] = {
            "athletics": 0,
            "acrobatics": 0,
            "sleight_of_hand": 0,
            "stealth": 0,
            "arcana": 0,
            "history": 0,
            "investigation": 0,
            "nature": 0,
            "religion": 0,
            "animal_handling": 0,
            "insight": 0,
            "medicine": 0,
            "perception": 0,
            "survival": 0,
            "deception": 0,
            "intimidation": 0,
            "performance": 0,
            "persuasion": 0
        } 

        charactersheet["equipment"] = {}
        charactersheet["actions"] = {}
        charactersheet["spellbook"] = {}

        return charactersheet



def setup(client):
    client.add_cog(CharacterSheetCog(client))