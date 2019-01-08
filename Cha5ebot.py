import discord
from discord.ext import commands
import asyncio
import re
import inspect
import os
import configparser
from modules.libraries.roll import roll_dice

client = commands.Bot(command_prefix='>')
extensions = ['modules.charactersheet','modules.statarray','modules.rolldice','modules.spells']
currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
config = configparser.ConfigParser()
config.read(currentPath + "/config/bot.ini")
token = config['DEFAULT']['token']
modules = config['MODULES']['active']
prefix = config['DEFAULT']['prefix']

client = commands.Bot(command_prefix=prefix)
# extensions = ['charactersheet','statarray','rolldice']


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def stop(ctx):
    await client.logout()

@client.command()
async def roll(ctx, arguments):
    dice_roll = roll_dice(arguments)
    await ctx.send(dice_roll[1])
    


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
