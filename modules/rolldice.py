from discord.ext import commands
from random import randint
import re

class RollDice:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def roll(self, ctx, arguments):
        detailed = "detailed" in ctx.message.content
        firstcheck = re.search(r'[0-9]+d[0-9]+[+][0-9]+', arguments)
        if firstcheck: 
            outcomeList = "{"
            matchString = str(firstcheck.group())
            argsList = matchString.split('d')
            splitArg = argsList[1].split('+')
            diceAmount = int(argsList[0])
            diceEyes = int(splitArg[0])
            bonus = int(splitArg[1])
            outcome = 0
            for _ in range(1, diceAmount + 1):
                randomNumber = randint(1, diceEyes)
                if detailed:
                    outcomeList += str(randomNumber) + " , "
                outcome += randomNumber

            outcome += bonus
            await ctx.send("Rolled " + str(diceAmount) + " d" + str(diceEyes) + " with a bonus of " + str(bonus) + " for a total count of: " + str(outcome))
            if detailed:
                    await ctx.send("Details on the rolls: " + outcomeList + " }")
        
        else:
            secondCheck = re.search(r'[0-9]+d[0-9]+', arguments)
            if secondCheck:
                outcomeList = "{ "
                matchedString = str(secondCheck.group())
                argsList = matchedString.split('d')
                diceAmount = int(argsList[0])
                diceEyes = int(argsList[1])
                outcome = 0
                for _ in range(1, diceAmount + 1):
                    randomNumber = randint(1, diceEyes)
                    if detailed:
                        outcomeList += str(randomNumber) + " , "
                    outcome += randomNumber

                await ctx.send("Rolled " + str(diceAmount) + " d" + str(diceEyes) + " for a total count of: " + str(outcome))
                if detailed:
                    await ctx.send("Details on the rolls: " + outcomeList + " }")
            else:
                tertiaryCheck = re.search(r'd[0-9]+', arguments)
                if tertiaryCheck:
                    matchedString = str(tertiaryCheck.group())
                    argsList = matchedString.split('d')
                    diceEyes = int(argsList[1])
                    outcome = randint(1, diceEyes)
                    await ctx.send("Rolled a d" + str(diceEyes) + " for: " + str(outcome))
                else:
                    await ctx.send("That is not a valid die. Proper formatting is `>roll {x]d{y}+{z}`, `>roll {x]d{y}` or `>roll d{x}`")

        
def setup(client):
    client.add_cog(RollDice(client))