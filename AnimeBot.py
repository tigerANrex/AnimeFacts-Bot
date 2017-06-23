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

@client.command()
async def name(*args):
        print(args)
        url = ("https://myanimelist.net/character.php?{}".format(urlencode({'q':' '.join(args)})))
        return await client.say(url)

client.run('MzI3MzU0NDY0MjcxMDczMjgw.DC0IlA.ablfsh7yqBvg-k79TXYzG1EDdc0')
