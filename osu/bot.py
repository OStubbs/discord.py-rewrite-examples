import discord
import asyncio
import requests
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!help"):
        msgEmbed = discord.Embed(title="Help", description="Commands")
        await message.channel.send(embed=msgEmbed)

client.run('')#Put bot token here
