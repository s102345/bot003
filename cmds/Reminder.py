import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json,datetime,asyncio

class Reminder(Cog_Extension):
         
    @commands.command()
    async def 提醒(self,ctx,year:int,month:int,day:int,hour:int,minute:int,*,msg:str):
        #td=datetime.timedelta(hours=8)
        #now=datetime.datetime.now()+td
        try:
            datetime.date(year,month,day)
        except:
            await ctx.send("日期輸入錯誤！")
        else:
            now=datetime.datetime.now()
            if(24<hour or hour <0 or 60<minute or 0>minute):
                await ctx.send("時間輸入錯誤！")
            elif(now.year>year):
                await ctx.send("無法設置逾時的行程！")
            elif(now.year==year and now.month>month):
                await ctx.send("無法設置逾時的行程！")
            elif(now.year==year and now.month==month and now.day>day):
                await ctx.send("無法設置逾時的行程！")
            elif(now.year==year and now.month==month and now.day==day and now.hour>hour):
                await ctx.send("無法設置逾時的行程！")
            elif(now.year==year and now.month==month and now.day==day and now.hour==hour and now.minute>minute):
                await ctx.send("無法設置逾時的行程！")
            else:
                with open('./data.json','r',encoding='UTF8') as jfile:
                    jdata = json.load(jfile)
                Reminder=jdata['Reminder']
                time=str(year)+'/'+str(month)+'/'+str(day)+' '+str(hour)+':'+str(minute)
                paylord = {"Time":time,"Thing":msg,"Mention":ctx.message.author.mention,"Channel":str(ctx.message.channel.id)}
                Reminder.append(paylord)
                with open('./data.json','w',encoding='UTF8') as jfile:
                    json.dump(jdata,jfile,indent=4,ensure_ascii=False)
                jfile.close()
                await ctx.send(ctx.message.author.mention+'已設置在'+time+'的提醒：'+msg)

    @提醒.error
    async def 提醒_error(self,ctx,error):
        await ctx.send('請輸入正確的指令！\n指令：!提醒　<年>　<月>　<日>　<時>　<分>　<事件>')
#中文中文中文

def setup(bot):
    bot.add_cog(Reminder(bot))
