import random

def roll_dice(nsides, ndice):
    dice = [
        str(random.choice(range(1, int(nsides) + 1)))
        for _ in range(int(ndice))     
    ]
    return dice

def multi_type_roll(user_input):
    rolls=user_input.replace(' ','').split('and')
    sumdice=0
    messages=""
    for i in range(len(rolls)):
        ndice,nsides = rolls[i].split('d')
        dice = roll_dice(nsides, ndice)
        sumdice += sum([int(i) for i in dice])
        print(f"{rolls[i]}: {', '.join(dice)}")
        messages = messages + (f"{rolls[i]}: {', '.join(dice)}\n")
        print(f"Message to be returned to roll request: {messages}")
    print(f"Total = {sumdice}")
    messages = messages + (f"Total = {sumdice}")
    print(f"Message to be returned to roll request: {messages}")
    return sumdice, messages

def single_type_roll(user_input):
    print(user_input)
    messages=""
    ndice,nsides = user_input.split('d')
    dice = roll_dice(nsides, ndice)
    sumdice = sum([int(i) for i in dice])
    if len(dice) > 1:
        print(f"{', '.join(dice)} \nTotal = {sumdice}")
        messages = messages + (f"{', '.join(dice)} \nTotal = {sumdice}")
    else:
        print(f"Total = {dice[0]}")
        messages = messages + (f"Total = {dice[0]}\n")
    return sumdice, messages