from discord.ext import commands
from dotenv import load_dotenv
import discord
import requests
import os


# load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
URL = os.getenv("BASE_URL")

# set intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# create a bot instance
bot = commands.Bot(command_prefix="/", intents=intents)


# Event: Bot is online
@bot.event
async def on_ready():
    print("bot activated")


# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


# Command: News {category} {count}
@bot.command()
async def news(ctx, category: str = None, count: int = 5):
    try:
        params = {}
        if category:
            params["category"] = category
        if count:
            params["count"] = count

        response = requests.get(URL, params=params)
        response.raise_for_status()
        news_list = response.json()

        if not news_list:
            await ctx.send("Sorry, couldn't find any news")
        else:
            for n in news_list:
                await ctx.send(format_news(n))

    except requests.exceptions.RequestException as e:
        print(e)


def format_news(news_str):
    formatted_news = []
    return formatted_news


bot.run(TOKEN)
