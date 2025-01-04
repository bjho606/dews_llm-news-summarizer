from discord.ext import commands
from dotenv import load_dotenv
import discord
import requests
import os


command_map = {
    "p": "politics",
    "e": "economy",
    "s": "society",
    "l": "life/culture",
    "c": "life/culture",
    "lc": "life/culture",
    "t": "tech",
    "politics": "politics",
    "economy": "economy",
    "society": "society",
    "life": "life/culture",
    "culture": "culture",
    "life/culture": "culture",
    "tech": "tech",
}

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
async def news(ctx, command: str = None, limit: int = 5):
    try:
        # case 1: invalid command
        category = "ALL"
        if command:
            category = parse_command(command)
            if category == "INVALID":
                await ctx.send("Invalid command. Please try again.")
                return

        # case 2: number of news out of range
        if limit < 1 or limit > 5:
            await ctx.send("Please enter a number between 1 and 5")
            return

        # set parameters for API
        params = {}
        if category != "ALL":
            params["category"] = category
        if limit:
            params["limit"] = limit

        # send request and get response
        response = requests.get(URL, params=params)
        response.raise_for_status()
        news_list = response.json()

        if not news_list:
            await ctx.send("Sorry, couldn't find any news")
        else:
            await ctx.send(format_news(news_list, category, limit))

    except requests.exceptions.RequestException as e:
        print(e)


# make actual bot message based on response
def format_news(news_list, category, limit):
    formatted_news = ""

    if category != "ALL":
        if len(news_list) < limit:
            formatted_news += f"**Sorry, we only found {len(news_list)} news**\n"
        formatted_news += f"**Here are the top {len(news_list)} news about {category}!**\n"
    else:
        formatted_news += "**Here are your daily news!**\n"

    for n in news_list:
        formatted_news += f"# {n['title']}\n"
        formatted_news += f"{n['summary']}\n"

    return formatted_news


# parse short command into actual category
# invalid category command is returned INVALID
def parse_command(command):
    parsed_command = command_map.get(command)
    if not parsed_command:
        return "INVALID"
    return parsed_command


bot.run(TOKEN)
