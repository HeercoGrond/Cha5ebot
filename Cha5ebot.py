import discord
from discord.ext import commands
import asyncio
import re
import inspect
import os
import configparser

client = commands.Bot(command_prefix='>')
# extensions = ['charactersheet','statarray','rolldice']
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
modules = config['MODULES']['active']

if token != "":
    if __name__ == "__main__":

        if modules != "":
            extensions = [x.strip() for x in modules.split(',')]
            for extension in extensions:
                try:
                    client.load_extension('modules.' + extension)
                except Exception as error:
                    print(error)


        client.run(token)
