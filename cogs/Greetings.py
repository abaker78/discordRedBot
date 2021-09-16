# import discord
from discord.ext import commands

commands_tally = {
    
}

class Greetings(commands.Cog):
    def __init__(self, bot):
        
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        await ctx.channel.send(error)


    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command is not None:
            if ctx.command.name in commands_tally:
                commands_tally[ctx.command.name] += 1
            else:
                commands_tally[ctx.command.name] = 1
            print(commands_tally)

    @commands.group(name='helpcmd', invoke_without_command=True)
    async def helpcommand(self, ctx):
        await ctx.channel.send("Base help command. Subcommands: Misc, Fun, Music")

    @commands.command(name='list')
    async def _list(self, ctx, *args):
        await ctx.channel.send(f'You passed in {len(args)} arguments: {args}')

def setup(bot):
    bot.add_cog(Greetings(bot))
