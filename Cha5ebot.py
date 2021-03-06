import discord
from discord.ext import commands
import asyncio
import re
import inspect
import os
import configparser
from modules.libraries.roll import roll_dice

extensions = ['modules.charactersheet','modules.statarray','modules.rolldice','modules.spells']
currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
config = configparser.ConfigParser()
config.read(currentPath + "/config/bot.ini")
token = config['DEFAULT']['token']
modules = config['MODULES']['active']
prefix = config['DEFAULT']['prefix']
admin_id = int(config['DEFAULT']['admin_id'])

client = commands.Bot(command_prefix=prefix)
# extensions = ['charactersheet','statarray','rolldice']


@client.event
async def on_ready():
    game = discord.Game("Dungeons & Dragons")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def stop(ctx):
    if admin_id == ctx.author.id:
        print("Shutting down bot because of admin command.") 
        await client.logout()

    elif admin_id == None: 
        print("Shutting down bot because of command.")
        await client.logout()

@client.command()
async def roll(ctx, arguments):
    dice_roll = roll_dice(arguments)
    await ctx.send(dice_roll[1])
    

# @client.command()
# async def role(ctx, arguments):
#     user = ctx.message.author
#     if (arguments.lower() == "dm"):
#         role = discord.utils.get(ctx.guild.roles, name="DM")
#         await user.add_roles(role)
#         await ctx.send("You now have the role of DM")
#         if discord.utils.get(ctx.guild.roles, name="Player") in user.roles:
#             await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Player"))
#             await ctx.send("Also removed your role of Player")
#     elif (arguments.lower() == "player"):
#         role = discord.utils.get(ctx.guild.roles, name="Player")
#         await user.add_roles(role)
#         await ctx.send("You now have the role of Player")
#         if discord.utils.get(ctx.guild.roles, name="DM") in user.roles:
#             await user.remove_roles(discord.utils.get(ctx.guild.roles, name="DM"))
#             await ctx.send("Also removed your role of DM")
#     else:
#         await ctx.send("That is not a role you can choose, please pick either 'Player' or 'DM'")
    

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
