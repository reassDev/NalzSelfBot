import selfcord
import time
import regex
import discord
from discord.ext import commands
import json
import base64
import os
import pyfiglet
from datetime import datetime
import requests
from colorama import init as colorama_init
from colorama import Fore
import io
import aiohttp
import warnings
from http.client import HTTPException

start_time = time.perf_counter()

with open('config.json', 'r') as file:
    config = json.load(file)

token = config['token']
prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix, self_bot=True)


def clear():
    colorama_init()
    text = "Nalz Bot"
    ASCII_convert = pyfiglet.figlet_format(text)
    text2 = "This is where magic happens :)"
    ASCII_convert2 = pyfiglet.figlet_format(text2)
    if  os.name == 'nt':
        os.system('cls')
        print(f"{Fore.RED}{ASCII_convert}")
        print(f"{Fore.GREEN}{ASCII_convert2}")
    else:
        os.system('clear')
        print(f"{Fore.RED}{ASCII_convert}")
        print(f"{Fore.GREEN}{ASCII_convert2}")


@bot.event
async def on_ready():
  print(f"Connected to {bot.user.name}")
  startupdone = time.perf_counter()
  startuptime = startupdone - start_time
  print(f"Startup took {startuptime} seconds")
  time.sleep(1)
  clear()



@bot.command()
async def ping(ctx):
  await ctx.message.reply(f'Pong! {round(bot.latency * 1000 / 1000)}ms', silent=True)

@bot.command()
async def createrole(ctx, role):
  rolecreate = await ctx.guild.create_role(name=role)
  await ctx.message.reply(f"Created role with name {role}", silent=True)


@bot.command()
async def createchannel(ctx, channel):
  channelcreate = await ctx.guild.create_text_channel(channel)
  await ctx.message.reply(f"Created channel with name {channel}", silent=True)


@bot.command()
async def msg(ctx, user: discord.Member, *, message):
  await user.send(message)
  await ctx.message.reply(f"Messaged {user} with the message {message}", silent=True)


@bot.command()
async def kick(ctx, user: discord.Member, *, reason):
  await user.kick(reason)
  await ctx.message.reply(f"Kicked {user}", silent=True)


@bot.command()
async def ban(ctx, user: discord.Member, *, reason):
  await user.ban(reason)
  await ctx.message.reply(f"Banned {user}", silent=True)


@bot.command()
async def serverinfo(ctx):
  guild = ctx.message.guild
  createdAt = guild.created_at.strftime("%d %B, %Y")
  await ctx.message.reply(f"**🖥 {guild.name}'s information**\n- ID: {guild.id}\n- Name: {guild.name}\n- Owner: {guild.owner}\n- Created At: {createdAt}", ephemeral=True)


@bot.command()
async def userinfo(ctx, user: discord.User):
  createdAt = user.created_at.strftime("%d %B, %Y")
  await ctx.message.reply(f"**👤 {user.name}'s information**\n- ID: {user.id}\n- Username: {user.name}\n- Discriminator: {user.discriminator}\n- Created At: {createdAt}", silent=True)

@bot.command()
async def com(ctx):
  await ctx.message.reply(f"(n-ping) - Returns the ping of the bot\n(n-createrole) - Creates a new role with the first argument of the command\n(n-createchannel) - Creates a new channel with the first argument of the command\n(n-msg) - Sends a message to the user in the first argument with the second argument as the message\n(n-kick) - Kicks the player provided in the first argument if you have permission to do so\n(n-ban) - Bans the player provided in the first argument if you have permission to do so\n(n-serverinfo) - Gives information about the server that the command is ran in\n(n-userinfo) - Gives information about the user provided in the first argument of the command\n(n-base64encrypt) - Encrypts the first argument of the command\n(n-base64decrypt) - Decrypts the first argument of the command", silent=True)


@bot.command()
async def base64encrypt(ctx, *, message):
  message_bytes = message.encode('ascii')
  base64_bytes = base64.b64encode(message_bytes)
  base64_message = base64_bytes.decode('ascii')
  await ctx.message.reply(f"Encoded message: {base64_message}", silent=True)


@bot.command()
async def base64decrypt(ctx, *, message):
  base64_bytes = message.encode('ascii')
  message_bytes = base64.b64decode(base64_bytes)
  decoded_message = base64_bytes.decode('ascii')
  await ctx.message.reply(f"Decoded message: {decoded_message}", silent=True)


bot.run(token)
