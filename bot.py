# bot.py
import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot('!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def test(ctx):
    await ctx.send("Test")


@client.command()
async def craft(ctx):
    await ctx.send('Craft Bot')


@client.command()
tailsNum=0
headsNum=0
async def coinflip(ctx, coinTimes=1):
    outcome=radom.randint(1,2)
    if coinTimes!=1:
        for i in range(min(max(times,1), 500)):
            if outcome=1:
                headsNum+=1
            else:
                tailsNum+=1
     else:
        if outcome=1:
            await ctx.send('You flipped Heads!')
        else:
            await ctx.send('You flipped Tails!')
   await ctx.send("You flipped Heads "+str(headsNum)+" times and Tials "+str(tailsNum)+" times!")


@client.command()
async def poll(ctx):
    upvote = '<:upvote:778439419014152193>'
    downvote = '<:downvote:778439419010613249>'

    await ctx.message.add_reaction(upvote)
    await ctx.message.add_reaction(downvote)


@client.command()
async def pizza(ctx):
    await ctx.send("Pizza")

@client.command()
async def mungeSpam(ctx, times=1):
    for i in range(min(max(times, 1), 10)):
        await ctx.send("@everyone munge")

client.run(TOKEN)
