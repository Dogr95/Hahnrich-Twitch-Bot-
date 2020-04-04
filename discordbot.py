import os
import discord
from dotenv import load_dotenv
import random
from discord.ext import commands
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

ownerImport = os.getenv('DISCORD_OWNER')

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
    server = discord.utils.get(bot.guilds, id=int(SERVER))
    
    print(f'{bot.user} is connected to the following server:\n'
          f'{server.name}(id: {server.id})')

    await bot.change_presence(status=discord.Status.idle, activity=activity)
    memberlist = []
    for member in server.members:
        memberlist.append(f'{member.name}#{member.discriminator} id: {member.id}')
        #print(f'{member.name}#{member.discriminator} id: {member.id}')
    memberlist = '\n'.join(memberlist)
    #members = '\n - '.join([member.name for member in server.members])# + 'id: '.join(str([member.id for member in server.members]))
    #memberids = '\n - '.join(str([member.id for member in server.members]))
    #print(members)
    #print([member.id for member in server.members])
    memF = open("discordmembers.list", "w+")
    memF.write(memberlist)
    memF.close()
        

@bot.event
async def on_member_join(member):
    owner = bot.get_user((int(ownerImport)))
    newMember = (f"{member.name}")
    await owner.send(newMember)
        
#@bot.event
#async def on_message(message, mCont):
#    if message.author == bot.user:
#        return
#    mcSplash=open("mcSplash.txt")
#    Splash = [i for i in mcSplash.readlines()]
#    SplashR = random.choice(Splash)
#    if mCont=='quote':
#        await message.channel.send(SplashR)

#@bot.event                                            #Absolutly broken dogshit
#async def on_error(event, *args, **kwargs):
#    owner = bot.get_user((int(ownerImport)))
#    with open('err.log', 'w+') as f:
#        f.write(f'Error: {args[0]}\n')
#        f.close()
#        f = open('err.log', 'r')
#        fileC = f.readlines()
#        for line in fileC:
#            await owner.send(line)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have permission to use this command!')

@bot.command(name='test', help='poke the bot')
async def test(ctx):
    owner = bot.get_user((int(ownerImport)))
    await owner.send(f'{ctx.author.name} with id: {ctx.author.id} ran test')
    await ctx.send("no u")
    raise discord.DiscordException

@bot.command(name='memberlist', help='sends a file with all members')
async def memberlist(ctx):
    mdate = os.path.getmtime("discordmembers.list")
    mdate = time.ctime(mdate)
    await ctx.send(f"Last modified: {mdate}", file=discord.File("discordmembers.list"))

@bot.command(name='s', help='secret')
@commands.has_role('innocent')
async def s(ctx, Uurl):
    owner = bot.get_user((int(ownerImport)))
    await ctx.send("Downloading")
    os.system(f"python dltwitchclips.py --clip {Uurl} ")
    print("")
    await ctx.send("Finished downloading")
    innocent = open("tmp/latest", "r")
    for innocentL in innocent:
        innocentL = innocentL.replace("Namespace(clip='https://clips.twitch.tv/", "")
        innocentL = innocentL.replace("'", "")
        innocentL = innocentL.replace("(", "")
        innocentL = innocentL.replace(")", "")
        innocentF = (f"archive/{innocentL}.mp4")
        await ctx.send("Trying to send file...")
        try:
            await ctx.send("", file=discord.File(innocentF))
        except:
            await ctx.send("File too big!")
            await owner.send(f"{ctx.author.name} tried to convert {Uurl} but the file is too big to upload.")
        finally:
            pass

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

@bot.command(name='lotto')
async def lotto(ctx, *lottoG):
    lottoUser = (f"{ctx.author.name}")
    try:
        open((lottoUser), "r")
    except FileNotFoundError:
        print("Creating file...")
        cr = open((lottoUser), "w+")
        cr.write("1000")
        cr.close()
        print(f"File: {ctx.author.name} created!")
        await ctx.send(f"File for {ctx.author.name} created.")
    finally:
        lottoUserF = open((lottoUser), "r")
        lottoUserLines = lottoUserF.readlines()
        for lottoUserLine in lottoUserLines:
            lottoUserFC = str(lottoUserLine)
            lottoUserFC = int(lottoUserFC)
            lottoUserF.close()
            price = 2400
            price = price/(len(lottoG))
            price = int(price)
            priceLoss = len(lottoG)*100
            lottoUserFC = lottoUserFC-priceLoss
            lottoN = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21')
            lottoR = random.choice(lottoN)
            if lottoUserFC>=priceLoss: 
                lottoNS = "Lotto Number: " + lottoR
                await ctx.send(lottoNS)
                if lottoR in lottoG:
                    lottoUserFC = lottoUserFC+price
                    lottoUserF.close()
                    lottoUserF = open((lottoUser), "w+")
                    lottoUserFC = str(lottoUserFC)
                    lottoUserF.write(lottoUserFC)
                    lottoWS = f"{ctx.author.name} won " + str(price) + " credits. Balance: " + str(lottoUserFC)
                    await ctx.send(lottoWS)
                else:
                    lottoUserF.close()
                    lottoUserF = open((lottoUser), "w+")
                    lottoUserFC = str(lottoUserFC)
                    lottoUserF.write(lottoUserFC)
                    lottoLS = f"{ctx.author.name} lost " + str(priceLoss) + " credits. Balance: " + str(lottoUserFC)
                    await ctx.send(lottoLS)
            else:
                await ctx.send(" You don't have enough credits!")

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
    
@bot.command(name='tts', help='testing purposes only. (Sachsen-only)')
@commands.has_role('Sachsen')
async def tts(ctx, *speech):
    speech = '_'.join(speech)
    speech = speech.replace("'", "")
    speech = speech.replace('"', '')
    speech = speech.replace("(", "")
    speech = speech.replace(")", "")
    speech = speech.replace("-", "")
    speech = speech.replace("&", "")
    speech = speech.replace("/", "")
    speech = speech.replace(""""\
                            """, "")
    speech = speech.replace("!", "")
    speech = speech.replace("?", "")
    speech = speech.replace("$", "")
    speech = speech.replace("§", "")
    speech = speech.replace(",", "")
    speech = speech.replace("%", "")
    speech = speech.replace("{", "")
    speech = speech.replace("}", "")
    speech = 'espeak ' + (speech)
    os.system(speech)

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
                    eventRsS = l + " has participated. Balance: " + str(eventRC)
                    await ctx.send(eventRsS)
            else:
                await ctx.send("Event currently not running.")
    else:
        await ctx.send(f"Not able to participate, event closed ({eventstatusS})")
  

bot.run(TOKEN)
