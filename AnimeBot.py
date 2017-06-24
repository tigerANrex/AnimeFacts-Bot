import discord
import asyncio
from pyrebase import pyrebase
from urllib.parse import urlencode

from discord.ext import commands

config = {
"apiKey": "AIzaSyCq_q5ny1h_hAv_JHglS7b2PQFpS7UewWQ",
"authDomain": "animefacts-bot.firebaseapp.com",
"databaseURL": "https://animefacts-bot.firebaseio.com",
"storageBucket": "animefacts-bot.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#client = discord.Client()
client = commands.Bot(description = "AnimeFacts Bot", command_prefix = "!")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    await client.change_presence(game=discord.Game(name='Prefix: !'))

@client.command(pass_context=True)
async def hello(ctx):
    msg = 'Hello World!'
    await client.say(msg)

@client.command()
async def name(*args):
        print(args)
        url = ("https://myanimelist.net/character.php?{}".format(urlencode({'q':' '.join(args)})))
        return await client.say(url)

@client.command()
async def allFacts():
    all_facts = db.child("anime").shallow().get()
    response = "All Facts:\n{}".format("\n".join(all_facts.val()))
    return await client.say(response)

@client.command(aliases = ['add'])
async def addFact(name, *, fact):
    db.child("anime").update({name: "{}".format(fact)})
    return await client.say("I've added {}".format(name))

@client.command()
async def fact(name):
    fact = db.child("anime").child(name).get()
    return await client.say(fact.val())

client.run('MzI3MzU0NDY0MjcxMDczMjgw.DC0IlA.ablfsh7yqBvg-k79TXYzG1EDdc0')
