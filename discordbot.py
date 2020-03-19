import os
import discord
from dotenv import load_dotenv
import random
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

owner = os.getenv('DISCORD_OWNER')
#client = discord.Client()
bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'))
try:
    eventstatus
except NameError:
    eventFile = open("Event", "r")
    eventLines = eventFile.readlines()
    for eventLine in eventLines:
        eventstatus = str(eventLine)
finally:
    if eventstatus=='close':
        eventstatus = 'closed'
        actEv = "Event is: " + eventstatus
        activity = discord.Game(actEv)
    else:
        actEv = "Event is: " + eventstatus
        activity = discord.Game(actEv)

def RepresentsInt(ReprInt):
    try: 
        int(ReprInt)
        return True
    except ValueError:
        return False
    
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord with version: {discord.__version__}')
    server = discord.utils.get(bot.guilds, name=SERVER)
    
    print(f'{bot.user} is connected to the following server:\n'
          f'{server.name}(id: {server.id})')

    await bot.change_presence(status=discord.Status.idle, activity=activity)
    members = '\n - '.join([member.name for member in server.members])
    #print(f'Server Members:\n - {members}')

@bot.event
async def on_member_join(member):
    await owner.create_dm()
    await owner.dm_channel.send("test")
    newMember = (f"{member.name}")
        
#@bot.event
#async def on_message(message, mCont):
#    if message.author == bot.user:
#        return
#    mcSplash=open("mcSplash.txt")
#    Splash = [i for i in mcSplash.readlines()]
#    SplashR = random.choice(Splash)
#    if mCont=='quote':
#        await message.channel.send(SplashR)

@bot.event
async def on_error(event, *args, **kwargs):
    print(f'{args[0]} \n')
    #await owner.create_dm()
    #await owner.dm_channel.send(f'{args[0]} \n')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have permission to use this command!')

@bot.command(name='test')
async def test(ctx):
    await ctx.send("no u")

@bot.command(name='flip', help="flips a given amount of credits, usage: !flip [amount]")
async def flip(ctx, betAmount):
    l = (f"{ctx.author.name}")
    try:
        k = open((l), "r")
    except FileNotFoundError:
        print("Creating file...")
        cr = open((l), "w+")
        cr.write("1000")
        cr.close()
        print(f"File: {ctx.author.name} created!")
        await ctx.send(f"File for {ctx.author.name} created.")
    finally:
        k = open((l), "r")
        lines = k.readlines()
        punkte = 0
        for line in lines:
            conv_int = int(line)
            punkte = punkte + conv_int
            k.close()
            try:
                betAmount = int(betAmount)
                VEerror = True
            except ValueError:
                await ctx.send(f"invalid syntax {ctx.author.name}")
                VEerror = False
            finally:
                if VEerror:
                    if betAmount >= 0 :
                        if betAmount > punkte:
                            await ctx.send("You do not have enough credits!")
                        elif betAmount <=punkte:
                            #define flip
                            coin = ('win', 'loss')
                            flip = random.choice(coin)
                            if flip=="win":
                                punkte=punkte+betAmount
                                meW = l + " won, total: " + str(punkte) + " credits!"
                                await ctx.send((meW))
                            elif flip=="loss":
                                punkte=punkte-betAmount
                                meL = l + " lost, total: " + str(punkte) + " credits!"
                                await ctx.send((meL))
                        else:
                            await ctx.send(f"invalid syntaxn background {ctx.author.name}")
                    else:
                        await ctx.send(f"Positive numbers only {ctx.author.name}")
            
        #saving stats to ({ctx.author.name}) file
        f = open((l), "w")
        f.write(str(punkte))
        f.close()

@bot.command(name='credits', help="shows the amount of credits you have")
async def credits(ctx):
    creditsCommand = (f"{ctx.author.name}")
    try:
        creditsCommandCheck = open((creditsCommand), "r")
    except FileNotFoundError:
        print("Creating file...")
        creditsCommandFile = open((creditsCommand), "w+")
        creditsCommandFile.write("1000")
        creditsCommandFile.close()
        print(f"File: {ctx.author.name} created!")
        await ctx.send(f" File for {ctx.author.name} created.")
    finally:
        creditsCommandCheck = open((creditsCommand), "r")
        creditsLines = creditsCommandCheck.readlines()
        for creditsLine in creditsLines:
            creditsCheckInt = int(creditsLine)
            await ctx.send(f"{ctx.author.name} has {creditsCheckInt} credits.")
    if creditsCheckInt < 100:
        await ctx.send(f"i felt bad for @{ctx.author.name} and gave him 300 credits.")
        creditsCheckInt = creditsCheckInt+300
        f = open((creditsCommand), "w")
        f.write(str(creditsCheckInt))
        f.close()
        await ctx.send(f"{ctx.author.name} now has {creditsCheckInt} credits.")
    else:
        pass
    
@bot.command(name='dice', help='roll the dice, usage: !dice [number of sides]')
async def dice(ctx, sides):
    print(RepresentsInt(sides))
    if RepresentsInt(sides):
        sides = int(sides)
        if sides<1:
            await ctx.send('invalid number of sides')
        else:
            dice = [str(random.choice(range(1, sides + 1)))]
            await ctx.send(random.choice(dice))
    else:
        await ctx.send("invalid input")

@bot.command(name='calc', help="given two numbers and an operator, it calculates the result. Possible Operators: '+' '-' ':' '*'")
async def calc(ctx, calc1, calcR, calc2):
    ErrorFree = True
    cVE1 = True
    cVE2 = True
    try:
        calc1 = int(calc1)
    except ValueError:
        cVE1 = False
    try:
        calc2 = int(calc2)
    except ValueError:
        cVE2 = False
    finally:
        if cVE1 and cVE2:
            if calcR == '+':
                calcE = int(calc1) + int(calc2)
            elif calcR == '-':
                calcE = int(calc1) - int(calc2)
            elif calcR == ':':
                calcE = int(calc1) / int(calc2)
            elif calcR == '*':
                calcE = int(calc1) * int(calc2)
            else:
                ErrorFree = False
                await ctx.send(f"invalid operator {ctx.author.name} - Possible Operators: '+' '-' ':' '*'")
            if ErrorFree:
                await ctx.send(calcE)
        else:
            await ctx.send("Invalid syntax")
   
@bot.command(name='event', help='opens the event (Moderator only)')
@commands.has_role('Moderator')
async def event(ctx, eventstatus):
    if True:
        #useless, eventstatus = ctx.content.split(' ')
        eventFile = open("Event", "r")
        eventLines = eventFile.readlines()
        for eventLine in eventLines:
            eventSF = str(eventLine)
        if eventstatus=='open' and eventSF=='open':
            await ctx.send("Event is already opened.")
            actEv = "Event is: " + eventstatus
            activity = discord.Game(actEv)
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        elif eventstatus=='open' and eventSF!='open':
            eventFile.close()
            eventCFile = open("Event", "w+")
            eventCFile.write(eventstatus)
            eventSs = "Event is now " + eventstatus + ". You can now enter !get to recieve 100 credits each time."
            await ctx.send(eventSs)
            actEv = "Event is: " + eventstatus
            activity = discord.Game(actEv)
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        elif eventstatus=='close' and eventSF=='close':
            await ctx.send(" Event is already closed")
            eventstatus = 'closed'
            actEv = "Event is: " + eventstatus
            activity = discord.Game(actEv)
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        elif eventstatus=='close' and eventSF!='close':
            eventFile.close()
            eventCFile = open("Event", "w+")
            eventCFile.write(eventstatus)
            eventSsC = (f"Event is now closed ({eventstatus})")
            await ctx.send(eventSsC)
            eventstatus = 'closed'
            actEv = "Event is: " + eventstatus
            activity = discord.Game(actEv)
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        else:
            await ctx.send(f"invalid input {ctx.author.name}")

@bot.command(name='get', help='participate in the event (only possible while its open)')
async def get(ctx):
    eventstatusF = open("Event", "r")
    eventstatusLines = eventstatusF.readlines()
    for eventstatusLine in eventstatusLines:
        eventstatusS = str(eventstatusLine)
    if eventstatusS=='open':
        l = (f"{ctx.author.name}")
        try:
            open((l), "r")
        except FileNotFoundError:
            print("Creating file...")
            cr = open((l), "w+")
            cr.write("1000")
            cr.close()
            print(f"File: {ctx.author.name} created!")
            await ctx.send(f"File for {ctx.author.name} created.")
        finally:
            if eventstatusS=='close':
                await ctx.send("Event currently not running.")
            if eventstatusS == 'open':
                eventRFile = open((l), "r")
                eventRLines = eventRFile.readlines()
                for eventRLine in eventRLines:
                    eventRC = int(eventRLine)
                    eventRC = eventRC+100
                    eventRFile.close()
                    eventRFile = open((l), "w+")
                    eventRFile.write(str(eventRC))
                    eventRFile.close()
                    eventRsS = l + "has participated. Balance: " + str(eventRC)
                    await ctx.send(eventRsS)
            else:
                await ctx.send("Event currently not running.")
    else:
        await ctx.send(f"Not able to participate, event closed ({eventstatusS})")
  

bot.run(TOKEN)
