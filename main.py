import os
from discord.ext import commands


bot = commands.Bot(command_prefix='%', case_insensitive=True)

my_secret = os.environ['REDBOT']
extensions = ['cogs.Administrator']

if __name__ == '__main__':
    for ext in extensions:
        bot.load_extension(ext)
        
bot.run(my_secret)
