import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):   
        channel = format(736604239081635911)
        await channel.send(f'還敢下來啊！{member}')

    @commands.Cog.listener()
    async def on_member_leave(self,member):
        channel = format(736604239081635911)
        await channel.send(f'{member}高歌離席！')

def setup(bot):
    bot.add_cog(Event(bot))