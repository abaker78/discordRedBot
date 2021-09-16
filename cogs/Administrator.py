from discord.ext import commands
import discord as d

class Administrator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dChannel', aliases=['remove'])
    async def remove_channel(self, ctx, channel: d.TextChannel):
        mbed = d.Embed(
            title = 'Success',
            description = f'Channel: "{channel}" has been deleted',
        )
        if ctx.author.guild_permissions.manage_channels:
            await ctx.send(embed=mbed)
            await channel.delete()

def setup(bot):
    bot.add_cog(Administrator(bot))
