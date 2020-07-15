# bot.py
import os
import roll_mechanics

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='roll', help="Dice are being thrown!\nUse format <numberofdice>d<numberofsides>. EX: `!roll 2d6` rolls two six sided dice.\nFor multiple dice types, separate them with the word 'and'. EX: `!roll 2d6 and 3d4` rolls two six sided dice and three four sided dice.\nFor advantage or disadvantage, you can add the phrases `with advantage`, `w/ advantage`, `adv`, `with disadvantage`, `w/ disadvantage` or `dis`. EX: `!roll 1d20 adv` rolls two twenty sided dice, and keeps the highest value.  ")
async def roll(ctx, *user_input):
    sender = str(ctx.author).split('#', 1)[0]
    user_input = ' '.join(user_input)
    flags = [
            'with disadvantage', 
            'w/ disadvantage', 
            'with dis',
            'w/ dis', 
            'dis',
            'with advantage', 
            'w/ advantage', 
            'with adv',
            'w/ adv', 
            'adv'
            ]
    advantage = disadvantage = False
    if any(i in user_input for i in flags[0:5]):
        disadvantage = True
    elif any(i in user_input for i in flags[5:10]):
        advantage = True
    for i in range(len(flags)): user_input = user_input.replace(flags[i], '')
    if 'and' in user_input:
        if advantage is True:
            sums = []
            for _ in range(2):
                this_roll = roll_mechanics.multi_type_roll(user_input)
                sums.append(this_roll[0])
                await ctx.send(this_roll[1])
            await ctx.send(f"{sender}'s total with advantage = {max(sums)}")
        elif disadvantage is True:
            sums = []
            for _ in range(2):
                this_roll = roll_mechanics.multi_type_roll(user_input)
                sums.append(this_roll[0])
                await ctx.send(this_roll[1])
            await ctx.send(f"{sender}'s total with disadvantage = {min(sums)}")
        else:
            this_roll = roll_mechanics.multi_type_roll(user_input)
            await ctx.send(this_roll[1])

    else:
        if advantage is True:
            sums = []
            for _ in range(2):
                this_roll = roll_mechanics.single_type_roll(user_input)
                sums.append(this_roll[0])
                await ctx.send(this_roll[1])
            await ctx.send(f"{sender}'s total with advantage = {max(sums)}")
        elif disadvantage is True:
            sums = []
            for _ in range(2):
                this_roll = roll_mechanics.single_type_roll(user_input)
                sums.append(this_roll[0])
                await ctx.send(this_roll[1])
            await ctx.send(f"{sender}'s total with disadvantage = {min(sums)}")
        else:
            this_roll = roll_mechanics.single_type_roll(user_input)
            await ctx.send(this_roll[1])

@bot.command(name='ping', help='ping pong bb you know what it is')
async def ping(ctx):
    await ctx.send('Pong')

bot.run(TOKEN)