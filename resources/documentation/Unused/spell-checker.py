import discord
from discord.ext import commands
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

TOKEN = ('')

bot = commands.Bot(command_prefix='%')

@bot.event
async def on_ready():
    print("ready ass")

@bot.event
async def on_message(message):
    if message.author.id in {754720671518687322} or message.channel.id not in {769023126507356163}:
        return
    else:

        text = message.content
        matches = tool.check(text)
        if len(matches) > 1:
            print(f"{message.author.name} can't fucking spell!")
            msg = (matches[1])
            msg6 = str(msg)[:1900]
            msg2 = (f"{message.author.mention} looks like you've made a grammar/spelling mistake\n```{msg}```")
            await message.channel.send(msg2)


bot.run(TOKEN)
