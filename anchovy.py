import discord
from discord.ext import commands
import os

TOKEN = ('')

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("ready ass")

@bot.command()
async def duce(ctx):
    if ctx.author.id in {133218314469113857}:
        print("do the achovy")

        directory = r'/home/soso/Desktop/Grabber/'
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                funnyname = (os.path.join(directory, filename))
                await ctx.send(file=discord.File(funnyname))
    else:
        await ctx.send("no")


bot.run(TOKEN)
