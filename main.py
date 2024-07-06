import discord
import os # default module
from discord.ext import commands
from discord.ext import tasks
import json
import logging
import cogs.system





with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]

if dev_status == "true":
            with open("devinfo.json", "r") as f:
            _r = json.load(f)
            botinfo = _r


if dev_status == "false":
            with open("info.json", "r") as f:
            _r = json.load(f)
            botinfo = _r




# Defing bot and bot user intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=botinfo["prefix"], intents=intents)

logging.basicConfig(level=logging.INFO)
#loading cogs
bot.load_extension('cogs.default')


@bot.event
async def on_ready():
    bot.auto_sync_commands = True
    logging.info("Bot is ready!")
    await bot.change_presence(activity=botinfo["game"])
    

@bot.event
async def on_application_command_error(interaction: discord.Interaction,
                                        error: discord.DiscordException):
    embed = discord.Embed(
        title = "Whoops!",
        description = "An error has occured.  Retrying the command might help, or this can be an internal server error",
        color = discord.Colour.red()
    )
    embed.add_field(name="Error Message", value="`{0}`".format(repr(error)))

    embed.set_thumbnail(url=botinfo["errorimg"])
    try:
        await interaction.response.send_message(embed=embed)
    except:
        await interaction.followup.send(embed=embed)
    raise error

#CombineBot website button for /about

# AutoRun prevention with __name__
if __name__ == "__main__": # import run prevention
    if os.path.isfile("token.json") == True: # check if token.json exists
        with open("token.json", "r") as f:
            _d = json.load(f)
            loadedJSONToken = _d["BOT_TOKEN"]
        if loadedJSONToken.lower() == "yourtokenhere":
            loadedJSONToken = None
    else:
        loadedJSONToken = None
    environToken = os.getenv("BOT_TOKEN")

    if (loadedJSONToken == None) and (environToken == None):
        raise EnvironmentError("No token specified!  Please enter a token via token.json or by passing an environment variable called 'BOT_TOKEN'.  Stop.")
    BOT_TOKEN = (environToken if environToken != None else loadedJSONToken)    
    bot.run(BOT_TOKEN)



































