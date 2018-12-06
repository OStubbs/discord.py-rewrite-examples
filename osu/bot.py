import discord
import asyncio
import requests
client = discord.Client()
osuApiKey = "" #put your osu!api key here, could put it inside the osu function it doesn't have a major affect in this code.
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
    
        
@client.command(pass_context=True)
async def osu(ctx, username:str):
    parameters = dict(k=osuApiKey, u=username)
    response = requests.get(url="https://osu.ppy.sh/api/get_user", params=parameters)
    data = response.json()
    profile = ""
    profile += "Username: {}\n".format(data["username"])
    profile += "Raw PP: {}\n".format(data["pp_raw"])
    profile += "Accuracy: {}\n".format(round(data["accuracy"],2))#Round to 2 d.p
    profile += "Country: {}".format(data["country"])
    await ctx.send(profile)#Change this to a embed, looks cleaner.
    
client.run('')#Put bot token here
