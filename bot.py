import discord
import os
from discord.ext import tasks
import requests

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1500116393356689482

intents = discord.Intents.default()
client = discord.Client(intents=intents)

posted = ""

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    check_scores.start()

@tasks.loop(minutes=5)
async def check_scores():
    global posted
    channel = client.get_channel(CHANNEL_ID)

    # Temporary test message
    if posted == "":
        await channel.send("⚔️ Sheffield United bot is now live!")
        posted = "done"

client.run(TOKEN)
