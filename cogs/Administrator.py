from discord.ext import commands
import discord as d

class Administrator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dChannel', aliases=['remove'])
    async def remove_channel(self, ctx, *channel: d.TextChannel):
       
        if ctx.author.guild_permissions.manage_channels:
            for i in channel:
                await i.delete()
                mbed = d.Embed(
                    title = 'Success',
                    description = f'Channel: {i} has been deleted',
                    color=0xFF5733
                )
                mbed.set_author(
                    name=ctx.author.display_name,
                    icon_url=ctx.author.avatar_url
                )
                await ctx.send(embed=mbed)

def setup(bot):
    bot.add_cog(Administrator(bot))
