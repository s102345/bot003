import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json,asyncio,datetime 

with open('D://Programming/Python Project/DiscordBot/bot003/setting.json','r',encoding='UTF8') as setting:
    settingData=json.load(setting)

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #async def interval():
        #    await self.bot.wait_until_ready()
        #    pass 
        #self.bg_task = self.bot.loop.create_task(interval())

        self.K_flag = False

        async def Krabby_Patty():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(int(settingData['Main_Channel']))
            while not self.bot.is_closed():
                if datetime.datetime.now().hour == 3 and not self.K_flag:
                    await self.channel.send('https://truth.bahamut.com.tw/s01/201602/5cbd45eb16e03c6382f96654bf2a570a.JPG')
                    self.K_flag=True
                    await asyncio.sleep(1)
                elif datetime.datetime.now().hour != 3:
                    self.K_flag=False
                    await asyncio.sleep(1)
                    pass 
                else:
                    await asyncio.sleep(1)
                    pass
                
        self.bg_task = self.bot.loop.create_task(Krabby_Patty())
   


def setup(bot):
    bot.add_cog(Task(bot))

#中文字中文字