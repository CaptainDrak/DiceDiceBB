# bot.py
import os
import random
import dotenv

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def roll_dice(nsides, ndice):
    dice = [
        str(random.choice(range(1, int(nsides) + 1)))
        for _ in range(int(ndice))     
    ]
    return dice

def multi_type_roll(user_input):
    rolls=user_input.replace(' ','').split('and')
    sumdice=0
    messages=[]
    for i in range(len(rolls)):
        ndice,nsides = rolls[i].split('d')
        dice = roll_dice(nsides, ndice)
        sumdice += sum([int(i) for i in dice])
        print(f"{rolls[i]}: {', '.join(dice)}")
        messages.append(f"{rolls[i]}: {', '.join(dice)}")
        print(f"Message to be returned to roll request: {messages}")
    print(f"Total = {sumdice}")
    messages.append(f"Total = {sumdice}")
    print(f"Message to be returned to roll request: {messages}")
    return sumdice, messages

def single_type_roll(user_input):
    print(user_input)
    messages=[]
    ndice,nsides = user_input.split('d')
    dice = roll_dice(nsides, ndice)
    sumdice = sum([int(i) for i in dice])
    if len(dice) > 1:
        print(f"{', '.join(dice)} \nTotal = {sumdice}")
        messages.append(f"{', '.join(dice)} \nTotal = {sumdice}")
    else:
        print(f"Total = {dice[0]}")
        messages.append(f"Total = {dice[0]}")
    return sumdice, messages

@bot.command(name='roll', help="Dice are being thrown!\nUse format <numberofdice>d<numberofsides>. EX: !roll 2d6 rolls two six sided dice.\nFor multiple dice, separate them with the word 'and'. EX: !roll 2d6 and 3d4 rolls two six sided dice and three four sided dice.")
async def roll(ctx, *user_input):
    print(f"Initial, raw values being passed in: {user_input}")
    user_input = ' '.join(user_input)
    print(f"Actual user input: {user_input}")
    advantage = 'with advantage' in user_input
    user_input = user_input.replace('with advantage', '')
    print(f"User input stripped of potential advantage indicator: {user_input}")
    if advantage is True:
        print('advantage!')
    else:
        print('no advantage!')
    if 'and' in user_input:
        if advantage is True:
            sums = []
            for _ in range(2):
                this_roll = multi_type_roll(user_input)
                sums.append(this_roll[0])
                for i in range(len(this_roll[1])):
                    await ctx.send(this_roll[1][i])
            await ctx.send('Total with advantage = {}'.format(max(sums)))
        else:
            this_roll = multi_type_roll(user_input)
            for i in range(len(this_roll[1])):
                await ctx.send(this_roll[1][i])

    else:
        if advantage is True:
            sums = []
            for _ in range(2):
                this_roll = single_type_roll(user_input)
                sums.append(this_roll[0])
                for i in range(len(this_roll[1])):
                    await ctx.send(this_roll[1][i])
            await ctx.send(f'Total with advantage = {max(sums)}')
        else:
            this_roll = single_type_roll(user_input)
            for i in range(len(this_roll[1])):
                await ctx.send(this_roll[1][i])

@bot.command(name='ping', help='ping pong bb you know what it is')
async def ping(ctx):
    await ctx.send('Pong')

bot.run(TOKEN)