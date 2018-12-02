import discord
from discord.ext import commands

class CharacterSheet:
    def __init__(self, client):
        self.client = client;

    async def on_ready(self):
        print("loaded cog")

def setup(client):
    client.add_cog(CharacterSheet(client))