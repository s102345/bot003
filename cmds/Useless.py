import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json,asyncio

class Useless(Cog_Extension):
    
    @commands.command()
    async def 更新(self,ctx):
        await ctx.send('我明天早上七點要起床，現在凌晨一點要叫我更新？你不會更新，你要先講，好嗎？')
    
    @commands.command()
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def 幫我撐10秒(self,ctx):
        await ctx.send("https://thumbs.gfycat.com/SlightQuaintBeagle-size_restricted.gif")
        await asyncio.sleep(10) #單位：秒
        await ctx.send("https://31.media.tumblr.com/tumblr_ma97m64In61rfpxhzo1_400.gif")


def setup(bot):
    bot.add_cog(Useless(bot))