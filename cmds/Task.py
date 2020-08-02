import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json,asyncio,datetime 

with open('./setting.json','r',encoding='UTF8') as setting:
    settingData=json.load(setting)

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        #async def interval():
        #    await self.bot.wait_until_ready()
        #    pass 
        #self.bg_task = self.bot.loop.create_task(interval())

        self.K_flag = False

        async def Background_Task():
            await self.bot.wait_until_ready()
            while not self.bot.is_closed():
                await Krabby_Patty()
                await asyncio.sleep(1)
                await Update()
                await asyncio.sleep(1)
                await Remind()
                await asyncio.sleep(1)

        async def Update():
            with open('./data.json','r',encoding='UTF8') as jfile:
                jdata = json.load(jfile)
            with open('./data_buf.json','r',encoding='UTF8') as jfile:
                jbuf=json.load(jfile)
            Reminder=jdata['Reminder']
            Reminder=Reminder+jbuf['Reminder']
            jbuf['Reminder'].clear()
            with open('./data_buf.json','w',encoding='UTF8') as jfile:
                json.dump(jbuf,jfile,indent=4,ensure_ascii=False)
            with open('./data.json','w',encoding='UTF8') as jfile:
                json.dump(jdata,jfile,indent=4,ensure_ascii=False)

        async def Remind(): 
            td=datetime.timedelta(hours=0) 
            now=datetime.datetime.now()+td
            with open('./data.json','r',encoding='UTF8') as jfile:
                jdata = json.load(jfile)
            now_time=str(now.year)+'/'+str(now.month)+'/'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)
            data_end= len(jdata["Reminder"])
            Reminder=jdata['Reminder']
            if(data_end!=0):
                for i in range(0,data_end):  
                    #print(Reminder[i]['Time'])                  
                    if(Reminder[i]['Time']==now_time):
                        self.channel=self.bot.get_channel(int(Reminder[i]['Channel']))
                        await self.channel.send(Reminder[i]["Mention"]+'該做'+Reminder[i]["Thing"]+'了')
                        await asyncio.sleep(1)
                    else:
                        await asyncio.sleep(1)
                        pass  
                Reminder_buf=[]
                for i in Reminder:
                    if(i['Time']!=now_time):
                        Reminder_buf.append(i)
                    else:
                        pass 
                jdata['Reminder']=Reminder_buf
                with open('./data.json','w',encoding='UTF8') as jfile:
                    json.dump(jdata,jfile,indent=4,ensure_ascii=False)
                await asyncio.sleep(1)
            else:
                await asyncio.sleep(1)
                pass

        async def Krabby_Patty():
            td=datetime.timedelta(hours=0)
            now=datetime.datetime.now()+td
            #await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(int(settingData['Main_Channel']))
            #while not self.bot.is_closed():
            if now.hour == 3 and not self.K_flag:
                await self.channel.send('https://truth.bahamut.com.tw/s01/201602/5cbd45eb16e03c6382f96654bf2a570a.JPG')
                self.K_flag=True
                await asyncio.sleep(1)
            elif now.hour != 3:
                self.K_flag=False
                await asyncio.sleep(1)
                pass 
            else:
                await asyncio.sleep(1)
                pass
                
        self.bg_task = self.bot.loop.create_task(Background_Task())
   


def setup(bot):
    bot.add_cog(Task(bot))

#中文字中文字