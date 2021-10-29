import discord
from discord.ext import commands

import settings

client = commands.Bot(command_prefix="")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content:
        category = message.channel.category.name
        channel = message.channel
        content = message.content
        author = message.author
        print(f"[{category} > #{channel}] <{author}> {content}")


client.run(settings.TOKEN)