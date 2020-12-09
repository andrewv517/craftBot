# bot.py
import os

import discord
import random
import sqlite3
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot('!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


@client.event
async def on_ready():
    db = sqlite3.connect('main.sqlite')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS main(
        guild_id TEXT,
        msg TEXT,
        channel_id TEXT
        )
        ''')
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def test(ctx):
    await ctx.send("Test")


@client.command()
async def craft(ctx):
    await ctx.send('Craft Bot')


@client.command()
async def coinflip(ctx, count=1):
    heads = 0
    tails = 0
    for i in range(min(max(count if type(count) is int else 1, 1), 500)):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1

    if count == 1:
        await ctx.send("Heads" if heads == 1 else "Tails")
    else:
        await ctx.send("You flipped heads %d times and tails %d times" % (heads, tails))


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
    for i in range(min(max(times if type(times) is int else 1, 1), 10)):
        await ctx.send("@everyone munge")


@client.command()
async def contribute(ctx):
    await ctx.send('https://github.com/andrewv517/craftBot')


client.run(TOKEN)
