import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json

class Trigger(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):   
        if msg.content=='怒' and msg.author != self.bot.user:
            await msg.channel.send('https://i.imgur.com/zn0SKVk.png')
        keyword=['野','格','炸','彈','我','的','最','愛']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('斷')
        if msg.content.endswith('www') and msg.author != self.bot.user:
            await msg.channel.send('w三小')
        if msg.content.startswith('嘛') and msg.author != self.bot.user:
            await msg.channel.send('嘛三小')
        if msg.content=='咩噗' and msg.author != self.bot.user:
            await msg.channel.send('https://media.discordapp.net/attachments/736482284508676178/738000488359919636/unknown.png')
        
        with open('./dict.json','r',encoding='UTF8') as jfile:
            jdata=json.load(jfile)

        if msg.content in jdata and msg.author != self.bot.user:
            await msg.channel.send(jdata[msg.content])


def setup(bot):
    bot.add_cog(Trigger(bot))

#中文字中文字