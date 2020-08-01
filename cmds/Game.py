import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import random
class Game(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.passwd=0
        self.upper=100
        self.lower=1

    def __initialize(self):
        self.passwd=0
        self.upper=100
        self.lower=1

    @commands.group()
    async def 終極密碼(self,ctx):
        pass

    @終極密碼.command()
    async def 開始(self,ctx):
        if(self.passwd==0):  
            self.__initialize()
            self.passwd=random.randint(1,100)
            await ctx.send("遊戲開始囉！\n範圍："+str(self.lower)+"~"+str(self.upper))
        else:
            await ctx.send("遊戲正在進行中！")
        
    @終極密碼.command()
    async def 猜(self,ctx,guess:int):
        if(self.passwd==0):
            await ctx.send("遊戲尚未開始！")
        elif(guess>self.lower and guess<self.upper):
            if(guess>self.passwd):
                self.upper=guess
                await ctx.send("範圍："+str(self.lower)+"~"+str(self.upper))
            if(guess<self.passwd):
                self.lower=guess
                await ctx.send("範圍："+str(self.lower)+"~"+str(self.upper))
            if(guess==self.passwd):
                await ctx.send("恭喜"+str(ctx.message.author.mention)+"獲得勝利")
                self.__initialize()
        else:
            await ctx.send("請輸入正確的數字！")

    @終極密碼.command()
    async def 結束(self,ctx):
        if(self.passwd==0):
            await ctx.send("遊戲尚未開始！")
        else:
            await ctx.send("答案是"+str(self.passwd)+"，sp4")
            self.__initialize()




def setup(bot):
    bot.add_cog(Game(bot))

#中文字中文字中文字