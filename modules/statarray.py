from discord.ext import commands
from random import randint

class StatArray:
    def __init__(self, client):
        self.client = client

    async def on_ready(self):
        print("loaded cog")

    @commands.command()
    async def statarray(self, ctx):
        print("I did the statarray thing")
        stats = []
        for x in range(6):
            currentStat = []
            for y in range(4):
                currentStat.append(randint(1, 6))

            lowestDie = min(currentStat)
            currentStat.remove(lowestDie)
            stats.append(sum(currentStat))

        statsString = ' '.join(str(e) for e in stats)
        await ctx.send("Current array for assignable stats is: " + statsString)
        
def setup(client):
    client.add_cog(StatArray(client))