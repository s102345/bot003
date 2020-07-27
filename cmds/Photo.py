import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json

class Photo(Cog_Extension):
    
    @commands.command()
    async def photo(self,ctx):
        await ctx.send('https://i.imgur.com/zn0SKVk.png')

def setup(bot):
    bot.add_cog(Photo(bot))