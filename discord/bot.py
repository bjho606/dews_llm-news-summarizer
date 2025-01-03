import discord
## import requests
from discord.ext import commands
from dotenv import load_dotenv
import os

# load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
## FASTAPI_URL = os.getenv("FASTAPI_URL")

# create a bot instance
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)


# Event: Bot is online
@bot.event
async def on_ready():
    print("bot activated")


# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


# Command: News {int}
@bot.command()
async def news(ctx, num: int):
    await ctx.send(f"Top {num} news here!")


bot.run(TOKEN)
