import discord
from discord.ext import commands
import json
import os

with open('setting.json','r',encoding='UTF8') as setting:
    settingData=json.load(setting)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    channel = bot.get_channel(int(settingData['Main_Channel']))
    await channel.send('引擎發動囉')
    
 
for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):     
        if(Filename!='__init__.py'):
            bot.load_extension(f'cmds.{Filename[:-3]}')

@commands.is_owner()
@bot.command()
async def load(ctx,extension):
    try:
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'已載入{extension}')
    except:
        await ctx.send(f'{extension}無法被載入')

@commands.is_owner()
@bot.command()
async def unload(ctx,extension):
    try:
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'已掛載{extension}')
    except :
        await ctx.send(f'無法掛載{extension}')

@commands.is_owner()
@bot.command()
async def reload(ctx,extension):
    try:
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'已重新載入{extension}')
    except:
        await ctx.send(f'無法重載{extension}')

if __name__=="__main__" :
    bot.run(settingData['TOKEN'])