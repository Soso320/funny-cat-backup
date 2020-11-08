# unfunny.py
import asyncio
import json
import os
import random
import secrets
import shutil
import string
import subprocess
import threading
import time
from time import sleep
from datetime import datetime
import sqlite3

import bs4 as bs
import cleverbotfreeapi
import discord
import requests
import tracemoepy
from PIL import Image, ImageDraw, ImageFont
from PyDictionary import PyDictionary
from discord.ext import commands
from discord.ext.commands import MemberConverter
from google_images_search import GoogleImagesSearch
from translate import Translator

connection = sqlite3.connect("tagbot.sqlite")

TOKEN = ('')

bot = commands.Bot(command_prefix='%',
                   description='''For detailed help, See https://gitlab.com/SosoM1k0r31z31/funny-cat/-/wikis/commands''')

@bot.event
async def on_ready():
    print("ready ass")

bot.remove_command('help')


@bot.command()
async def help(ctx):
    msg = (f"{ctx.author.mention} https://gitlab.com/SosoM1k0r31z31/funny-cat/-/wikis/commands")
    await ctx.send(msg)


def randomnumbergen(range1, range2):
    a = int(range1)
    b = int(range2)

    r = requests.get(f"https://www.random.org/integers/?num=1&min={a}&max={b}&col=1&base=10&format=plain&rnd=new")
    randnumber = (r.text)
    y = randnumber.strip()
    z = int(y)
    return z


@bot.command()
async def accountage(ctx, *, id):
    if id == None:
        msg = (
            f"{ctx.author.name} Info:\nJoin date: {ctx.author.joined_at}\nAccount creation date: {ctx.author.created_at}\nAvatar URL: {ctx.author.avatar_url}")
        await ctx.channel.send(msg)
    else:
        avamember = await bot.fetch_user(id)
        msg = (
            f"{avamember.name} Info:\nJoin date: {avamember.joined_at}\nAccount creation date: {avamember.created_at}\nAvatar URL: {avamember.avatar_url}")
        await ctx.channel.send(msg)


@bot.command()
async def randnum(ctx, ran1, ran2, num):
    r = requests.get(
        f"https://www.random.org/integers/?num={num}&min={ran1}&max={ran2}&col=1&base=10&format=plain&rnd=new")
    randnumber = (r.text)
    msg = (f"```{randnumber}```")
    await ctx.send(msg)


@bot.command()
async def passgen(ctx, leng):
    if float(leng) > 1960:
        await ctx.send("too high, limit is `1950`")

    length = int(leng)

    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    msg = (f"```Your {leng} character password is\n{password}```")
    if len(msg) > 2000:
        await ctx.send("Hit character limit.")
    await ctx.channel.send(msg)


@bot.command()
async def lying(ctx, iss, pronoun):
    if pronoun == "she":
        zerotwo = (
            "<@{0}> has me lying on my back. She's holding my legs in the air, and she's used an entire bottle of lube on her 8 inch cock. She slides her dino dick inside my winking, inviting asshole and starts thrusting into me. My moans of pleasure turn to shouts as she thrusts harder and harder inside me, slamming against my prostate. We look into each others' eyes, and she grabs my throbbing, erect penis and starts jacking me off while continuously thrusting her dinogirl penis deeper into my anal cavity. I can't take anymore and blast a gigantic load that hits my face, my eyes, my mouth, and my hair. Her thrusts get even faster and I feel my asshole start to overfill with her cum as she blasts a load into my anal cavity. She pulls her girlcock out of me and a river of dino semen starts to flow out of my asshole. She looks at my cum covered face and shoves her tongue down my throat and starts licking up the cum from my face.").format(
            iss)
    elif pronoun == "he":
        zerotwo = (
            "<@{0}> has me lying on my back. He's holding my legs in the air, and he's used an entire bottle of lube on his 8 inch cock. He slides his dino dick inside my winking, inviting asshole and starts thrusting into me. My moans of pleasure turn to shouts as he thrusts harder and harder inside me, slamming against my prostate. We look into each others' eyes, and he grabs my throbbing, erect penis and starts jacking me off while continuously thrusting his dinogirl penis deeper into my anal cavity. I can't take anymore and blast a gigantic load that hits my face, my eyes, my mouth, and my hair. His thrusts get even faster and I feel my asshole start to overfill with his cum as he blasts a load into my anal cavity. He pulls his cock out of me and a river of dino semen starts to flow out of my asshole. He looks at my cum covered face and shoves his tongue down my throat and starts licking up the cum from my face.").format(
            iss)
    else:
        await ctx.send("Invalid pronoun")
    print(iss)
    await ctx.send(zerotwo)


@bot.command()
async def aiwaifu(ctx):
    randnum = randomnumbergen(1, 100000)
    link = (f"https://www.thiswaifudoesnotexist.net/example-{randnum}.jpg")
    embed1 = discord.Embed(title="AI Generated waifu", color=0xff0080)
    embed1.set_image(url=f"{link}")
    await ctx.send(embed=embed1)


@bot.command()
async def rate(ctx, *, inp):
    rating = secrets.randbelow(100)
    await ctx.channel.send(f"I rate `{inp}` a {rating}/100")


@bot.command()
async def randomwaifu(ctx):
    url = "https://www.random.org/integers/?num=1&min=1&max=104900&col=1&base=10&format=plain&rnd=new"
    q = requests.get(url)
    randnumbe = (q.text)
    randnumber = int(randnumbe)

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    }
    url = (f"http://www.animecharactersdatabase.com/api_series_characters.php?character_id={randnumber}")
    r = requests.get(url, headers=headers)
    json_data = r.json()

    charactername = (json_data["name"])
    charactergender = (json_data["gender"])
    characteranime = (json_data["origin"])
    characterimage = (json_data["character_image"])
    characterid = (json_data["id"])

    embed1 = discord.Embed(title="Random waifu", color=0xc290c6)
    embed1.add_field(name="Name:", value=f"{charactername}", inline=False)
    embed1.add_field(name="Anime", value=f"{characteranime}", inline=False)
    embed1.add_field(name="Gender:", value=f"{charactergender}", inline=False)
    embed1.set_footer(text=f"Character ID: {characterid}")
    embed1.set_image(url=f"{characterimage}")
    await ctx.send(embed=embed1)


@bot.command()
async def screenshot(ctx, address, mode: str = None):
    if ctx.author.id == ctx.author.id:
        if "https://nhentai.net" in address:
            await ctx.send("no :happytroll:")
            return
        try:
            await ctx.send(f"ok, screenshotting `{address}`\nplease wait...")
            if mode == "full":
                attachmentname = ('GFS-SNAPSHOT_{0}.png').format(ctx.message.id)
                message = ("Screenshot of `{0}` Successfully taken").format(address)

                options = webdriver.FirefoxOptions()
                options.headless = True
                driver = webdriver.Firefox(options=options)
                driver.get(address)
                S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
                driver.set_window_size(S('Width'), S(
                    'Height'))  # May need manual adjustment
                driver.find_element_by_tag_name('body').screenshot(attachmentname)

                driver.quit()
            else:
                attachmentname = ('GFS-SNAPSHOT_{0}.png').format(ctx.message.id)
                message = ("Screenshot of `{0}` Successfully taken").format(address)

                driver = webdriver.Firefox()
                driver.get(address)
                sleep(5)
                driver.get_screenshot_as_file(attachmentname)

            await ctx.channel.send(message, file=discord.File(attachmentname))
            os.remove(attachmentname)

        except Exception as x:
            print(x)
            exc = (":boom: **Error** ```{0}```").format(x)
            await ctx.channel.send(exc)
            driver.quit()


async def approach(message):
    await message.add_reaction("<a : approach: 744291002235355146 >")


@bot.command()
async def react(ctx, idd):
    msg = await ctx.channel.fetch_message(idd)
    await approach(msg)


def webhook(message, username, avatar, url):
    embed = {
        "content": message,
        "username": username,
        "avatar_url": avatar
    }
    result = requests.post(url, data=json.dumps(embed), headers={"Content-Type": "application/json"})


@bot.command()
async def frame(ctx, id, *, message):
    if "everyone" in message or "@everyone" in message or "@Everyone" in message or "@here" in message:
        await ctx.send("wtf bro no...")
    else:
        try:
            await ctx.message.delete()
        except:
            pass
        avamember = await bot.fetch_user(id)
        url = "https://discordapp.com/api/webhooks/"
        name = (f'{avamember.name}')
        avatar = (f'{avamember.avatar_url}')
        msg = (f'"{message}"')
        webhook(message, name, avatar, url)
        print(
            f"INFO: Frame command ran: [{ctx.author.name}#{ctx.author.discriminator} Framed {avamember.name}#{avamember.discriminator} to say '{message}']")


@bot.command()
async def webhooktransmit(ctx, link, username, avatar, content):
    await ctx.message.delete()
    embed = {
        "content": content,
        "username": username,
        "avatar_url": avatar
    }
    result = requests.post(link, data=json.dumps(embed), headers={"Content-Type": "application/json"})
    a = result.raise_for_status()
    await ctx.send(a)


@bot.command()
async def rename(ctx, *, name):
    if ctx.author.id in {133218314469113857}:
        await bot.user.edit(username=name)
    else:
        await ctx.send("bot owner only :////")


@bot.command()
async def changeavatar(ctx):
    if ctx.author.id in {133218314469113857}:
        try:

            await ctx.send("ok")
            print("ok")
            urlll = (""'{}'"").format(ctx.message.attachments[0].url)
            urlllname = (""'{}'"").format(ctx.message.attachments[0].filename)
            print(urlll)
            print(urlllname)
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
            }
            r = requests.get(urlll, headers=headers, stream=True)

            with open(urlllname, 'wb') as out_file:
                shutil.copyfileobj(r.raw, out_file)
            del r
            print("ok2")
            await ctx.message.delete()
            with open(urlllname, 'rb') as f:
                await bot.user.edit(avatar=f.read())
            print("ok3")
            os.remove(urlllname)
            print("ok4")
            await ctx.send(f"ok, changed avatar to `{urlllname}`")
        except Exception as x:
            await ctx.channel.send(f"error...\n`{x}`")
    else:
        await ctx.send("bot owner only :////")


@bot.command()
async def activity(ctx, *, act):
    if ctx.author.id in {133218314469113857}:
        await bot.change_presence(activity=discord.Game(name=act))
        await ctx.send(f"changed game status to `{act}`")
    else:
        await ctx.send("bot owner only :////")


@bot.command()
async def yomama(ctx):
    lines = open("yomama.txt").read().splitlines()
    joke = secrets.choice(lines)
    await ctx.send(f"{ctx.author.mention} {joke}")


@bot.command()
async def ask(ctx, *, question):
    a = secrets.randbelow(2)
    if a == 0:
        msg = (f"> {question}\n{ctx.author.mention} Yes")
    else:
        msg = (f"> {question}\n{ctx.author.mention} No")
    await ctx.send(msg)


@bot.command()
async def opinion(ctx, avamember: discord.User = None):
    a = secrets.randbelow(2)
    if a == 1:
        await ctx.send(
            f"{avamember.mention} https://tenor.com/view/ihate-you-anime-mad-ihate-you-so-fucking-much-gif-17124653")
    else:
        await ctx.send(f"{avamember.mention} https://media.tenor.com/images/32ee226a0b4bd839f444fddbde231310/tenor.gif")


@bot.command()
async def randompasta(ctx):
    with connection:
            data = connection.execute("SELECT * FROM PASTAS ORDER BY RANDOM() LIMIT 1;")
            for row in data:
                a = (row[1])
                b = (row[0])
                await ctx.send(a)
                await ctx.send(f"`{b}`")

@bot.command()
async def appendpasta(ctx, *, pasta):
    if len(pasta) > 1968:
        await ctx.send(f"Sorry, your copypasta is too long. the limit is `1968` (Yours was `{len(pasta)}`)")
        return
    authorid = (secrets.token_hex(8))
    formatting = (f"{pasta} **[Courtesy of {ctx.author.name}#{ctx.author.discriminator}]**\n")
    sql = 'INSERT INTO PASTAS (id, content) values(?, ?)'
    data = [
        (authorid, formatting),
    ]
    with connection:
        connection.executemany(sql, data)
    await ctx.send(f"Successfully added your copypasta to the database")

@bot.command()
async def deletepasta(ctx, pastaid):
    try:
        if ctx.author.id in {133218314469113857}:
            exe = connection.execute(f"DELETE FROM PASTAS WHERE id LIKE '{pastaid}'")
            await ctx.send(f"```{exe}```")
            await ctx.send(f"Successfully deleted pasta `{pastaid}`")
        else:
            await ctx.send("bot owner only!")
    except Exception as x:
        await ctx.send(f"Error: ```{x}```")


@bot.command()
async def femboyrate(ctx, avamember: discord.User = None):
    a = randomnumbergen(0, 100)
    msg = (f"{avamember.mention} is {a}% fe mb oy")
    await ctx.channel.send(msg)


@bot.command()
async def ship(ctx, avamember: discord.User = None, avamember2: discord.User = None):
    a = randomnumbergen(0, 100)
    print(a)
    print("ok")
    if a <= 10:
        kokoro = (
            "[ :blue_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 20:
        kokoro = (
            "[ :blue_heart: :blue_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 30:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 40:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 50:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 60:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 70:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 80:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :black_heart: :black_heart: ]")
    elif a <= 90:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :black_heart: ]")
    elif a <= 100:
        kokoro = (
            "[ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: ]")
    if avamember.id in {133218314469113857} and avamember2.id in {397928612906532865}:
        msg = (
            f"Person 1: {avamember.mention}\nPerson 2: {avamember2.mention}\nRating: [ :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart:  :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: :blue_heart: ] (59864561561561564651561890565914685534653412343542345374534534254534545324153%)")
    else:
        msg = (f"Person 1: {avamember.mention}\nPerson 2: {avamember2.mention}\nRating: {kokoro} ({a}%)")
    await ctx.send(msg)


@bot.command()
async def threesomeship(ctx, avamember: discord.User = None, avamember2: discord.User = None,
                        avamember3: discord.User = None):
    a = randomnumbergen(0, 100)
    print(a)
    print("ok")
    if a <= 10:
        kokoro = (
            "[ :green_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 20:
        kokoro = (
            "[ :green_heart: :green_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 30:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 40:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :green_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 50:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 60:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 70:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 80:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :black_heart: :black_heart: ]")
    elif a <= 90:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :black_heart: ]")
    elif a <= 100:
        kokoro = (
            "[ :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: :green_heart: ]")
    msg = (
        f"Person 1: {avamember.mention}\nPerson 2: {avamember2.mention}\nPerson 3: {avamember3.mention}\nRating: {kokoro} ({a}%)")
    await ctx.send(msg)


@bot.command()
async def orgyship(ctx, avamember: discord.User = None, avamember2: discord.User = None,
                   avamember3: discord.User = None, avamember4: discord.User = None, avamember5: discord.User = None):
    a = randomnumbergen(0, 100)
    print(a)
    print("ok")
    if a <= 10:
        kokoro = (
            "[ :heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 20:
        kokoro = (
            "[ :heart: :heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 30:
        kokoro = (
            "[ :heart: :heart: :heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 40:
        kokoro = (
            "[ :heart: :heart: :heart: :heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 50:
        kokoro = (
            "[ :heart: :heart: :heart: :heart: :heart: :black_heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 60:
        kokoro = (
            "[ :heart: :heart: :heart: :heart: :heart: :heart: :black_heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 70:
        kokoro = (
            "[ :heart: :heart: :heart: :heart: :heart: :heart: :heart: :black_heart: :black_heart: :black_heart: ]")
    elif a <= 80:
        kokoro = ("[ :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :black_heart: :black_heart: ]")
    elif a <= 90:
        kokoro = ("[ :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :black_heart: ]")
    elif a <= 100:
        kokoro = ("[ :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: ]")
    kokorofunny = ("[ :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: :heart: ]")
    if avamember.id in {338474093743439872} and avamember2.id in {397928612906532865} and avamember3.id in {
        658342427546877994} and avamember4.id in {133218314469113857} and avamember5.id in {389850804607254528}:
        msg = (
            f"Person 1: {avamember.mention}\nPerson 2: {avamember2.mention}\nPerson 3: {avamember3.mention}\nPerson 4: {avamember4.mention}\nPerson 5: {avamember5.mention}\nRating: {kokorofunny} (100%)")
    else:
        msg = (
            f"Person 1: {avamember.mention}\nPerson 2: {avamember2.mention}\nPerson 3: {avamember3.mention}\nPerson 4: {avamember4.mention}\nPerson 5: {avamember5.mention}\nRating: {kokoro} ({a}%)")
    await ctx.send(msg)


@bot.command()
async def convert(ctx, num, type, type2):
    if type == "days":
        if type2 == "hours":
            a = int(num) * 24
            await ctx.send(a)
        if type2 == "seconds":
            a = int(num) * 3600


@bot.command()
async def bmi(ctx, kg, cm):
    try:
        height = float(cm)
        weight = float(kg)

        bmi = weight / (height ** 2)

        if (bmi < 5):
            a = ("wtf")

        elif (bmi < 16):
            a = ("severely underweight (((((are you a femboy???))))) :warning:")

        elif (bmi >= 16 and bmi < 18.5):
            a = ("underweight :information_source:")

        elif (bmi >= 18.5 and bmi < 26):
            a = ("Healthy :white_check_mark: ")

        elif (bmi >= 26 and bmi < 30):
            a = ("overweight :warning:")

        elif (bmi >= 30):
            a = ("severely overweight :warning:")

        await ctx.send(f"Your BMI is `{bmi}` and you are\n{a}")
    except Exception as x:
        await ctx.send(f"an error occured\n```{x}```")


@bot.command()
async def say(ctx, *, what):
    if "@everyone" in ctx.message.content or "@here" in ctx.message.content:
        await ctx.send("everyone/here ping detected, aborting...")
    else:
        await ctx.message.delete()
        await ctx.send(what)


@bot.command()
async def avatar(ctx, avamember: discord.User = None):
    msg = (f"`{avamember.name}#{avamember.discriminator}'s avatar is` {avamember.avatar_url}")
    await ctx.send(msg)


@bot.command()
async def dict(ctx, *, word):
    try:
        dictionary = PyDictionary()
        a = (dictionary.meaning(word))
        b = (a["Noun"])
        await ctx.send(f"Noun:\n{b}")
    except Exception as x:
        await ctx.send(f"an error occured:\n```{x}```")


@bot.command()
async def wordcloud(ctx, range):
    await ctx.send(f"ok generating wordcloud for {range} message, please wait (this may take a while)")
    a = int(range)
    messages = await ctx.channel.history(limit=a).flatten()

    with open("channel_messages.txt", 'w', encoding='utf-8') as f:
        for msg in messages:
            lol = (msg.content + '\n')
            f.write(lol)
    os.system("wordcloud_cli --width 1920 --height 1080 --text channel_messages.txt --imagefile wordcloud.png")
    await ctx.send("successfully generated", file=discord.File("wordcloud.png"))
    os.remove("channel_messages.txt")
    os.remove("wordcloud.png")


@bot.command()
async def iplocation(ctx, ip):
    try:
        url = f"https://api.ipgeolocation.io/ipgeo?apiKey=&ip={ip}"
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}
        r = requests.get(url, headers=headers)
        s = r.json()

        ip = (s['ip'])
        continent = (s['continent_name'])
        country = (s['country_name'])
        capital = (s['country_capital'])
        city = (s['city'])
        district = (s['district'])
        lat = (s['latitude'])
        lon = (s['longitude'])
        eu = (s['is_eu'])
        callingcode = (s['calling_code'])
        isp = (s['isp'])
        organization = (s['organization'])
        flag = (s['country_flag'])

        embed = discord.Embed(title="IPInfo", color=0x2d3dff)
        embed.set_thumbnail(url=flag)
        embed.add_field(name="IP", value=ip, inline=True)
        embed.add_field(name="Continent", value=continent, inline=True)
        embed.add_field(name="Country", value=country, inline=True)
        embed.add_field(name="Country Capital", value=capital, inline=True)
        embed.add_field(name="Latitude", value=lat, inline=True)
        embed.add_field(name="Longitude", value=lon, inline=True)
        embed.add_field(name="ISP", value=isp, inline=True)
        embed.add_field(name="Organization", value=organization, inline=True)
        embed.add_field(name="Is EU", value=eu, inline=True)
        embed.add_field(name="Calling code", value=callingcode, inline=True)

        await ctx.send(embed=embed)
    except Exception as x:
        await ctx.send(f"An error occured\n```{x}```")


@bot.command()
async def img(ctx, *, term):
    a = await ctx.send("Contacting API <:load:757718569978036314>")

    gis = GoogleImagesSearch('', '
    :wilie2bh9p4')
    _search_params = {
        'q': term,
        'num': 1,
        'safe': 'off',
    }

    gis.search(search_params=_search_params)
    for image in gis.results():
        global url
        url = (image.url)

    embed1 = discord.Embed(title="Image search result", description=f"`{term}`", color=0x0000ff)
    embed1.set_image(url=f"{url}")
    embed1.set_footer(text=f"Page 1")

    await a.delete()

    await ctx.send(embed=embed1)


@bot.command()
async def osu(ctx, action, *, inp):
    if action == "user":
        try:
            url = f"https://osu.ppy.sh/api/get_user?u={inp}&k="
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
            }

            r = requests.get(url, headers=headers)
            s = r.json()

            user_id = (s[0]['user_id'])
            username = (s[0]['username'])
            join_date = (s[0]['join_date'])
            ranked_score = (s[0]['ranked_score'])
            total_score = (s[0]['total_score'])
            pp_rank = (s[0]['pp_rank'])
            accuracy = (s[0]['accuracy'])
            count_rank_ss = (s[0]['count_rank_ss'])
            total_seconds_played = (s[0]['total_seconds_played'])
            country = (s[0]['country'])
            pp_country_rank = (s[0]['pp_country_rank'])
            playcount = (s[0]['playcount'])
            pp_raw = (s[0]['pp_raw'])

            lowercountry = (country.lower())

            icon_url = f"http://s.ppy.sh/a/{user_id}"
            time = int(total_seconds_played) / 3600

            embed = discord.Embed(title="User search", description=username)
            embed.set_author(name="Osu!",
                             icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Osu%21Logo_%282015%29.png/600px-Osu%21Logo_%282015%29.png")
            embed.set_thumbnail(url=icon_url)
            embed.add_field(name="User ID", value=user_id, inline=True)
            embed.add_field(name="Username", value=username, inline=True)
            embed.add_field(name="Join Date", value=join_date, inline=True)
            embed.add_field(name="Ranked Score", value=ranked_score, inline=True)
            embed.add_field(name="Total Score", value=total_score, inline=True)
            embed.add_field(name="PP Rank", value=pp_rank, inline=True)
            embed.add_field(name="Accuracy", value=accuracy, inline=True)
            embed.add_field(name="Count rank SS", value=count_rank_ss, inline=True)
            embed.add_field(name="Total seconds played", value=f"{total_seconds_played} ({round(time)} hours)",
                            inline=True)
            embed.add_field(name="Country", value=f"{country} :flag_{lowercountry}:", inline=True)
            embed.add_field(name="PP Country rank", value=pp_country_rank, inline=True)
            embed.add_field(name="Raw PP", value=pp_raw, inline=True)
            embed.add_field(name="Play Count", value=playcount, inline=True)
            embed.set_footer(text="Funny cat - Powered by Osu! API")
            await ctx.send(embed=embed)
        except Exception as x:
            await ctx.send(f"An error occured ```{x}```")

    elif action == "beatmap" or action == "map":
        try:
            url = f"https://osu.ppy.sh/api/get_beatmaps?b={inp}&k="
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
            }

            r = requests.get(url, headers=headers)
            s = r.json()

            beatmap_id = (s[0]['beatmap_id'])
            approved = (s[0]['approved'])
            total_length = (s[0]['total_length'])
            hit_length = (s[0]['hit_length'])
            version = (s[0]['version'])
            diff_size = (s[0]['diff_size'])
            count_normal = (s[0]['count_normal'])
            count_slider = (s[0]['count_slider'])
            count_spinner = (s[0]['count_spinner'])
            title = (s[0]['title'])
            artist = (s[0]['artist'])
            source = (s[0]['source'])
            bpm = (s[0]['bpm'])
            submit_date = (s[0]['submit_date'])
            creator = (s[0]['creator'])
            favourite_count = (s[0]['favourite_count'])
            rating = (s[0]['rating'])
            playcount = (s[0]['playcount'])
            passcount = (s[0]['passcount'])
            difficultyrating = (s[0]['difficultyrating'])
            tags = (s[0]['tags'])

            cover = f"https://assets.ppy.sh/beatmaps/{beatmap_id}/covers/cover.jpg"
            thumb = f"https://b.ppy.sh/thumb/{beatmap_id}l.jpg"

            embed = discord.Embed(title="Beatmap search", description="5456156")
            embed.set_author(name="Osu!",
                             icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Osu%21Logo_%282015%29.png/600px-Osu%21Logo_%282015%29.png")
            embed.set_thumbnail(url=thumb)
            embed.add_field(name="Beatmap ID", value=beatmap_id, inline=True)
            embed.add_field(name="Approved", value=approved, inline=True)
            embed.add_field(name="Total Length", value=total_length, inline=True)
            embed.add_field(name="Hit Length", value=hit_length, inline=True)
            embed.add_field(name="Difficulty", value=version, inline=True)
            embed.add_field(name="Diff Size", value=diff_size, inline=True)
            embed.add_field(name="Circle Count", value=count_normal, inline=True)
            embed.add_field(name="Slider Count", value=count_slider, inline=True)
            embed.add_field(name="Spinner Count", value=count_spinner, inline=True)
            embed.add_field(name="Song Title", value=title, inline=True)
            embed.add_field(name="Song Artist", value=artist, inline=True)
            embed.add_field(name="Source", value=source, inline=True)
            embed.add_field(name="BPM", value=bpm, inline=True)
            embed.add_field(name="Submit date", value=submit_date, inline=True)
            embed.add_field(name="Creator", value=creator, inline=True)
            embed.add_field(name="Favourite Count", value=favourite_count, inline=True)
            embed.add_field(name="Rating", value=rating, inline=True)
            embed.add_field(name="Play Count", value=playcount, inline=True)
            embed.add_field(name="Pass Count", value=passcount, inline=True)
            embed.add_field(name="Difficulty Rating", value=difficultyrating, inline=True)
            embed.add_field(name="Tags", value=tags, inline=True)
            embed.set_image(url=cover)
            embed.set_footer(text="Funny cat - Powered by Osu! API")
            await ctx.send(embed=embed)
        except Exception as x:
            await ctx.send(f"An error occured ```{x}```")


@bot.command()
async def tempconvert(ctx, unit, inp):
    if unit == "c" or unit == "celsius":
        a = int(inp)
        converted = (a * 9 / 5) + 32
        await ctx.send(f"**{inp}°C** Is equal to **{converted}°F**")
    elif unit == "f" or unit == "fahrenheit":
        a = int(inp)
        converted = (a - 32) * 5 / 9
        await ctx.send(f"**{inp}°F** Is equal to **{converted}°C**")


@bot.command()
async def speedconvert(ctx, unit, number):
    if unit == "mph" or unit == "miles":
        a = int(number)
        converted = a / 1.609
        await ctx.send(f"**{number} Km/h** is equal to approximately **{converted} Mph**")
    elif unit == "kph" or unit == "kilometer":
        a = int(number)
        converted = a * 1.609
        await ctx.send(f"**{number} Mph** is equal to approximately **{converted} Km/h**")


@bot.command()
async def weightconvert(ctx, unit, number):
    if unit == "kg":
        a = int(number)
        converted = a / 2.205
        await ctx.send(f"**{number} Pounds** is equal to **{converted} Kg**")
    elif unit == "pounds":
        a = int(number)
        converted = a * 2.205
        await ctx.send(f"**{number} Kg** is equal to **{converted} Pounds**")


@bot.command()
async def delete(ctx, msgid):
    if ctx.author.id in {133218314469113857}:
        await ctx.message.delete()
        msg = await ctx.channel.fetch_message(msgid)
        await msg.delete()
        await ctx.send(f"Deleted `{msgid}`")
    else:
        await ctx.send("bot owner only :///")


@bot.command()
async def urban(ctx, *, word):
    try:
        url = f"http://api.urbandictionary.com/v0/define?term={word}"
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

        r = requests.get(url, headers=headers)

        s = r.json()

        word = (s['list'][0]['word'])
        definition = (s['list'][0]['definition'])
        example = (s['list'][0]['example'])

        defformatted = definition.replace("[", "")
        defformatted2 = defformatted.replace("]", "")

        exampleformatted = example.replace("[", "")
        exampleformatted2 = exampleformatted.replace("]", "")

        embed = discord.Embed(title=word)
        embed.set_author(name="Urban Dictionary", icon_url="https://img.utdstc.com/icons/urban-dictionary-android.png")
        embed.set_thumbnail(url="https://img.utdstc.com/icons/urban-dictionary-android.png")
        embed.add_field(name="Definition", value=defformatted2, inline=True)
        embed.add_field(name="Example", value=exampleformatted2, inline=True)
        await ctx.send(embed=embed)
    except Exception as x:
        await ctx.send(f"An error occured ```{x}```")


@bot.command()
async def ping(ctx):
    ping = subprocess.Popen(
        ["ping", "-c", "1", "google.com"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, error = ping.communicate()
    await ctx.send(out)


@bot.command()
async def typing(ctx):
    await ctx.message.delete()
    async with ctx.typing():
        sleep(25)


@bot.command()
async def pocky(ctx, person, person2):
    inp1spaces = person.replace("-", " ")
    inp2spaces = person2.replace("-", " ")
    try:
        await ctx.message.delete()
    except:
        pass
    image = Image.open('pockytemplate.png')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Prototype.ttf', size=45)

    (x, y) = (50, 50)
    message = inp1spaces
    color = 'rgb(0, 0, 0)'  # black color

    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (380, 97)
    message = inp2spaces
    color = 'rgb(0, 0, 0)'  # black color

    draw.text((x, y), message, fill=color, font=font)

    image.save('pocky.png')
    await ctx.send(file=discord.File("pocky.png"))
    os.remove("pocky.png")


@bot.command()
async def translate(ctx, fro, to, *, inputt):
    translator = Translator(from_lang=fro, to_lang=to)
    translation = translator.translate(inputt)
    message = ("Translation from `{0}` to `{1}`\n```{2}```").format(fro, to, translation)
    await ctx.channel.send(message)


@bot.command()
async def whatanime(ctx, url: str = None):
    try:
        if not ctx.message.attachments:
            await ctx.channel.send("Searching...")
            videoname = ('GFS-ANIME_{0}.mp4').format(ctx.message.id)
            tracemoe = tracemoepy.tracemoe.TraceMoe()
            link = ('{0}').format(url)
            output = tracemoe.search(link, is_url=True)
            video = tracemoe.video_preview(output)
            with open(videoname, 'wb') as f:
                f.write(video)
            result = output['docs'][0]
            title = (f"**Title**: {result['title_english']}")
            ogtitle = (f"**Original Title**: {result['title_native']}")
            romaji = (f"{result['title_romaji']}")
            year = (f"**Year**: {result['season']}")
            Episode = (f"**Episode**: {result['episode']}")
            similarity = (f"**Similarity**: {str(result['similarity'])[2]}")
            adult = (f"{result['is_adult']}")
            at = (f"**Timestamp**: {str(result['from'])[1]}")
            msg = ("{0}\n{1} | {6}\n{2}\n{3}\n{4} minutes\n{5}").format(title, ogtitle, year, Episode, at, similarity,
                                                                        romaji)

            if adult == "True":
                if ctx.channel.is_nsfw():
                    await ctx.channel.send(msg, file=discord.File(videoname))
                    os.remove(videoname)
                else:
                    await ctx.channel.send(
                        "Can't send NSFW Result in SFW Channel! (Try running the command in an NSFW channel)")
                    os.remove(videoname)
            elif adult == "False":
                await ctx.channel.send(msg, file=discord.File(videoname))
            else:
                await ctx.channel.send("An error occured, Please try again.")



        else:
            await ctx.channel.send("Searching...")
            attachmenturl = (""'{}'"").format(ctx.message.attachments[0].url)
            attachmentfilename = (""'{0}'"").format(ctx.message.attachments[0].filename)
            attachmentname = ('GFS-ANIME{0}-{1}').format(ctx.message.id, attachmentfilename)
            videoname = ('GFS-ANIME_{0}.mp4').format(ctx.message.id)

            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
            }
            r = requests.get(attachmenturl, headers=headers, stream=True)
            with open(attachmentname, 'wb') as out_file:
                shutil.copyfileobj(r.raw, out_file)
            del r

            tracemoe = tracemoepy.tracemoe.TraceMoe()
            link = ('{0}').format(url)
            output = tracemoe.search(attachmentname, encode=True)
            video = tracemoe.video_preview(output)

            result = output['docs'][0]
            title = f"**Title**: {result['title_english']}"
            ogtitle = f"**Original Title**: {result['title_native']}"
            romaji = f"{result['title_romaji']}"
            year = f"**Year**: {result['season']}"
            Episode = f"**Episode**: {result['episode']}"
            similarity = f"**Similarity**: {str(result['similarity'])[2]}"
            adult = f"{result['is_adult']}"
            at = f"**Timestamp**: {str(result['from'])[1]}"
            msg = "{0}\n{1} | {6}\n{2}\n{3}\n{4} minutes\n{5}".format(title, ogtitle, year, Episode, at, similarity,
                                                                      romaji)

            if adult == "True":
                if ctx.channel.is_nsfw():
                    await ctx.channel.send(msg)
                    await ctx.send(video)
                else:
                    await ctx.channel.send(
                        "Can't send NSFW Result in SFW Channel! (Try running the command in an NSFW channel)")
            elif adult == "False":
                await ctx.channel.send(msg)
                await ctx.send(video)
            else:
                await ctx.channel.send("An error occured, Please try again.")
    except Exception as x:
        print(x)
        exc = (":boom: **Error**```{0}```").format(x)
        await ctx.channel.send(exc)


@bot.command()
async def servers(ctx):
    a = str(len(bot.guilds))
    b = ""
    for name in bot.guilds:
        b += f"{name}\n"
    await ctx.send(f"Bot is in {a} servers.\n```{b}```")

# This part of the code is for the 2 person image reactions
# The paths may be incorrect
# Update them accordingly when self hosting this bot

@bot.command()
async def hugging(ctx, person, person2):
    inp1spaces = person.replace("-", " ")
    inp2spaces = person2.replace("-", " ")
    try:
        await ctx.message.delete()
    except:
        pass
    image = Image.open('hugtemplate.png')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Prototype.ttf', size=45)

    (x, y) = (182, 262)
    message = inp1spaces
    color = 'rgb(0, 0, 0)'  # black color

    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (433, 555)
    message = inp2spaces
    color = 'rgb(0, 0, 0)'  # black color

    draw.text((x, y), message, fill=color, font=font)

    image.save('hug.png')
    await ctx.send(file=discord.File("hug.png"))
    os.remove("hug.png")


@bot.command()
async def kissing(ctx, person, person2):
    inp1spaces = person.replace("-", " ")
    inp2spaces = person2.replace("-", " ")
    try:
        await ctx.message.delete()
    except:
        pass
    image = Image.open('kisstemplate.jpg')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Prototype.ttf', size=45)

    (x, y) = (420, 288)
    message = inp1spaces
    color = 'rgb(255, 255, 255)'  # white color

    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (589, 316)
    message = inp2spaces
    color = 'rgb(255, 255, 255)'  # white color

    draw.text((x, y), message, fill=color, font=font)

    image.save('kiss.png')
    await ctx.send(file=discord.File("kiss.png"))
    os.remove("kiss.png")

@bot.command()
async def drinking(ctx, person, person2):
    inp1spaces = person.replace("-", " ")
    inp2spaces = person2.replace("-", " ")
    try:
        await ctx.message.delete()
    except:
        pass
    image = Image.open('drinktemplate.png')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Prototype.ttf', size=45)

    (x, y) = (157, 263)
    message = inp1spaces
    color = 'rgb(255, 0, 0)'  # red color

    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (485, 227)
    message = inp2spaces
    color = 'rgb(255, 0, 0)'  # red color

    draw.text((x, y), message, fill=color, font=font)

    image.save('drink.png')
    await ctx.send(file=discord.File("drink.png"))
    os.remove("drink.png")


@bot.command()
async def shinji(ctx, person, person2):
    inp1spaces = person.replace("-", " ")
    inp2spaces = person2.replace("-", " ")
    try:
        await ctx.message.delete()
    except:
        pass
    image = Image.open('shinjitemplate.png')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('Prototype.ttf', size=45)

    (x, y) = (157, 252)
    message = inp1spaces
    color = 'rgb(255, 0, 0)'  # red color

    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (409, 106)
    message = inp2spaces
    color = 'rgb(255, 0, 0)'  # red color

    draw.text((x, y), message, fill=color, font=font)

    image.save('shinji.png')
    await ctx.send(file=discord.File("shinji.png"))
    os.remove("shinji.png")



@bot.command()
async def repeat(ctx, num, *, content):
    if num > 5:
        await ctx.send("maximum number of repeats is 5.")
    else:
        for i in range(num):
            await ctx.send(content)

@bot.command()
async def duckduckgo(ctx, term, num : int = 0):
    try:
        url = f"https://api.duckduckgo.com/?q={term}&format=json&pretty=1"
        headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

        r = requests.get(url, headers=headers)

        s = r.json()

        url = (s['RelatedTopics'][num]['FirstURL'])
        icon = (s['RelatedTopics'][num]['Icon']['URL'])
        text = (s['RelatedTopics'][num]['Text'])

        embed=discord.Embed(title="Search", url=url)
        embed.set_author(name="Duckduckgo", icon_url="https://upload.wikimedia.org/wikipedia/en/9/90/The_DuckDuckGo_Duck.png")
        embed.set_thumbnail(url=icon)
        embed.add_field(name=term, value=text, inline=True)
        embed.set_footer(icon_url=f"{ctx.author.avatar_url}", text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}")

        await ctx.send(embed=embed)
    except:
        await ctx.send("An error occured (Empty JSON)")

def neko(reaction):
    if reaction == "kiss":
        lines = open("nekos/kiss.txt").read().splitlines()
        joke = random.choice(lines)
    elif reaction == "hug":
        lines = open("nekos/hug.txt").read().splitlines()
        joke = random.choice(lines)
    elif reaction == "poke":
        lines = open("nekos/poke.txt").read().splitlines()
        joke = random.choice(lines)
    return joke

@bot.command()
async def kiss(ctx, person : discord.User=None):
    a = neko("kiss")
    await ctx.send(f"{ctx.author.mention} Kissed {person.mention}\n{a}")

@bot.command()
async def hug(ctx, person : discord.User=None):
    a = neko("hug")
    await ctx.send(f"{ctx.author.mention} Hugged {person.mention}\n{a}")

@bot.command()
async def poke(ctx, person : discord.User=None):
    a = neko("poke")
    await ctx.send(f"{ctx.author.mention} Poked {person.mention}\n{a}")

@bot.command()
async def gelbooru(ctx, tags, num : int = 0):
    url = f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&tags={tag}&json=1"

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

    r = requests.get(url, headers=headers)
    s = r.json()

    imgid = (s[0]['id'])
    rating = (s[0]['rating'])
    hashimg = (s[0]['hash'])

    source = (s[0]['source'])
    tags = (s[0]['tags'])
    image = (s[0]['file_url'])

    embed1=discord.Embed(title="Gelbooru Search", color=0xc290c6)
    embed1.add_field(name="ID:", value=imgid, inline=False)
    embed1.add_field(name="Rating:", value=rating, inline=False)
    embed1.add_field(name="Source:", value=source, inline=False)
    embed1.add_field(name="Tags:", value=tags, inline=False)
    embed1.set_footer(text=f"Hash: {hashimg} ")
    embed1.set_image(url=image)
    await ctx.send(embed=embed1)

@bot.command()
async def urlcheck(ctx, url):
    try:
        line_count = 0

        o = urlparse(url)
        domain = o.netloc
        if domain == "":
            await ctx.send("Invalid link")
            return

        await ctx.send(f"Checking `{url}`")
        with open("/home/sosoplayz/vps-backup/useful/iplog/iploggers.txt") as f:
            for line in f:
                line_count += 1
                if domain in line:
                    await ctx.send(f":octagonal_sign: The provided link is an IP Logger\nProvided link: `{url}`\nDatabase Match: `{line}`")
                    return
        await ctx.send(f"`{url}` Is safe :white_check_mark:, Scanned out of {line_count} URLs\n{domain}")
    except Exception as x:
        await ctx.send(f"Error: ```{x}```")


@bot.command()
async def lyrics(ctx, *, song):

    ss = song.replace(" ", "%20")
    url = f"https://some-random-api.ml/lyrics?title={ss}"

    r = requests.get(url)
    s = r.json()

    title = (s['title'])
    author = (s['author'])
    lyrics = (s['lyrics'])
    thumbnail = (s['thumbnail']['genius'])
    link = (s['links']['genius'])

    formatted_lyrics = lyrics.replace('\\n', '\n').replace('\\t', '\t')[:1024]

    embed1=discord.Embed(title="Lyrics Search", color=0xc290c6)
    embed1.set_thumbnail(url=thumbnail)
    embed1.add_field(name="Title:", value=title, inline=True)
    embed1.add_field(name="Author:", value=author, inline=False)
    embed1.add_field(name="Lyrics:", value=formatted_lyrics, inline=False)
    embed1.set_footer(text=f"Link: {link}")

    await ctx.send(embed=embed1)

    if len(lyrics) > 1024:
        await ctx.send(f"```{formatted_lyrics}```")


@bot.command()
async def aita(ctx):

    rs = requests.get(f"https://www.random.org/integers/?num=1&min=0&max=25&col=1&base=10&format=plain&rnd=new")
    qs = (rs.text)
    q = int(qs)


    url = "https://www.reddit.com/r/amitheasshole.json"
    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

    r = requests.get(url, headers=headers)
    s = r.json()

    title = (s['data']['children'][q]['data']['title'])
    content = (s['data']['children'][q]['data']['selftext'])

    formatted_content = content.replace('\\n', '\n').replace('\\t', '\t')

    msg = (f"{title}\n\n{formatted_content}")[:2000]

    await ctx.send(msg)

@bot.command()
async def tag(ctx, mode, *, insertion : str = None):
    # some variables
    authorid = ctx.author.id
    currenttime = f"{datetime.date(datetime.now())} At {datetime.time(datetime.now())} GMT +3"
    if insertion != None:
        firstword = insertion.split(' ')[0]
        try:
            secondword = insertion.split(' ')[1]
        except:
            pass
        try:
            formatinsertion = insertion.split(' ', 1)[1]
        except:
            pass

    if mode == "add":
        if "@everyone" in insertion or "@here" in insertion:
            await ctx.send("no")
        else:
            if secondword == "" or secondword == None:
                await ctx.send("content can't be empty")
            else:
                sql = 'INSERT INTO TAG (id, name, content, date) values(?, ?, ?, ?)'
                data = [
                    (authorid, firstword, formatinsertion, currenttime),
                ]
                with connection:
                    connection.executemany(sql, data)
                await ctx.send(f"Tag `{firstword}` Successfully added.")

    elif mode == "delete":
        with connection:
            data = connection.execute(f"SELECT * FROM TAG WHERE name LIKE '{mode}'")
            for row in data:
                a = (row[0])
        if ctx.author.id == a:
            data = connection.execute(f"DELETE FROM TAG WHERE name LIKE '{firstword}'")
            await ctx.send(f"Successfully deleted tag `{firstword}`")
        else:
            await ctx.send(f"{ctx.author.mention} You do not have permission to delete the `{firstword}` tag.")

    elif mode == "list":
        taglist = ""
        data = connection.execute(f"SELECT * FROM TAG WHERE id LIKE '{authorid}'")
        for row in data:
            name = (row[1])
            date = (row[3])
            taglist += (f"`{name}` Created on `{date}`\n")

        await ctx.send(f"List of tags owned by `{ctx.author.name}#{ctx.author.discriminator}`:\n{taglist}")

    else:
        with connection:
            data = connection.execute(f"SELECT * FROM TAG WHERE name LIKE '{mode}'")
            for row in data:
                a = (row[2])
                await ctx.send(a)

@bot.command()
async def invite(ctx):
    await ctx.send(f"{ctx.author.mention} https://discord.com/api/oauth2/authorize?client_id=754720671518687322&permissions=125952&scope=bot")

@bot.command()
async def politeness(ctx, *, inputt):

    formatted_input = inputt.replace(" ", "+")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox'}
    data = {'text': formatted_input}

    r = requests.post('https://politeness.cornell.edu/score-politeness', headers=headers, data=data)
    s = r.json()

    confidence = (s['confidence'])
    label = (s['label'])

    await ctx.send(f"Label: {label}\nConfidence: {confidence}")

@bot.command()
async def fraudcheck(ctx, *, ip):
    url = (f"https://ipqualityscore.com/api/json/ip/APIKEYHERE/{ip}?strictness=0&allow_public_access_points=true&fast=true&lighter_penalties=true&mobile=true")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox'}
    r = requests.post(url, headers=headers)
    s = r.json()

    fraud_score = (s['fraud_score'])
    country_code = (s['country_code'])
    city = (s['city'])
    ISP = (s['ISP'])
    ASN = (s['ASN'])
    host = (s['host'])
    proxy = (s['proxy'])
    vpn = (s['vpn'])
    tor = (s['tor'])
    recent_abuse = (s['recent_abuse'])
    bot_status = (s['bot_status'])
    request_id = (s['request_id'])

    msg = f"```Fraud score: {fraud_score}\nCountry Code: {country_code}\nCity: {city}\nISP: {ISP}\nASN: {ASN}\nHost: {host}\nProxy: {proxy}\nVPN: {vpn}\nTOR: {tor}\nRecent Abuse: {recent_abuse}\nBot Status: {bot_status}\nRequest ID: {request_id}```"

    await ctx.send(msg)

def saucesearch(url):
    url = (f"https://saucenao.com/search.php?api_key=25fe684c5e5981db9fcdab3fdd9b019e5afcb839&db=999&output_type=2&testmode=1&numres=16&url={url}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox'}
    r = requests.post(url, headers=headers)
    s = r.json()

    limit = (s['header']['long_remaining'])

    simres0 = (s['result'][0]['header']['similarity'])
    indexnameres0 = (s['result'][0]['header']['index_name'])
    urlres0 = (s['result'][0]['data']['ext_urls'[0]])

    simres1 = (s['result'][1]['header']['similarity'])
    indexnameres1 = (s['result'][1]['header']['index_name'])
    urlres1 = (s['result'][1]['data']['ext_urls'[0]])

    simres2 = (s['result'][2]['header']['similarity'])
    indexnameres2 = (s['result'][2]['header']['index_name'])
    urlres2 = (s['result'][2]['data']['ext_urls'[0]])

    msg = f"Sauce found:\nSearches remaining for today: {limit}\n```Result 1:\nSimilarity: {simres0}\nIndex Name: {indexnameres0}\nURL: {urlres0}\n\nResult 2:\nSimilarity: {simres1}\nIndex Name: {indexnameres1}\nURL: {urlres1}\n\nResult 3:\nSimilarity: {simres2}\nIndex Name: {indexnameres2}\nURL: {urlres2}"

@bot.command()
async def sauce(ctx, link : str = None):
    if not ctx.message.attachments:
        await ctx.channel.send("Searching...")

    else:
        await ctx.channel.send("Searching...")
        link = (""'{}'"").format(ctx.message.attachments[0].url)

    url = (f"https://saucenao.com/search.php?api_key=25fe684c5e5981db9fcdab3fdd9b019e5afcb839&db=999&output_type=2&testmode=1&numres=16&url={link}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox'}
    r = requests.post(url, headers=headers)
    s = r.json()

    limit = (s['header']['long_remaining'])

    simres0 = (s['results'][0]['header']['similarity'])
    indexnameres0 = (s['results'][0]['header']['index_name'])
    urlres0 = (s['results'][0]['data']['ext_urls'][0])

    simres1 = (s['results'][1]['header']['similarity'])
    indexnameres1 = (s['results'][1]['header']['index_name'])
    urlres1 = (s['results'][1]['data']['ext_urls'][0])

    simres2 = (s['results'][2]['header']['similarity'])
    indexnameres2 = (s['results'][2]['header']['index_name'])
    urlres2 = (s['results'][2]['data']['ext_urls'][0])

    await ctx.send(f"Sauce found:\nSearches remaining for today: {limit}\n```Result 1:\nSimilarity: {simres0}\nIndex Name: {indexnameres0}\nURL: {urlres0}\n\nResult 2:\nSimilarity: {simres1}\nIndex Name: {indexnameres1}\nURL: {urlres1}\n\nResult 3:\nSimilarity: {simres2}\nIndex Name: {indexnameres2}\nURL: {urlres2}```")

@bot.command()
async def sqlsearch(ctx, *, term): # Used for the memecord message Database
    match_count = 0
    with connection2:
        data = connection2.execute(f"SELECT * FROM LOGS WHERE content LIKE '{term}' COLLATE NOCASE")
        for row in data:
            match_count += 1
            dbid = (row[0])
            msgid = (row[1])
            authorname = (row[2])
            avatar = (row[3])
            chid = (row[4])
            userid = (row[5])
            content = (row[6])
            channelname = (row[7])
            timer = (row[8])

            msg = f"(temporary formatting)\nDB-ID: {dbid}\nMessage ID: {msgid}\nAuthor: {authorname}\nAvatar: `{avatar}`\nChannel ID: {chid}\nUser ID: {userid}\nContent: `{content}`\nTimestamp: {timer}\nMatch number: {match_count}"

            formattedname = f"{authorname} [ID: {userid}]"

            embed=discord.Embed(title=f"Search result for \n`{term}`", description=f"Match #{match_count} | Message ID: {msgid}", color=0x800040)
            embed.set_author(name=formattedname, icon_url=avatar)
            embed.add_field(name="Content:", value=content, inline=False)
            embed.set_footer(text=f"Touhoubot V2 \nChannel ID: {chid} \nTimestamp: {timer} (GMT +3)\nDatabase ID: {dbid}")
            await ctx.send(embed=embed)
            if match_count > 1:
                await ctx.send("Over 2 results found. Quitting!")
                return
        if match_count == 0:
            await ctx.send("No results found.")
            return
        await ctx.send("Execution successful.")


@bot.command()
async def yuri(ctx):
    lines = open("yurilist.txt").read().splitlines()
    yuri = secrets.choice(lines)
    await ctx.send(f"{yuri}")


@bot.command()
async def ruined(ctx, avamember : discord.User=None):
    await ctx.send(f"{avamember.mention} https://cdn.discordapp.com/attachments/769023126507356163/769630011770142740/fedora_2020_10_22__11_50_53.png")

@bot.command()
async def anchovy(ctx):
    lines = open("resources/anchovy.txt").read().splitlines()
    anchovy = secrets.choice(lines)
    await ctx.send(f"{anchovy}")

bot.run(TOKEN)
