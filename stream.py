import discord, asyncio, sys, time, os, io, shutil
client = discord.Client()
token = "NzgyMjA3NTMwNzI1OTMzMDY2.X8JHsA.NbA9VhB6WMyBFdYJ-bRxmbLQlA4"
from discord.ext import (
    commands,
    tasks
)
client = commands.Bot(
    description='Set Stream Status',
    command_prefix="x",
    self_bot=True
)

def lol(cmd):
    subprocess.call(cmd, shell=True)
    
@client.event
async def on_connect():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("► MightyStatus v1.0 ".center(width))
        print("► Made by kubusxd".center(width))
        print("► Zalogowano na: {0}".format(client.user).center(width))
        print("► Uzywaj z rozwaga! Aby odpalic wpisz na dm/serwerze: xstream `nazwa streama`".center(width))
    ui()
@client.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/kubusxd", 
    )
    await client.change_presence(activity=stream) 
    width = shutil.get_terminal_size().columns
    print("")
    print("")
    print("→ Aktualnie streamujesz: {0} ".format(message).center(width))

client.run(token, bot=False)
