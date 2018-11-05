import discord
import asyncio
from random import randint
import re
import inspect
import os
import configparser

client = discord.Client()
currentPath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        channel = message.channel
        if "!statarray" in message.content:
            stats = []
            for x in range(6):
                currentStat = []
                for y in range(4):
                    currentStat.append(randint(1, 6))

                lowestDie = min(currentStat)
                currentStat.remove(lowestDie)
                stats.append(sum(currentStat))

            statsString = ' '.join(str(e) for e in stats)
            await channel.send("Current array for assignable stats is: " + statsString)

        if message.content.startswith("!roll"):
            detailed = "detailed" in message.content
            firstcheck = re.search(r'[0-9]+d[0-9]+[+][0-9]+', message.content)
            if firstcheck: 
                outcomeList = "{ "
                matchString = str(firstcheck.group())
                argsList = matchString.split('d')
                splitArg = argsList[1].split('+')
                diceAmount = int(argsList[0])
                diceEyes = int(splitArg[0])
                bonus = int(splitArg[1])
                outcome = 0
                for x in range(1, diceAmount + 1):
                    randomNumber = randint(1, diceEyes)
                    if detailed:
                        outcomeList += str(randomNumber) + " , "
                    outcome += randomNumber

                outcome += bonus
                await channel.send("Rolled " + str(diceAmount) + " d" + str(diceEyes) + " with a bonus of " + str(bonus) + " for a total count of: " + str(outcome))
                if detailed:
                        await channel.send("Details on the rolls: " + outcomeList + " }")
                
            else:
                filteredString = re.search(r'[0-9]+d[0-9]+', message.content)
                if filteredString:
                    outcomeList = "{ "
                    matchedString = str(filteredString.group())
                    argsList = matchedString.split('d')
                    diceAmount = int(argsList[0])
                    diceEyes = int(argsList[1])
                    outcome = 0
                    for x in range(1, diceAmount + 1):
                        randomNumber = randint(1, diceEyes)
                        if detailed:
                            outcomeList += str(randomNumber) + " , "
                        outcome += randomNumber

                    await channel.send("Rolled " + str(diceAmount) + " d" + str(diceEyes) + " for a total count of: " + str(outcome))
                    if detailed:
                        await channel.send("Details on the rolls: " + outcomeList + " }")
                else:
                    secondaryFilter = re.search(r'd[0-9]+', message.content)
                    if secondaryFilter:
                        matchedString = str(secondaryFilter.group())
                        argsList = matchedString.split('d')
                        diceEyes = int(argsList[1])
                        outcome = randint(1, diceEyes)
                        await channel.send("Rolled a d" + str(diceEyes) + " for: " + str(outcome))
                    else:
                        await channel.send("That is not a valid die. Proper formatting is `!roll {x]d{y}` or `!roll d{x}`")

        if message.content.startswith("!charsheet"):
            if message.server != None:
                currentServerPath = currentPath + "/servers/" + message.server.id
                print(currentServerPath)

                if not os.path.exists(currentServerPath):
                    os.makedirs(currentServerPath)

                currentUserPath = currentServerPath + "/user/" + message.author.id
                if not os.path.exists(currentUserPath):
                    os.makedirs(currentUserPath)
                    print("Created charsheet folder for user " + message.author.id)
            

config = configparser.ConfigParser()
config.read(currentPath + "/config/bot.ini")
token = config['DEFAULT']['token']

if token != "":
    client.run(token)
