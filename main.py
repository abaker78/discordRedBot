import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='%', case_insensitive=True)

my_secret = os.environ['REDBOT']
client = discord.Client()

extensions = ['cogs.Greetings', 'cogs.Administrator']
if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)
bot.run(my_secret)
