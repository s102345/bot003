import discord
from discord.ext import commands
from .core.classes import Cog_Extension
import json

class Role(Cog_Extension):

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,paylord):
        if(paylord.message_id == 738726856270020650):
            print(paylord.emoji)
            if(str(paylord.emoji) == "<:OOOOO:738727584879345687>"):
                guild =self.bot.get_guild(731883226527694918)
                role=guild.get_role(738722890932944896)
                member=paylord.member
                await member.send(f"你已獲得{role}身分組")
                await member.add_roles(role)

            if(str(paylord.emoji) == "3️⃣"):
                guild =self.bot.get_guild(731883226527694918)
                role=guild.get_role(738722894195982408)
                member=paylord.member
                await member.send(f"你已獲得{role}身分組")
                await member.add_roles(role)

            if(str(paylord.emoji) == "🈲"):
                guild =self.bot.get_guild(731883226527694918) 
                role=guild.get_role(738761889827520552)
                member=paylord.member
                await member.send(f"你已獲得{role}身分組")
                await member.add_roles(role)

            if(str(paylord.emoji) == "💻"):
                guild =self.bot.get_guild(731883226527694918)
                role=guild.get_role(738733197264683121)
                member=paylord.member
                await member.send(f"你已獲得{role}身分組")
                await member.add_roles(role)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,paylord):
        if(paylord.message_id == 738726856270020650):
            if(str(paylord.emoji) == "<:OOOOO:738727584879345687>"):
                guild =self.bot.get_guild(731883226527694918)
                role=guild.get_role(738722890932944896)
                member=guild.get_member(paylord.user_id)
                await member.send(f"你已失去{role}身分組")
                await member.remove_roles(role)

            if(str(paylord.emoji) == "3️⃣"):
                guild =self.bot.get_guild(731883226527694918)
                role=guild.get_role(738722894195982408)
                member=guild.get_member(paylord.user_id)
                await member.send(f"你已失去{role}身分組")
                await member.remove_roles(role)

            if(str(paylord.emoji) == "💻"):
                guild =self.bot.get_guild(731883226527694918)
                role=guild.get_role(738733197264683121)
                member=guild.get_member(paylord.user_id)
                await member.send(f"你已失去{role}身分組")
                await member.remove_roles(role)

            if(str(paylord.emoji) == "📖"):
                guild=self.bot.get_guild(731883226527694918)
                role=guild.get_role(738761887730106430)
                member=guild.get_member(paylord.user_id)
                await member.send(f"你已失去{role}身分組")
                await member.remove_roles(role)

            if(str(paylord.emoji) == "🈲"):
                guild=self.bot.get_guild(731883226527694918)
                role=guild.get_role(738761889827520552)
                member=guild.get_member(paylord.user_id)
                await member.send(f"你已失去{role}身分組")
                await member.remove_roles(role)

#中文字中文字中文字
def setup(bot):
    bot.add_cog(Role(bot))

    