import discord
from discord.ext import commands


class ExampleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cogtestcmd")
    async def cogtest_cmd(self, ctx):
        await ctx.send("Cog is working!")

def setup(bot):
    bot.add_cog(ExampleCog(bot))