import discord
from discord.ext import commands

class Challenge(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if not message.guild or message.author.bot:
            return
                
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Challenge(bot))
