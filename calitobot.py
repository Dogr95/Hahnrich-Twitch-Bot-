import os # for importing env vars for the bot to use
from twitchio.ext import commands
import random
from dotenv import load_dotenv

load_dotenv()
CHANNEL1 = 'calitobundo'
#channels = str(channels)
channels = CHANNEL1
print("running on:", channels)

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TWITCH_TMI_TOKEN'],
    client_id=os.environ['TWITCH_CLIENT_ID'],
    nick=os.environ['TWITCH_BOT_NICK'],
    prefix=os.environ['TWITCH_BOT_PREFIX'],
    initial_channels=[f"{CHANNEL1}"]
)

channelid=[os.environ['TWITCH_CHANNELID']]

@bot.event
async def event_command_error(ctx, error):
    error = str(error)
    with open("calitoerr.log", "a+") as errorfile:
        error = error + "\n"
        errorfile.write(error)

@bot.event
async def event_ready():
    #'Called once when the bot goes online.'
    print(f"{(os.environ['TWITCH_BOT_NICK'])} is online!")

@bot.command(name='calitoisttoll')
async def calitoisttoll(ctx):
    if str(ctx.author.name) == 'vertikarl':
        chance = ["!spin 5", "!spin 4", "!spin 3", "!w", "!wallets", "!lotto 7"]
        chanceV = random.choice(chance)
        chanceV = str(chanceV)
        await ctx.channel.send(chanceV)

@bot.command(name='spin')
async def spin(ctx):
    if str(ctx.author.name) != "zfcbot" and str(ctx.author.name) != "calitobundo" and str(ctx.author.name) != "calitobot":
        await ctx.channel.send(ctx.content)
    
@bot.command(name='slot')
async def slot(ctx):
    if str(ctx.author.name) != "zfcbot" and str(ctx.author.name) != "calitobundo" and str(ctx.author.name) != "calitobot":
        await ctx.channel.send(ctx.content)

@bot.command(name='c')
async def c(ctx):
    if str(ctx.author.name) == 'vertikarl':
        chance = ["!spin 5", "!spin 4", "!spin 3", "!w", "!wallets", "!lotto 7"]
        chanceV = random.choice(chance)
        chanceV = str(chanceV)
        await ctx.channel.send(chanceV)

@bot.command(name='r')
async def r(ctx):
    if str(ctx.author.name) == 'vertikarl' or str(ctx.author.name) == 'vertikarl' or str(ctx.author.name) == 'vertikarl':
        removeR = ctx.content
        if str(ctx.author.name) != 'vertikarl':
            removeR = removeR.replace("!gift", "Keine Berechtigung: !gift")
            removeR = removeR.replace("!r ", "")
            await ctx.channel.send(removeR)
        elif str(ctx.author.name) == 'vertikarl':
            removeR = removeR.replace("!r ", "")
            await ctx.channel.send(removeR)
    
@bot.command(name='checkerrors')
async def checkerrors(ctx):
    if (ctx.author.name) == 'vertikarl':
        if 'last' in ctx.content:
            with open("calitoerr.log", "r") as f:
                for last_line in f:
                    fS = "/me Last error: " + last_line
                await ctx.channel.send(fS)
        elif 'last' not in ctx.content:
            with open("calitoerr.log", "r") as f:
                errorcount = 0
                wnf = 0
                for line in f:
                    errorcount = errorcount + 1
                    if "was not found" in line:
                        wnf = wnf + 1
                errorcount = errorcount-1
                errormessage = "/me " + str(errorcount) + " errors have been logged. " + str(wnf) + " were CommandNotFound errors"
                await ctx.channel.send(errormessage)

@bot.command(name='plsdont')
async def plsdont(ctx):
    if (ctx.author.name) == 'vertikarl':
        x=10
        while x>0:
            x = x-1
            await ctx.channel.send("!f 5000")
    elif (ctx.author.name) != 'vertikarl':
        print(f"/me no permission to use this command @{ctx.author.name}")
    
########################################
#    Starts the bot                    #
########################################

if __name__ == "__main__":
    bot.run()

