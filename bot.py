import discord
import asyncio
import random

import time
from bs4 import BeautifulSoup
import requests
client = discord.Client()

import lib


@client.event
async def on_ready():

    print("----------log----------")
    await client.change_presence(activity=discord.Game(name='paly game', type=1))


@client.event
async def on_message(message):

    if message.content.startswith('ping'):
        await message.channel.send("pong")
    
##random

    if message.content.startswith('hello'):
        hi = "hi/hello"
        hichoice = hi.split("/")
        hirnmber = random.randint(1, len(hichoice))
        hiresult = hichoice[hirnmber - 1]
        await message.channel.send(hiresult)


client.run('bot token')
