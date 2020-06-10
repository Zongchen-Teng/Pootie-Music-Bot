import discord
from discord.ext import commands 
import asyncio
#import youtube_dl
import shutil
import os 
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('System is Online, Welcome to Pootie Music Bot')

 #/help manual
@client.command(aliases=['hi'])
async def hello(ctx):
    user = ctx.message.author
    await ctx.send(f"Hello There {user.mention}, here is the help manual:")

client.run('NzE5OTc4MDMxNjk0NzQxNTYy.XuAkhA.ivJkvmoH0YrZYGjD6MI-wFIpL1Y')