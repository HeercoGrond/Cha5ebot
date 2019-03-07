from discord.ext import commands
import discord
from random import randint
import json
from modules.libraries.roll import roll_dice

class Monsters(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def monster(self, ctx, *, arg):
        with open('./modules/libraries/monsters.json') as f:
            monster_data = json.load(f)
            for monster in monster_data:
                if monster["title"].lower() == arg.lower():
                    embed_monster = discord.Embed(title=monster["title"])

                    for content in monster["contents"]:
                        if content != "rule":
                            if "subtitle" in content:
                                embed_monster.description = content.split('|')[1]

                            # if "armor class" in content.lower() or "hit points" in content.lower() or "speed" in content.lower():
                            #     if "text" not in content.lower():
                            #         splitContent = content.split("|")
                                    
                            #         embed_monster.add_field(name=splitContent[1], value=splitContent[2])
                                

                    embed_monster.set_thumbnail(url=monster["background_image"])

                    await ctx.send(embed=embed_monster)

def setup(client):
    client.add_cog(Monsters(client))