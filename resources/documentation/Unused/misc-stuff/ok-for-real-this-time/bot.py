import discord
from discord.ext import commands
import secrets

TOKEN = ('')

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("client ready")

@bot.command
async def pecorine(ctx):
    lines = open("pecorine.botdata").read().splitlines()
    pecorine = secrets.choice(lines)
    await ctx.send(f"{pecorine}")

bot.run(TOKEN)
