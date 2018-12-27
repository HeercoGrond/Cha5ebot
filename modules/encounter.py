from discord.ext import commands
import discord
import json
import os

class Encounter:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")
    
    @commands.command()
    async def encounter(self, ctx, *args):
        if discord.utils.get(ctx.guild.roles, name="DM") in ctx.message.author.roles:
            if ctx.guild != None:
                # Variables
                currentGuildPath = "./guilds/" + str(ctx.guild.id)
                currentEncounterPath = currentGuildPath + "/encounters"
                argumentCount = len(args)

            if argumentCount == 0:
                await ctx.send("No arguments were provided, please make sure to provide an argument to the command.")

            else:
                argument = args[0]

                if argument == "make":
                    if argumentCount != 2:
                        await ctx.send("There was either less or more than 1 argument input into the command. Propper usage is '>encounter make {x}' where {x} is the encounter name.")

                    else:
                        filename = args[1]
                        if not os.path.exists(currentGuildPath):
                            os.makedirs(currentGuildPath)
                            print("Created guild path.")

                        if not os.path.exists(currentEncounterPath):
                            os.makedirs(currentEncounterPath)
                            print("Created encounter path")

                        if not os.path.exists(currentEncounterPath + "/" + filename + ".json"):
                            with open(currentEncounterPath + "/" + filename + ".json", 'w') as fp:
                                data = self.make_encounter(filename)
                                json.dump(data, fp, indent=4, sort_keys=True)
                                await ctx.send("Created an encounter with the name: " + data["name"])

                        else:
                            await ctx.send("An encounter with the name '" + filename + "' was already found.")

                elif argument == "delete":
                    if argumentCount != 2:
                        await ctx.send("There was either less or more than 1 argument into the command. Proper usage is `>encounter delete {x}` where {x} is the encounter's name that will be deleted.")

                    else:
                        filename = args[1]
                        path = currentEncounterPath + "/" + filename + ".json"
                        if os.path.exists(path):
                            os.remove(path)
                            await ctx.send("Succesfully deleted encounter '" + filename + "'.")
                        else:
                            await ctx.send("The encounter you are trying to delete doesn't seem to exist.")

                elif argument == "list":
                    with os.scandir(currentEncounterPath + "/") as encounters:
                        description = "" 
                        for file in encounters:
                            description += file.name.replace(".json", "") + "\n"

                        embed_totalEncounters = discord.Embed(title="Currently active encounters:", description=description)
                        await ctx.send(embed=embed_totalEncounters)

                elif os.path.exists(currentEncounterPath + "/" + argument + ".json"):
                    if args[1] == "add":
                        with open("./modules/libraries/monsters.json") as f:
                            monster_data = json.load(f)
                            for monster in monster_data:
                                if monster["title"].lower() in args:
                                    with open(currentEncounterPath + "/" + argument + ".json", "r+") as f:
                                        encounter_file = json.load(f)

                                        encounter_file["participants"].append(monster["title"])

                                        f.seek(0)
                                        json.dump(encounter_file, f, indent=4)
                                        f.truncate()

                                    await ctx.send("Added one " + monster["title"] + " to the " + argument + " encounter.")

                    elif args[1] == "remove":
                        with open(currentEncounterPath + "/" + argument + ".json") as f:
                            encounter_data = json.load(f)
                            for monster in encounter_data["participants"]:
                                if monster.lower() in args:
                                    encounter_data["participants"].remove(monster)

                                    with open(currentEncounterPath + "/" + argument + ".json", "w") as f:
                                        encounter_data = json.load(f)
                                        json.dump(encounter_data, f)
                                    await ctx.send("Removed one " + monster + " from the " + argument + " encounter.")

                    elif args[1] == "list":
                        with open(currentEncounterPath + "/" + argument + ".json", "r") as f:
                            encounter_data = json.load(f)
                            description = "" 
                            for monster in encounter_data["participants"]:
                                description += monster + "\n"

                            embed_totalMonsters = discord.Embed(title="Current monsters in encounter: " + args[0], description=description)
                            await ctx.send(embed=embed_totalMonsters)

        else:
            await ctx.send("You don't have permission to use that command.")

    def make_encounter(self, enc_name):
        encounter = {}

        encounter["name"] = enc_name
        encounter["description"] = ""
        encounter["participants"] = []
        encounter["map"] = ""

        return encounter




def setup(client):
    client.add_cog(Encounter(client))