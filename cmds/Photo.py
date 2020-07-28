import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json,random

with open('./setting.json','r',encoding='UTF8') as setting:
    settingData=json.load(setting)

class Photo(Cog_Extension):
    
    #@commands.command()
    #async def photo(self,ctx):
    #    await ctx.send('https://i.imgur.com/zn0SKVk.png')

    @commands.command()
    async def 北科(self,ctx):
        rnd_pic=random.choice(settingData['Canson'])
        await ctx.send(rnd_pic)

def setup(bot):
    bot.add_cog(Photo(bot))

#中文字中文字中文字