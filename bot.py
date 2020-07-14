# bot.py
import os
import roll_mechanics

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='roll', help="Dice are being thrown!\nUse format <numberofdice>d<numberofsides>. EX: !roll 2d6 rolls two six sided dice.\nFor multiple dice, separate them with the word 'and'. EX: !roll 2d6 and 3d4 rolls two six sided dice and three four sided dice.")
async def roll(ctx, *user_input):
    user_input = ' '.join(user_input)
    advantage = 'with advantage' in user_input
    user_input = user_input.replace('with advantage', '')
    if 'and' in user_input:
        if advantage is True:
            sums = []
            for _ in range(2):
                this_roll = roll_mechanics.multi_type_roll(user_input)
                sums.append(this_roll[0])
                await ctx.send(this_roll[1])
            await ctx.send('Total with advantage = {}'.format(max(sums)))
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
            await ctx.send(f'Total with advantage = {max(sums)}')
        else:
            this_roll = roll_mechanics.single_type_roll(user_input)
            await ctx.send(this_roll[1])

@bot.command(name='ping', help='ping pong bb you know what it is')
async def ping(ctx):
    await ctx.send('Pong')

bot.run(TOKEN)