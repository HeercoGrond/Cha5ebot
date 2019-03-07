import discord
from discord.ext import commands
from enum import Enum
import os 
import inspect
import json

currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))[:-8] 

class CharacterSheet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def charsheet(self, ctx, *args):
        if ctx.guild != None:
            # Variables
            currentGuildPath =  "/guilds/" + str(ctx.guild.id)
            currentUserPath = currentGuildPath + "/user/" + str(ctx.author.id)
            argumentCount = len(args)

            print(args)

            if(argumentCount == 0):
                await ctx.send("No arguments were provided, please make sure to provide an argument to the command.")

            else:
                argument = args[0]

                if argument == "make":
                    if argumentCount != 2:
                        await ctx.send("There was either less or more than 1 argument into the command. Proper usage is `>charactersheet make {x}` where {x} is the new character sheet's name. This name can be changed later.")
                    
                    else:
                        filename = args[1]
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
                    if argumentCount != 3:
                        await ctx.send("There were either less or more than 2 arguments into the command. Proper usage is `>charactersheet rename {x} {y}` where {x} is the existing sheetname and {y} is the new sheetname.")

                    else: 
                        renamePath = "." + currentUserPath + "/" + args[1] + ".json"
                        newPath = "." + currentUserPath + "/" + args[2] + ".json"

                        if os.path.exists(renamePath):
                            with open(renamePath) as file:
                                data = json.load(file)
                                data["name"] = args[2]
                                json.dump(data, fp, indent=4, sort_keys=True)
                                os.rename(renamePath, newPath) 
                        
                        else:
                            await ctx.send("The sheet requested doesn't exist.")

                elif argument == "delete":
                    if argumentCount != 2:
                        await ctx.send("There was either less or more than 1 argument into the command. Proper usage is `>charactersheet delete {x}` where {x} is the character sheet's name that will be deleted.")

                    else:
                        path = "." + currentUserPath + "/" + filename + ".json"
                        if os.path.exists(path):
                            os.remove(path)
                            await ctx.send("Succesfully deleted charactersheet '" + filename + "'.")
                        else:
                            await ctx.send("The charactersheet you are trying to delete doesn't seem to exist.")

                elif argument == "list":
                    userpath = ""
                    username = "" 
                    if argumentCount == 2:
                        userid = args[1].replace('<@', "").replace('>', "")
                        userpath = currentGuildPath + "/user/" + userid

                        user = ctx.guild.get_member(int(userid))
                        username = user.display_name
                    else:
                        userpath = currentUserPath
                        username = ctx.author.display_name 

                    with os.scandir("." + userpath + "/") as sheets:
                        description = "" 
                        for file in sheets:
                            description += file.name.replace(".json", "") + "\n"

                        embed_totalsheets = discord.Embed(title="%s's sheets:" % username, description=description)
                        await ctx.send(embed=embed_totalsheets)

                elif argumentCount != 0:
                    filepath = "." + currentUserPath + "/" + argument + ".json"
                    if os.path.exists(filepath):
                        with open("." + currentUserPath + "/" + argument + ".json") as file:
                            data = json.load(file)

                            embed_sheet = discord.Embed(title=data["name"])

                            attributes = ""
                            attributes += "**Strength:**\t" + str(data["attributes"]["strength"]) + "\n"
                            attributes += "**Dexterity:**\t" + str(data["attributes"]["dexterity"]) + "\n"
                            attributes += "**Constitution:**\t" + str(data["attributes"]["constitution"]) + "\n"
                            attributes += "**Intelligence:**\t" + str(data["attributes"]["intelligence"]) + "\n"
                            attributes += "**Wisdom:**\t" + str(data["attributes"]["wisdom"]) + "\n"
                            attributes += "**Charisma:**\t" + str(data["attributes"]["charisma"]) + "\n"


                            embed_sheet.add_field(name="Attributes", value=attributes)

                            

                            await ctx.send(embed=embed_sheet)
                    else:
                        await ctx.send("There is not a charactersheet with such a name. If you wish to view all your characters sheets, please use `>charsheet list`.")

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
            "strength": False,
            "dexterity": False,
            "constitution": False,
            "intelligence": False,
            "wisdom": False,
            "charisma": False
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
    client.add_cog(CharacterSheet(client))