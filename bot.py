# bot.py
import os
import random

import discord
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def rolldice(nsides, ndice):
    dice = [
        str(random.choice(range(1, int(nsides) + 1)))
        for _ in range(int(ndice))     
    ]
    return dice

#client = discord.Client()
@bot.command(name='roll', help="Dice are being thrown!\nUse format <numberofdice>d<numberofsides>. EX: !roll 2d6 rolls two six sided dice.\nFor multiple dice, separate them with the word 'and'. EX: !roll 2d6 and 3d4 rolls two six sided dice and three four sided dice.")
async def roll(ctx, *user_input):
    user_input = ''.join(user_input)
    if 'and' in user_input:
        rolls=user_input.replace(' ','').split('and')
        sumdice=0
        for i in range(len(rolls)):
            ndice,nsides = rolls[i].split('d')
            dice = rolldice(nsides, ndice)
            sumdice += sum([int(i) for i in dice])
            await ctx.send("{}: {}".format(rolls[i],', '.join(dice)))
        await ctx.send("Total = {}".format(sumdice))
    else:
        ndice,nsides = user_input.split('d')
        dice = rolldice(nsides, ndice)
        sumdice = sum([int(i) for i in dice])
        if len(dice) > 1:
            await ctx.send("{} \nTotal = {}".format(', '.join(dice),sumdice))
        else:
            await ctx.send(dice[0])

@bot.command(name='Ping', help='ping pong bb you know what it is')
async def ping(ctx):
    await ctx.send('Pong')

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

bot.run(TOKEN)