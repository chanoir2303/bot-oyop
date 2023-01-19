import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from py_unite_db import UniteDb

load_dotenv(dotenv_path="config")  # load token in config file
unite_db = UniteDb()  # load unite-db REST API

# discord app config
default_intents = discord.Intents.all()
default_intents.members = True
bot = commands.Bot(command_prefix="!", intents=default_intents)

# list of word for bot event
words = ['bagarre', 'unite', 'go']


@bot.event
async def on_ready():
    print("oyop prêt pour bagarre.")


@bot.event
async def on_message(message):
    if message.content == "ping":
        await message.channel.send("pong")

    if message.content in words:
        await message.channel.send("la bagarre y'a que ca de vrai.")

    if message.content == "poyo":
        emoji = '❤️'
        await message.add_reaction(emoji)

    await bot.process_commands(message)


# display all commands available
@bot.command(name="commands")
async def help_commands(ctx):
    await ctx.send("""
    all commands:
    !stats <name> to display pokemon stats
    !attacker to display list of attackers
    !jungler to display list of junglers
    !defender to display list of defenders
    !polyvalent to display list of polyvalents
    !support to display list of supports
    !wizz
    !author
    """)


# display developer contact
@bot.command(name="author")
async def author(ctx):
    await ctx.send("chanoir2303 - https://github.com/chanoir2303 - https://twitter.com/chanoir2303")


# list all support type pokemon
@bot.command(name="support")
async def support(ctx):
    list_support = []
    for p in unite_db.pokemon:
        if p.role == "Supporter":
            list_support.append(p.name)
    await ctx.send(list_support)


# list all jungler type pokemon
@bot.command(name="jungler")
async def jungler(ctx):
    list_jungler = []
    for p in unite_db.pokemon:
        if p.role == "Speedster":
            list_jungler.append(p.name)
    await ctx.send(list_jungler)


# list all defender type pokemon
@bot.command(name="defender")
async def defender(ctx):
    list_defender = []
    for p in unite_db.pokemon:
        if p.role == "Defender":
            list_defender.append(p.name)
    await ctx.send(list_defender)


# list all polyvalent type pokemon
@bot.command(name="polyvalent")
async def polyvalent(ctx):
    list_polyvalent = []
    for p in unite_db.pokemon:
        if p.role == "All-Rounder":
            list_polyvalent.append(p.name)
    await ctx.send(list_polyvalent)


# list all attacker type pokemon
@bot.command(name="attacker")
async def attacker(ctx):
    list_attacker = []
    for p in unite_db.pokemon:
        if p.role == "Attacker":
            list_attacker.append(p.name)
    await ctx.send(list_attacker)


# search stats for specific pokemon
@bot.command(name="stats")
async def search_pokemon_stats(ctx, name):
    x = []
    for i in unite_db.pokemon:
        if i.name == name:
            x.append(i.stats[0])
    await ctx.send(x)

# spam salty peeps
@bot.command(name="wizz")
@commands.cooldown(1, 600, commands.BucketType.user) # nbr times, nbr seconds
async def salty(ctx, name):
    print(name)
    for i in range(0, 15):
        if name == "<@919292102456803378>":
            break
        else:
            await ctx.send(name)


# TODO: MVP command

bot.run(os.getenv("TOKEN"))
