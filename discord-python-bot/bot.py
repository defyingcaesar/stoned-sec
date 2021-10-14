import os
import random
import discord
import logging
from dotenv import load_dotenv
import requests
import json
from types import SimpleNamespace

# Logging setup
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
FLOOR = os.getenv('FLOOR_API')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="your mom"))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello friend!')
        
    if message.content.startswith('!ping'):
        await message.channel.send('I am working!')

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == '!help':
        await message.channel.send("`I support 4 commands:\n!ping - To check if I am working\n!hello - To greet me\n'99!' - Prints random brooklyn 99 quote\n!help - For checking out what commands are available`")

    if message.content == '69':
        await message.channel.send(':eyes: :eyes: :eyes:')
    
    if message.content =='!floor':
        url = "https://61675396ba841a001727c2de.mockapi.io/api/v1/collections"
        response = requests.get(url)
        await message.channel.send(response.text)
        
        
client.run(TOKEN)