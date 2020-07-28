import requests,json
import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import datetime
class Weather(Cog_Extension):

    #questLocation=input('請輸入要查詢的地區：')
    @commands.command()
    async def 天氣(self,ctx,msg):
        td=datetime.datetime.today()
        time_delta=datetime.timedelta(hours=8)
        new_td=td+time_delta
        td_format=new_td.strftime("%Y/%m/%d %H:%M")
        r=requests.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-52AFE010-C3DF-41AE-8805-125037BDA80D&format=JSON',verify=False)
        if(r.status_code == 200):
            result=r.json()
            #print(type(result))
            record=result['records']
            location=record['location']
            parameter_list=[]
            startTime_list=[]
            for i in location:
                if(msg==i['locationName']):
                    for j in i['weatherElement']:
                        counter=0
                        for k in j['time']:
                            if(counter<3):
                                startTime_list.append(k['startTime'])
                                counter+=1
                            parameter_list.append(k['parameter']['parameterName'])
                    break
            if(parameter_list == []):
                await ctx.send('輸入錯誤！')
            else:
                embed=discord.Embed(title=msg, description='第一列：'+startTime_list[0]+'\n第二列：'+startTime_list[1]+'\n第三列：'+startTime_list[2])
                embed.add_field(name='天氣狀態', value=parameter_list[0], inline=True)
                embed.add_field(name='天氣狀態', value=parameter_list[1], inline=True)
                embed.add_field(name='天氣狀態', value=parameter_list[2], inline=True)
                embed.add_field(name='降雨機率', value=parameter_list[3], inline=True)
                embed.add_field(name='降雨機率', value=parameter_list[4], inline=True)
                embed.add_field(name='降雨機率', value=parameter_list[5], inline=True)
                embed.add_field(name='最低溫', value=parameter_list[6], inline=True)
                embed.add_field(name='最低溫', value=parameter_list[7], inline=True)
                embed.add_field(name='最低溫', value=parameter_list[8], inline=True)
                embed.add_field(name='天氣狀況', value=parameter_list[9], inline=True)
                embed.add_field(name='天氣狀況', value=parameter_list[10], inline=True)
                embed.add_field(name='天氣狀況', value=parameter_list[11], inline=True)
                embed.add_field(name='最高溫', value=parameter_list[12], inline=True)
                embed.add_field(name='最高溫', value=parameter_list[13], inline=True)
                embed.add_field(name='最高溫', value=parameter_list[14], inline=True)
                embed.set_footer(text=td_format)
                await ctx.send(embed=embed)
        else:
            await ctx.send('暫時無法取得資料，請稍後再試') 
#now =datetime.now()


    #中文字中文字中文字

def setup(bot):
    bot.add_cog(Weather(bot))