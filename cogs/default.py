import discord
from discord.ext import commands
import os



class botcommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

                
           

           
                  

def setup(bot): # this is called by Pycord to setup the co
    bot.add_cog(botcommands(bot)) # add the cog to the bot
