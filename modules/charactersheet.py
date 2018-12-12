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
    async def charsheet(self, ctx, argument, arguments=""):
        if ctx.guild != None:
            # Variables
            currentGuildPath =  "/guilds/" + str(ctx.guild.id)
            currentUserPath = currentGuildPath + "/user/" + str(ctx.author.id)
            filename = arguments.replace(argument, "")
            filepath = "." + currentUserPath + "/" + filename + ".json"

            if argument == "make":
                if not os.path.exists("." + currentGuildPath):
                    os.makedirs("." + currentGuildPath)
                    print("This path doesn't exist")

                if not os.path.exists("." + currentUserPath):
                    os.makedirs("." + currentUserPath)
                    print("Created charsheet folder for user " + str(ctx.author.id))

                if not os.path.exists("." + currentUserPath + "/" + filename + ".json"):
                    with open("." + currentUserPath + "/" + filename + ".json", 'w') as fp:
                        data = self.make_charsheet(filename, ctx.guild.id, ctx.author.id)
                        json.dump(data, fp, indent=4, sort_keys=True)
                        await ctx.send("Created charactersheet with the name: " + data["name"])
                else:
                    await ctx.send("A charactersheet with the name '" + filename + "' was already found.")

            elif argument == "rename":
                args = filename.split()

                if len(args) != 2:
                    await ctx.send("There were either less or more than 2 arguments into the command. Proper usage is `>charactersheet rename {x} {y}` where {x} is the existing sheetname and {y} is the new sheetname.")

                else: 
                    renamePath = "." + currentUserPath + "/" + args[0] + ".json"
                    newPath = "." + currentUserPath + "/" + args[1] + ".json"

                    if os.path.exists(renamePath):
                        with open(renamePath, 'w') as file:
                            data = json.load(file)
                            data["name"] = args[1]
                            json.dump(data, fp, indent=4, sort_keys=True)
                            os.rename(renamePath, newPath) 
                    
                    else:
                        await ctx.send("The sheet requested doesn't exist.")

            elif argument == "delete":
                path = "." + currentUserPath + "/" + filename + ".json"
                if os.path.exists(path):
                    os.remove(path)
                    await ctx.send("Succesfully deleted charactersheet '" + filename + "'.")
                else:
                    await ctx.send("The charactersheet you are trying to delete doesn't seem to exist.")

            elif argument == "list":
                with os.scandir("." + currentUserPath + "/") as sheets:
                    
                    description = "" 
                    for file in sheets:
                        description += file.name.replace(".json", "") + "\n"

                    embed_totalsheets = discord.Embed(title="Your sheets:", description=description)
                    await ctx.send(embed=embed_totalsheets)

            elif arguments == "":
                with open("." + currentUserPath + "/" + argument + ".json") as file:
                    data = json.load(file)

                    embed_sheet = discord.Embed(title=data["name"])

                    await ctx.send("Found charactersheet with the name: " + data["name"])

    def make_charsheet(self, sheetname, guild_id, user_id):
        charactersheet = {}

        charactersheet["name"] = sheetname
        charactersheet["guild_id"] = guild_id
        charactersheet["user_id"] = user_id

        charactersheet["class"] = "undefined"
        charactersheet["level"] = 1
        charactersheet["avatar_image"] = ""

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