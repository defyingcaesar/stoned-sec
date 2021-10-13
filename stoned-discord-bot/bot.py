import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    print('Bot is connected')



client.run('ODk3Nzc4NjUyNzY5NTc0OTMy.YWanhg.LP_BtzgwXcn4xAObqn3hHf3R_-Y')