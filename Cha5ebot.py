import discord
from discord.ext import commands
import asyncio
import re
import inspect
import os
import configparser

client = commands.Bot(command_prefix='>')
extensions = ['modules.charactersheet','modules.statarray','modules.rolldice']
currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def stop(ctx):
    await client.logout()

config = configparser.ConfigParser()
config.read(currentPath + "/config/bot.ini")
token = config['DEFAULT']['token']

if token != "":
    if __name__ == "__main__":
        for extension in extensions:
            try:
                client.load_extension(extension)
            except Exception as error:
                print(error)


        client.run(token)
