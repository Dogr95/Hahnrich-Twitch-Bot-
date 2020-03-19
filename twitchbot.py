import os # for importing env vars for the bot to use
import random
from twitchio.ext import commands

CHANNEL1, CHANNEL2 = [os.environ['TWITCH_CHANNEL']] + [os.environ['TWITCH_CHANNEL2']]
#channels = str(channels)
channels = CHANNEL1 + ", " + CHANNEL2
print("running on:", channels)

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TWITCH_TMI_TOKEN'],
    client_id=os.environ['TWITCH_CLIENT_ID'],
    nick=os.environ['TWITCH_BOT_NICK'],
    prefix=os.environ['TWITCH_BOT_PREFIX'],
    initial_channels=[f"{CHANNEL1}", f"{CHANNEL2}"]
)

channelid=[os.environ['TWITCH_CHANNELID']]

def RepresentsInt(ReprInt):
    try: 
        int(ReprInt)
        return True
    except ValueError:
        return False

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{(os.environ['TWITCH_BOT_NICK'])} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(f"{CHANNEL1}", f"/me is watching!")
    await ws.send_privmsg(f"{CHANNEL2}", f"/me is watching!")

@bot.event
async def event_join(user):
    ej = bot._ws
    filterUser = str(f"{user}")
    filterUser = filterUser.replace("<User name=", "")
    if f"channel={CHANNEL1}" in filterUser:
        filterUser = filterUser.replace(f"channel={CHANNEL1}>", "")
        print(f"{filterUser}joined. (JoinEvent)")
        await ej.send_privmsg(f"{CHANNEL1}", f"/me {filterUser} joined. (JoinEvent)")
    elif f"channel={CHANNEL2}" in filterUser:
        filterUser = filterUser.replace(f"channel={CHANNEL2}>", "")
        print(f"{filterUser}joined. (JoinEvent)")
        await ej.send_privmsg(f"{CHANNEL2}", f"/me {filterUser} joined. (JoinEvent)")
    
@bot.event
async def event_part(user):
    ep = bot._ws
    filterUserP = str(f"{user}")
    filterUserP = filterUserP.replace("<User name=", "")
    if f"channel={CHANNEL1}" in filterUserP:
        filterUserP = filterUserP.replace(f"channel={CHANNEL1}>", "")
        print(f"{filterUserP} left. (LeaveEvent)")
        await ep.send_privmsg(f"{CHANNEL1}", f"/me {filterUserP} left. (LeaveEvent)")
    elif f"channel={CHANNEL2}" in filterUserP:
        filterUserP = filterUserP.replace(f"channel={CHANNEL2}>", "")
        print(f"{filterUserP} left. (LeaveEvent)")
        await ep.send_privmsg(f"{CHANNEL2}", f"/me {filterUserP} left. (LeaveEvent)")

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    #shortened channelsend
    greet = ctx.content.lower()
    stateM = ctx.content.lower()
    husoN = ctx.content.lower()
    #leetN = ctx.content.lower()
    greet = greet.split(' ')
    greetAnswer = ['Hi! HeyGuys', 'Auch hier? PogChamp', 'Lang nicht gesehen PogChamp', 'Hey, was geht?', 'Tag, haben wir uns schonmal gesehen?']
    greetList = ['dogr7sachse', 'dogr7geist', 'dogr7flex', 'snaqblank', 'joelucutz', 'joelucutz,', 'hello', 'hello,', 'hi', 'hi,', 'tag', 'tag,', 'hallo', 'hallo,', 'selphyhi', 'selphyhi,', 'servus', 'servus,', 'grüße', 'grüße,', 'hey', 'hey,', 'sup', 'sup,', 'hay', 'hay,' 'hoi', 'hoi,']
    greetWList = ['wie gehts', 'was geht', 'und dir?', 'deine lage?']
    greetWAnswer = ['Ganz okay... hoffentlich bald Feierabend NotLikeThis', 'Mir gehts ganz gut und selber?', 'Das geht dich nichts an! selphyPout', 'Meine Lage ist unbestimmt seit der Zeit in Vietnam selphySad', 'Sag du es mir', 'Die Frage ist, wie gehts DIR?', 'Lass dir mal ne andere Frage einfallen']
    husoList = ['huso', 'haʟʟo', 'haʟʟo,', 'haiio', 'hailo', 'hailo,', 'halio', 'halio,', 'haiio,', 'halo', 'halo,', 'was los klaus', 'alles husos', 'husos', 'erschieß dich', 'erschiess dich', 'account vor drei minuten erstellt', 'xhuso']
    husoAnswer = ['Alles Husos, was los Klaus.', 'Account vor drei Minuten erstellt, ahja', 'ahja', 'xhuso']
    #leetList = ['h4770', 'hall0']
    
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['TWITCH_BOT_NICK'].lower():
        return
    #elif ctx.author.name.lower() == 'zeldafanchris'.lower():
        #return
    await bot.handle_commands(ctx)
    #await ctx.channel.send(ctx.content) #| annoying repeating messages
    if any(word in greet for word in greetList):
        await ctx.channel.send(f"/me {random.choice(greetAnswer)} @{ctx.author.name}!")
    elif any(word in stateM for word in greetWList):
        await ctx.channel.send(f"/me {random.choice(greetWAnswer)} @{ctx.author.name}")
    elif any(word in husoN for word in husoList):
        await ctx.channel.send(f"/me {random.choice(husoAnswer)} @{ctx.author.name}")
    #elif any(word in leetN for word in leetList):
        #await ctx.channel.send(f"/me {random.choice(husoAnswer)} @{ctx.author.name}")
    
        
@bot.event
async def event_command_error(ctx, error):
    await ctx. channel.send(f'/me Error running command: {error} @{ctx.message.author.name}')

@bot.command(name='test')
async def test(ctx):
    testOP = "user: " + str(ctx.author.name) + " with the id: " + str(ctx.author.id) + " ran test in channel: " + str((os.environ['CHANNEL']))
    print(testOP)
    await ctx.send(testOP)

@bot.command(name='calc')
async def calc(ctx):
    ErrorFree = True
    useless, calc1, calcR, calc2 = ctx.content.split(' ')
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
                await ctx.channel.send(f"invalid operator @{ctx.author.name} - Possible Operators: '+' '-' ':' '*'")
            if ErrorFree:
                await ctx.channel.send(calcE)
        else:
            await ctx.channel.send("Invalid syntax")

@bot.command(name='operators')
async def operators(ctx):
    await ctx.channel.send("Possible Operators: '+' '-' ':' '*'")

@bot.command(name='clip')
async def clip(ctx):
    await bot.create_clip((os.environ['TMI_TOKEN']), (os.environ['CHANNEL']))

@bot.command(name='listusers')
async def listusers(ctx):
    #Chatters = await bot.get_chatters((os.environ['CHANNEL']))
    #print(Chatters)
    lUc = "/me {}" + str(await bot.get_chatters((os.environ['CHANNEL'])))
    lUc = lUc.replace("'", "")
    lUc = lUc.replace("(", " ")
    lUc = lUc.replace(")", "")
    lUc = lUc.replace("{", "")
    lUc = lUc.replace("}", "")
    lUc = lUc.replace("[", "")
    lUc = lUc.replace("]", "")
    lUc = lUc.replace("Chatters count=", "Users=")
    await ctx.channel.send(lUc)


@bot.command(name='timeout')
async def timeout(ctx, user):
    if str(ctx.author.is_mod)=="True":
        useless, cU, cT, cR = ctx.content.split(' ')
        await ctx.timeout(str(cU), int(cT), str(cR))
        mTs = "/me Set " + str(cU) + " for " + str(cT) + " seconds in timeout. Reason: " + str(cR)
        await ctx.channel.send((mTs))
    else:
        await ctx.channel.send("/me Netter Versuch, der Command ist nur für Mods :)")

@bot.command(name='event')
async def event(ctx, user):
    if str(ctx.author.is_mod)=="True":
        useless, eventstatus = ctx.content.split(' ')
        eventFile = open("Event", "r")
        eventLines = eventFile.readlines()
        for eventLine in eventLines:
            eventSF = str(eventLine)
        if eventstatus=='open' and eventSF=='open':
            await ctx.channel.send("/me Event is already opened.")
        elif eventstatus=='open' and eventSF!='open':
            eventFile.close()
            eventCFile = open("Event", "w+")
            eventCFile.write(eventstatus)
            eventSs = "/me Event is now " + eventstatus + ". You can now enter !get to recieve 100 credits each time."
            await ctx.channel.send(eventSs)
        elif eventstatus=='close' and eventSF=='close':
            await ctx.channel.send("/me Event is already closed")
        elif eventstatus=='close' and eventSF!='close':
            eventFile.close()
            eventCFile = open("Event", "w+")
            eventCFile.write(eventstatus)
            eventSsC = (f"/me Event is now closed ({eventstatus})")
            await ctx.channel.send(eventSsC)
        else:
            await ctx.channel.send(f"/me invalid input {ctx.author.name}")
    else:
        await ctx.channel.send("/me Netter Versuch, der Command ist nur für Mods :)")

@bot.command(name='dice')
async def dice(ctx, sides):
    if RepresentsInt(sides):
        sides = int(sides)
        if sides<1:
            await ctx.send('invalid number of sides')
        else:
            dice = [str(random.choice(range(1, sides + 1)))]
            await ctx.channel.send(random.choice(dice))
    else:
        await ctx.send("invalid input")

@bot.command(name='get')
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
            await ctx.channel.send(f"/me File for {ctx.author.name} created.")
        finally:
            if eventstatusS=='close':
                await ctx.channel.send("/me Event currently not running.")
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
                    eventRsS = "/me " + l + " has participated. Balance: " + str(eventRC)
                    await ctx.channel.send(eventRsS)
            else:
                await ctx.channel.send("/me Event currently not running.")
    else:
        await ctx.channel.send(f"/me Not able to participate, event closed ({eventstatusS})")
            

#@bot.command(name='followage')
#async def followage(ctx):
    #await ctx.channel.send(await bot.get_follow(({ctx.author.id}), (channelid)))

@bot.command(name='flip')
async def flip(ctx):
    l = (f"{ctx.author.name}")
    try:
        k = open((l), "r")
    except FileNotFoundError:
        print("Creating file...")
        cr = open((l), "w+")
        cr.write("1000")
        cr.close()
        print(f"File: {ctx.author.name} created!")
        await ctx.channel.send(f"/me File for {ctx.author.name} created.")
    finally:
        k = open((l), "r")
        lines = k.readlines()
        punkte = 0
        for line in lines:
            conv_int = int(line)
            punkte = punkte + conv_int
            k.close()
            useless, betAmount = ctx.content.split(' ')
            try:
                betAmount = int(betAmount)
                VEerror = True
            except ValueError:
                await ctx.channel.send(f"/me invalid syntax @{ctx.author.name}")
                VEerror = False
            finally:
                if VEerror:
                    if betAmount >= 0 :
                        if betAmount > punkte:
                            await ctx.channel.send("/me You do not have enough credits!")
                        elif betAmount <=punkte:
                            #define flip
                            coin = ('win', 'loss')
                            flip = random.choice(coin)
                            if flip=="win":
                                punkte=punkte+betAmount
                                meW = "/me " + l + " won, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meW))
                            elif flip=="loss":
                                punkte=punkte-betAmount
                                meL = "/me " + l + " lost, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meL))
                        else:
                            await ctx.channel.send(f"/me invalid syntaxn background @{ctx.author.name}")
                    else:
                        await ctx.channel.send(f"/me Positive numbers only @{ctx.author.name}")
            
        #saving stats to ({ctx.author.name}) file
        f = open((l), "w")
        f.write(str(punkte))
        f.close()

@bot.command(name='credits')
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
        await ctx.channel.send(f"/me File for {ctx.author.name} created.")
    finally:
        creditsCommandCheck = open((creditsCommand), "r")
        creditsLines = creditsCommandCheck.readlines()
        for creditsLine in creditsLines:
            creditsCheckInt = int(creditsLine)
            await ctx.channel.send(f"/me {ctx.author.name} has {creditsCheckInt} credits.")
    if creditsCheckInt < 100:
        await ctx.channel.send(f"/me i felt bad for @{ctx.author.name} and gave him 300 credits.")
        creditsCheckInt = creditsCheckInt+300
        f = open((creditsCommand), "w")
        f.write(str(creditsCheckInt))
        f.close()
        await ctx.channel.send(f"/me {ctx.author.name} now has {creditsCheckInt} credits.")
    else:
        pass

@bot.command(name='gift')
async def gift(ctx):
    giftUser1 = (f"{ctx.author.name}")
    try:
        giftFile = open((giftUser1), "r")
    except FileNotFoundError:
        print("Creating file...")
        giftFile = open((giftUser1), "w+")
        giftFile.write("1000")
        giftFile.close()
        print(f"File: {ctx.author.name} created!")
        await ctx.channel.send(f"/me File for {ctx.author.name} created.")
    finally:
        giftFile = open((giftUser1), "r")
        giftLines = giftFile.readlines()
        for giftLine in giftLines:
            giftC = int(giftLine)
            useless, giftR, giftAmount = ctx.content.split(' ')
            GRError = True
            giftAmount = int(giftAmount)
            if giftAmount <= giftC and giftAmount >= 0:
                try:
                    giftRFile = open((giftR), "r")
                except FileNotFoundError:
                    await ctx.channel.send(f"/me Receiving user not found or invalid amount")
                    GRError = False
                finally:
                    if GRError:
                        giftRFile = open((giftR), "r")
                        giftRLines = giftRFile.readlines()
                        for giftRLine in giftRLines:
                            giftRC = int(giftRLine)
                            giftRC = giftRC+giftAmount
                            giftC = giftC-giftAmount
                            giftRFile.close()
                            giftFile.close()
                            giftDone = open((giftUser1), "w+")
                            giftDone.write(str(giftC))
                            giftRDone = open((giftR), "w+")
                            giftRDone.write(str(giftRC))
                            await ctx.channel.send (f"/me @{ctx.author.name} sent {giftAmount} credits to {giftR}.")
                    else:
                        break
            elif giftAmount < 0:
                await ctx.channel.send("invalid gift amount")

@bot.command(name='commands')
async def commands(ctx):
    await ctx.channel.send("/me !flip [betAmount]")
    await ctx.channel.send("/me !gift [user] [giftAmount]")
    await ctx.channel.send("/me !credits")
    await ctx.channel.send("/me (mod-only) !timeout [user] [time] [reason]")
    await ctx.channel.send("/me !listusers")
    await ctx.channel.send("/me (broken) !clip")
    await ctx.channel.send("/me !test")
    await ctx.channel.send("/me !calc [number] [operator] [number]")
    await ctx.channel.send("/me !operators")
    await ctx.channel.send("/me !dice [number of sides]")

#async def franzosen(ctx):
#    if "bonjour" in frG:  
#        await ctx.channel.send(f"huso, keine franzsosen in diesem stream DansGame")
#        franzosen = str(ctx.author.name)
#        await ctx.timeout((franzosen), int(60), str("Keine Franzosen")) #Timeout 60 Sekunden
    

if __name__ == "__main__":
    bot.run()

