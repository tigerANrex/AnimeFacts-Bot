import discord
import asyncio

from discord.ext import commands

#client = discord.Client()
client = commands.Bot(description = "AnimeFacts Bot", command_prefix = "!")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(pass_context=True)
async def hello(ctx):
    msg = 'Hello World!'
    await client.say(msg)

client.run('MzI3MzU0NDY0MjcxMDczMjgw.DC0IlA.ablfsh7yqBvg-k79TXYzG1EDdc0')
