import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json,asyncio,random

class Useless(Cog_Extension):
    
    @commands.command()
    async def 更新(self,ctx):
        await ctx.send('我明天早上七點要起床，現在凌晨一點要叫我更新？你不會更新，你要先講，好嗎？')
    
    @commands.has_guild_permissions()
    @commands.command()
    async def clear(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)

    @commands.command()
    async def 幫我撐10秒(self,ctx):
        await ctx.send("https://thumbs.gfycat.com/SlightQuaintBeagle-size_restricted.gif")
        await asyncio.sleep(10) #單位：秒
        await ctx.send("https://31.media.tumblr.com/tumblr_ma97m64In61rfpxhzo1_400.gif")

    @commands.command()
    async def 煮泡麵(self,ctx):
        await ctx.send(f'{ctx.message.author.mention}開始煮泡麵囉！')
        await asyncio.sleep(180)
        await ctx.send(f'{ctx.message.author.mention}泡麵煮好囉！')

    @commands.command()
    async def 說笑話(self,ctx):
        await ctx.send('你')

    @commands.command()
    async def 尬廣(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.group()
    async def 語萱(self,ctx):
        pass

    @語萱.command()
    async def 新增(self,ctx,key,*,value):
        with open('./dict.json','r',encoding='UTF8') as jfile:
            jdata=json.load(jfile)
        jfile.close()
        await ctx.send(f'關鍵字{key}設置成功，回答詞為{value}')
        jdata[f'{key}']=f'{value}'
        with open('./dict.json','w',encoding='UTF8') as jfile:
            json.dump(jdata,jfile,indent=4,ensure_ascii=False)    
        jfile.close()

    @語萱.command()
    async def 刪除(self,ctx,key):
        with open('./dict.json','r',encoding='UTF8') as jfile:
            jdata=json.load(jfile)
        jfile.close()
        if key in jdata:
          await ctx.send(f'關鍵字{key}刪除成功')
          del jdata[f'{key}']
          with open('./dict.json','w',encoding='UTF8') as jfile:
              json.dump(jdata,jfile,indent=4,ensure_ascii=False)    
          jfile.close()
        else:
          await ctx.send("沒有該關鍵字")


    @新增.error
    async def 語萱_新增_error(self,ctx,error):
        await ctx.send('請輸入正確的指令！\n指令：!語萱　新增　<關鍵字>　<回答詞>')
    
    @刪除.error
    async def 語萱_刪除_error(self,ctx,error):
        await ctx.send('請輸入正確的指令！\n指令：!語萱　刪除　<關鍵字>')

def setup(bot):
    bot.add_cog(Useless(bot))