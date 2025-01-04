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
async def news(ctx, category: str = None, limit: int = 5):
    try:
        if limit < 1 or limit > 5:
            await ctx.send("Please enter a number between 1 and 5")
            return

        params = {}
        if category:
            params["category"] = category
        if limit:
            params["limit"] = limit

        response = requests.get(URL, params=params)
        response.raise_for_status()
        news_list = response.json()

        if not news_list:
            await ctx.send("Sorry, couldn't find any news")
        else:
            await ctx.send(format_news(news_list, category, limit))

    except requests.exceptions.RequestException as e:
        print(e)


def format_news(news_list, category, limit):
    formatted_news = ""

    if category:
        if len(news_list) < limit:
            formatted_news += f"**Sorry, we only found {len(news_list)} news**\n"
        formatted_news += f"**Here are the top {len(news_list)} news about {category}!**\n"
    else:
        formatted_news += "**Here are your daily news!**\n"

    for n in news_list:
        formatted_news += f"# {n['title']}\n"
        formatted_news += f"{n['summary']}\n"

    return formatted_news


bot.run(TOKEN)
