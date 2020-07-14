# DiceDiceBB
DiceDiceBB is a Discord bot that rolls dice, written in Python. It's pretty simple.

## Commands
`!roll` is used to make rolls. You can roll multiple instances of multiple types of dice at once, with or without advantage.

Examples:
`!roll 2d6` rolls two six sided die.\
`!roll 1d8 and 2d6` rolls one eight sided die and two six sided dice.\
`!roll 1d20 with advantage` rolls one twenty sided dice with advantage (twice, keep the highest).\

## File Structure
`bot.py` contains and bot commands, and their logic.\
`roll_mechanics.py` is a module containing dice-rolling logic, specifically.\
`procfile` and `requirements` contain things for Heroku; process types and dependencies, respectively.\

## Contributing
Pull requests are welcome. Make them against development. If you have a feature you'd like to add, please feel free to do so.
