import os # for importing env vars for the bot to use
import random
from twitchio.ext import commands
from dotenv import load_dotenv
import asyncio
import datetime as DT

load_dotenv()
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
ttsCost=500

greetAnswer = ['Hi! selphyHi', 'Auch hier? selphyHi', 'Lang nicht gesehen selphyHi', 'Hey, was geht? selphyHi', 'Tag, haben wir uns schonmal gesehen? selphyHi']
greetList = ['vertik1sachse', 'vertik1geist', 'vertik1flex', 'snaqblank', 'joelucutz', 'joelucutz,', 'hello', 'hello,', 'hi', 'hi,', 'tag', 'tag,', 'hallo', 'hallo,', 'selphyhi', 'selphyhi,', 'moin', 'moin,', 'servus', 'servus,', 'grüße', 'grüße,', 'hey', 'hey,', 'sup', 'sup,', 'hay', 'hay,' 'hoi', 'hoi,']
greetWList = ['wie gehts', 'was geht', 'und dir?', 'deine lage?', 'bei dir?']
greetWAnswer = ['Ganz okay... hoffentlich bald Feierabend selphySweat', 'Mir gehts ganz gut und selber? selphySmug', 'Das geht dich nichts an! selphyPout', 'Meine Lage ist unbestimmt seit der Zeit in Vietnam selphySad', 'Sag du es mir selphyIQ', 'Die Frage ist, wie gehts DIR? selphyAra', 'Lass dir mal ne andere Frage einfallen selphyRage']
husoList = ['huso', 'haʟʟo', 'haʟʟo,', 'haiio', 'hailo', 'hailo,', 'halio', 'halio,', 'haiio,', 'halo', 'halo,', 'was los klaus', 'alles husos', 'husos', 'erschieß dich', 'erschiess dich', 'account vor drei minuten erstellt', 'xhuso']
husoAnswer = ['Alles Husos, was los Klaus.', 'Account vor drei Minuten erstellt, ahja', 'ahja', 'xhuso']
ripList = ['rip', 'rip,', 'f', 'f,', 'selphysad', 'noo', 'nooo', 'noooo']
ripAnswer = ['F', 'NOOO', 'WHY', 'warum tust du das?', 'alles husos', 'beim nächsten mal läufts bestimmt besser']

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

#@bot.event
#async def event_join(user):
#    ej = bot._ws
#    filterUser = str(f"{user}")
#    filterUser = filterUser.replace("<User name=", "")
#    c1nc = CHANNEL1.lower()
#    c2nc = CHANNEL2.lower()
#    if f"channel={c1nc}" in filterUser:
#        filterUser = filterUser.replace(f"channel={c1nc}>", "")
#        print(f"{filterUser}joined. (JoinEvent)")
#        await ej.send_privmsg(f"{c1nc}", f"/me Twitch says {filterUser} hi. selphyHi (JoinEvent)")
#    elif f"channel={c2nc}" in filterUser:
#        filterUser = filterUser.replace(f"channel={c2nc}>", "")
#        print(f"{filterUser}joined. (JoinEvent)")
#        await ej.send_privmsg(f"{c2nc}", f"/me Twitch says {filterUser} hi. selphyHi (JoinEvent)")
#    else:
#        print(f"event_join couldn't find channel")
#    
#@bot.event
#async def event_part(user):
#    ep = bot._ws
#    filterUserP = str(f"{user}")
#    filterUserP = filterUserP.replace("<User name=", "")
#    c1nc2 = CHANNEL1.lower()
#    c2nc2 = CHANNEL2.lower()
#    if f"channel={c1nc2}" in filterUserP:
#        filterUserP = filterUserP.replace(f"channel={c1nc2}>", "")
#        print(f"{filterUserP} left. (LeaveEvent)")
#        await ep.send_privmsg(f"{c1nc2}", f"/me Twitch says {filterUserP} bye. (LeaveEvent)")
#    elif f"channel={c2nc2}" in filterUserP:
#        filterUserP = filterUserP.replace(f"channel={c2nc2}>", "")
#        print(f"{filterUserP} left. (LeaveEvent)")
#        await ep.send_privmsg(f"{c2nc2}", f"/me Twitch says {filterUserP} bye. (LeaveEvent)")
#    else:
#        print(f"event_part couldn't find channel")

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    #shortened channelsend
    greet = ctx.content.lower()
    stateM = ctx.content.lower()
    husoN = ctx.content.lower()
    ripN = ctx.content.lower()
    ripN = greet.split(' ')
    greet = greet.split(' ')
    
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['TWITCH_BOT_NICK'].lower():
        return
    elif ctx.author.name.lower() == 'zfcbot'.lower() or ctx.author.name.lower() == 'calitobot'.lower():
        return
    await bot.handle_commands(ctx)
    #await ctx.channel.send(ctx.content) #| annoying repeating messages
    if any(word in greet for word in greetList):
        await ctx.channel.send(f"/me {random.choice(greetAnswer)} @{ctx.author.name}!")
    elif any(word in stateM for word in greetWList):
        await ctx.channel.send(f"/me {random.choice(greetWAnswer)} @{ctx.author.name}")
    elif any(word in husoN for word in husoList):
        await ctx.channel.send(f"/me {random.choice(husoAnswer)} @{ctx.author.name}")
    elif any(word in ripN for word in ripList):
        await ctx.channel.send(f"/me {random.choice(ripAnswer)} selphySad @{ctx.author.name}")
    elif 'selphytootl2' in ctx.content.lower():
        await ctx.channel.send("selphyTootl2")
        
@bot.event
async def event_command_error(ctx, error):
    error = str(error)
    if "was not found" not in error:
        errormessage = f"/me @{ctx.author.name}" + " Error: " + error
        await ctx.channel.send(errormessage)
    with open("commanderr.log", "a+") as errorfile:
        error = error + "\n"
        errorfile.write(error)

@bot.command(name='checkerrors')
async def checkerrors(ctx):
    if str(ctx.author.is_mod)=="True":
        if 'last' in ctx.content:
            with open("commanderr.log", "r") as f:
                for last_line in f:
                    fS = "/me Last error: " + last_line
                await ctx.channel.send(fS)
        elif 'last' not in ctx.content:
            with open("commanderr.log", "r") as f:
                errorcount = 0
                wnf = 0
                for line in f:
                    errorcount = errorcount + 1
                    if "was not found" in line:
                        wnf = wnf + 1
                errorcount = errorcount-1
                errormessage = "/me " + str(errorcount) + " errors have been logged. " + str(wnf) + " were CommandNotFound errors"
                await ctx.channel.send(errormessage)
    else:
        await ctx.channel.send("/me Netter Versuch, der Command ist nur für Mods :)")

@bot.command(name='test')
async def test(ctx):
    testOP = "/me user: " + str(ctx.author.name) + " with the id: " + str(ctx.author.id) + " ran test"
    print(testOP)
    await ctx.channel.send(testOP)

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

@bot.command(name='marry')
async def marry(ctx):
    if (ctx.channel.name)==CHANNEL1:
        mchoices = ['yes'] * 1 + ['no'] * 99
        persuade = ['selphyNuu', 'selphyGasm', 'selphyAra', 'selphySad', 'vertik1Geist', 'selphyPat', 'selphySweat']
        persuadePercentage = 4
        persuadeBitPercentage = 99
        persuadeBit = ['cheer1000', 'cheer5000', 'cheer50000']
        if any(word in ctx.content.split(' ') for word in persuade):
            x = 0
            while x < persuadePercentage:
                mchoices.remove('no')
                x = x+1
            while x > 0:
                mchoices.append('yes')
                x = x-1
        elif any(word in ctx.content.split(' ') for word in persuadeBit):
            x = 0
            while x < persuadeBitPercentage:
                mchoices.remove('no')
                x = x+1
            while x > 0:
                mchoices.append('yes')
                x = x-1
        yes, no = 0, 0
        for p in mchoices:
            if p=='yes':
                yes = yes+1
            elif p=='no':
                no = no+1
        myes = random.choice(mchoices)
        print(f"{ctx.author.name} used !marry in channel {CHANNEL1} and had a", yes, "% Chance to win, ", no, f"% to lose. Result: {myes}")
        with open("marry", "r") as marryF:
            for mcontent in marryF:
                if mcontent==f"{ctx.author.name}":
                    await ctx.channel.send(f"/me @{ctx.author.name} we are already married, are you trying to cheat on me? selphyNANI")
                elif myes=='yes':
                    with open("marry", "w+") as marryF:
                        marryF.write(f"{ctx.author.name}")
                        await ctx.channel.send(f"/me YES I WILL selphyPog @{ctx.author.name}")
                elif myes=='no':
                    with open("marry", "r") as marryF:
                        for mcontent in marryF:
                            mpass = [f"/me No, never selphyPout @{ctx.author.name}", f"/me Not even in your dreams selphyRage @{ctx.author.name}", f"/me Not like this selphyPout @{ctx.author.name}", f"/me Get a little more creative selphyIQ @{ctx.author.name}"]
                            manswer = random.choice(mpass) + f" (i am still married to {mcontent})"
                            await ctx.channel.send(manswer)
    else:
        mchoices = ['yes'] * 1 + ['no'] * 99
        persuade = ['selphyNuu', 'selphyGasm', 'selphyAra', 'selphySad', 'vertik1Geist', 'selphyPat', 'selphySweat']
        persuadePercentage = 4
        persuadeBitPercentage = 99
        persuadeBit = ['cheer1000', 'cheer5000', 'cheer50000']
        if any(word in ctx.content.split(' ') for word in persuade):
            x = 0
            while x < persuadePercentage:
                mchoices.remove('no')
                x = x+1
            while x > 0:
                mchoices.append('yes')
                x = x-1
        yes, no = 0, 0
        for p in mchoices:
            if p=='yes':
                yes = yes+1
            elif p=='no':
                no = no+1
        myes = random.choice(mchoices)
        print(f"{ctx.author.name} used !marry in channel {CHANNEL2} and had a", yes, "% Chance to win, ", no, f"% to lose. Result: {myes}")
        with open("marry", "r") as marryF:
            for mcontent in marryF:
                if mcontent==f"{ctx.author.name}":
                    await ctx.channel.send(f"/me @{ctx.author.name} we are already married, are you trying to cheat on me? selphyNANI")
                elif myes=='yes':
                    with open("marry", "w+") as marryF:
                        marryF.write(f"{ctx.author.name}")
                        await ctx.channel.send(f"/me YES I WILL selphyPog @{ctx.author.name}")
                elif myes=='no':
                    with open("marry", "r") as marryF:
                        for mcontent in marryF:
                            mpass = [f"/me No, never selphyPout @{ctx.author.name}", f"/me Not even in your dreams selphyRage @{ctx.author.name}", f"/me Not like this selphyPout @{ctx.author.name}", f"/me Get a little more creative selphyIQ @{ctx.author.name}"]
                            manswer = random.choice(mpass) + f" (i am still married to {mcontent})"
                            await ctx.channel.send(manswer)

@bot.command(name='divorce')
async def divorce(ctx):
    with open("marry", "r") as marryF:
        for mcontent in marryF:
            if mcontent==f"{ctx.author.name}":
                with open("marry", "w+") as marryF:
                    marryF.write(f"noone")
                    await ctx.channel.send(f"/me WHAT? YOU CANT JUST UN-MARRY ME selphyNANI ({os.environ['TWITCH_BOT_NICK']} is now married to noone)")
            elif mcontent!=f"{ctx.author.name}":
                await ctx.channel.send(f"/me We are not even married @{ctx.author.name} selphyPout")

@bot.command(name='operators')
async def operators(ctx):
    await ctx.channel.send("/me Possible Operators: '+' '-' ':' '*'")

@bot.command(name='clip')
async def clip(ctx):
    await bot.create_clip((os.environ['TMI_TOKEN']), (os.environ['CHANNEL']))

@bot.command(name='listusers')
async def listusers(ctx):
    #Chatters = await bot.get_chatters((os.environ['CHANNEL']))
    #print(Chatters)
    lUc = str(await bot.get_chatters((f"{CHANNEL1}")))
    lUc = lUc.replace("'", "")
    lUc = lUc.replace("(", " ")
    lUc = lUc.replace(")", "")
    lUc = lUc.replace("{", "")
    lUc = lUc.replace("}", "")
    lUc = lUc.replace("[", "")
    lUc = lUc.replace("]", "")
    lUc = lUc.replace("Chatters count=", "Users=")
    lUc = f"Users in channel {CHANNEL1}: " + lUc
    await ctx.channel.send(lUc)

@bot.command(name='pomf')
async def pomf(ctx):
    liste = random.choice([greetAnswer, greetWAnswer, husoAnswer, ripAnswer])
    listeSmol = random.choice(liste)
    listeMessage = "/me " + listeSmol + f" @{ctx.author.name} selphyHae"
    await ctx.channel.send(listeMessage)

@bot.command(name='lotto')
async def lotto(ctx, *l):
    lottoUser = (f"{ctx.author.name}")
    try:
        open((lottoUser), "r")
    except FileNotFoundError:
        print("Creating file...")
        cr = open((lottoUser), "w+")
        cr.write("1000")
        cr.close()
        print(f"File: {ctx.author.name} created!")
        await ctx.channel.send(f"/me File for {ctx.author.name} created.")
    finally:
        lottoUserF = open((lottoUser), "r")
        lottoUserLines = lottoUserF.readlines()
        for lottoUserLine in lottoUserLines:
            lottoUserFC = str(lottoUserLine)
            lottoUserFC = int(lottoUserFC)
            lottoUserF.close()
            useless, *lottoG = ctx.content.split(' ')
            if 'jackpot' in lottoG:
                with open("jackpot", "r") as jackpotF:
                    for jackpotL in jackpotF:
                        jackpotL = int(jackpotL)
                        await ctx.channel.send(f"/me Jackpot is at {jackpotL} credits. @{ctx.author.name}")
                        lottoStatus='check'
            elif 'jackpot' not in lottoG:
                with open("jackpot", "r") as jackpotF:
                    for jackpotL in jackpotF:
                        jackpotL = int(jackpotL)
                        price = 2400
                        price = price/(len(lottoG))
                        price = int(price)
                        priceLoss = len(lottoG)*100
                        lottoUserFC = lottoUserFC-priceLoss
                        lottoN = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21')
                        lottoR = random.choice(lottoN)
                        lottoGAnzahl = (len(lottoG))
                        if lottoUserFC>=priceLoss: 
                            lottoNS = "/me Lotto Number: " + lottoR
                            await ctx.channel.send(lottoNS)
                            if lottoGAnzahl== 1 and lottoR in lottoG:
                                await ctx.channel.send(f"/me @{ctx.author.name} won the jackpot. ({jackpotL}) selphyPog")
                                with open((lottoUser), "w+") as lottoUserF:
                                    lottoUserFC = lottoUserFC+jackpotL
                                    lottoUserFC = str(lottoUserFC)
                                    lottoUserF.write(lottoUserFC)
                                with open("jackpot", "w+") as jackpotF3:
                                    jackpotWrite = 0
                                    jackpotF3.write(str(jackpotWrite))
                                    lottoStatus = 'jackpot'
                            elif lottoGAnzahl != 1 and lottoR in lottoG:
                                lottoStatus = 'won'
                                lottoUserFC = lottoUserFC+price
                                lottoUserF.close()
                                lottoUserF = open((lottoUser), "w+")
                                lottoUserFC = str(lottoUserFC)
                                lottoUserF.write(lottoUserFC)
                                lottoWS = f"/me {ctx.author.name} won " + str(price) + " credits. Balance: " + str(lottoUserFC)
                                await ctx.channel.send(lottoWS)
                            else:
                                lottoStatus = 'lost'
                                lottoUserF.close()
                                lottoUserF = open((lottoUser), "w+")
                                lottoUserFC = str(lottoUserFC)
                                lottoUserF.write(lottoUserFC)
                                lottoUserF.close()
                                lottoLS = f"/me {ctx.author.name} lost " + str(priceLoss) + " credits. Balance: " + str(lottoUserFC)
                                await ctx.channel.send(lottoLS)
                        else:
                            lottoStatus = 'error'
                            await ctx.channel.send("/me You don't have enough credits!")
    if lottoStatus=='lost':
        with open("jackpot", "w+") as jackpotF:
            jackpotL = priceLoss+jackpotL
            jackpotF.write(str(jackpotL))

@bot.command(name='tts')
async def tts(ctx, *speech):
    ttsUser = (f"{ctx.author.name}")
    try:
        open((ttsUser), "r")
    except FileNotFoundError:
        print("Creating file...")
        cr = open((ttsUser), "w+")
        cr.write("1000")
        cr.close()
        print(f"File: {ctx.author.name} created!")
        await ctx.channel.send(f"/me File for {ctx.author.name} created.")
    finally:
        ttsUserF = open((ttsUser), "r")
        ttsUserLines = ttsUserF.readlines()
        for ttsUserLine in ttsUserLines:
            ttsUserFC = str(ttsUserLine)
            ttsUserFC = int(ttsUserFC)
            if ttsUserFC>=ttsCost:
                ttsUserFC -= (ttsCost)
                ttsUserFC = str(ttsUserFC)
                ttsUserF.close()
                ttsUserF = open((ttsUser), "w+")
                ttsUserF.write(ttsUserFC)
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
                TextVar = 'espeak ' + (speech)
                os.system(TextVar)
            elif ttsUserFC<ttsCost:
                await ctx.channel.send(f"/me You don't have enough credits @{ctx.author.name}")

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
            await ctx.send(f'/me @{ctx.author.name} invalid number of sides')
        else:
            dice = str(random.choice(range(1, sides + 1)))
            if sides>1 and int(dice) == int(sides):
                reward = 50 * int(sides) # amount of credits earned per side
                with open((ctx.author.name), "r") as howmuchfile:
                    userCurrency = howmuchfile.readline()
                    userCurrency = int(userCurrency) + reward
                with open((ctx.author.name), "w+") as howmuchfile:
                    howmuchfile.write(str(userCurrency))
                diceMessage = f"/me @{ctx.author.name} " + str(dice) + f" is the same number as the number of sides, congrats take these {reward} credits. selphyPray"
                await ctx.channel.send(diceMessage)
            elif dice != sides:
                diceMessage = f"/me @{ctx.author.name} Your number is: " + dice
                await ctx.channel.send(diceMessage)
    else:
        await ctx.channel.send("invalid input")

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
            
@bot.command(name='flip')
async def flip(ctx):
    l = (f"{ctx.author.name}")
    mf = 25 # Minimum Flip
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
                VEerror = False
            finally:
                if VEerror:
                    if betAmount > mf :
                        if betAmount > punkte:
                            flipStatus = 'error'
                            await ctx.channel.send("/me You do not have enough credits!")
                        elif betAmount <= punkte:
                            #define flip
                            coin = ('win', 'loss')
                            flip = random.choice(coin)
                            if flip=="win":
                                flipStatus = 'won'
                                punkte=punkte+betAmount
                                meW = "/me " + l + " won, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meW))
                            elif flip=="loss":
                                flipStatus = 'lost'
                                punkte=punkte-betAmount
                                meL = "/me " + l + " lost, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meL))
                        else:
                            flipStatus = 'error'
                            await ctx.channel.send(f"/me invalid syntax @{ctx.author.name}")
                    elif betAmount < mf:
                        flipStatus = 'error'
                        await ctx.channel.send(f"/me {mf} is the minimum flipable value @{ctx.author.name}")
                    else:
                        flipStatus = 'error'
                        await ctx.channel.send(f"/me Positive numbers only @{ctx.author.name}")
                elif VEerror==False:
                    if betAmount=='all' or betAmount=='max':
                        betAmount = punkte
                        if betAmount >= mf:
                            coin = ('win', 'loss')
                            flip = random.choice(coin)
                            if flip=="win":
                                flipStatus = 'won'
                                punkte=punkte+betAmount
                                meW = f"/me @{ctx.author.name} went all in and won, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meW))
                            elif flip=="loss":
                                flipStatus = 'lost'
                                punkte=punkte-betAmount
                                meL = f"/me @{ctx.author.name} went all in and lost, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meL))
                        elif betAmount < mf:
                            flipStatus = 'error'
                            await ctx.channel.send(f"/me {mf} is the minimum flipable value @{ctx.author.name}")
                    else:
                        flipStatus = 'error'
                        await ctx.channel.send(f"/me invalid syntax @{ctx.author.name}")
                    
            
        #adding lost amount to jackpot
        if flipStatus=='lost':
            with open("jackpot", "r") as jackpotF:
                for jackpotL in jackpotF:
                    jackpotL = int(jackpotL)
                    jackpotL = betAmount+jackpotL
                    with open("jackpot", "w+") as jackpotF2:
                        jackpotF2.write(str(jackpotL))
        
        #saving stats to ({ctx.author.name}) file
        f = open((l), "w")
        f.write(str(punkte))
        f.close()

@bot.command(name='luv')
async def luv(ctx, *luvtarget):
    luvChoice = random.choice(range(1, 101))
    luvtarget = str(luvtarget)
    luvtarget = luvtarget.replace("(", "")
    luvtarget = luvtarget.replace(")", "")
    luvtarget = luvtarget.replace("'", "")
    luvtarget = luvtarget.replace(",", "")
    if luvChoice<=1:
        await ctx.timeout((ctx.author.name), 60, "doesn't have enough luv in their live")
    elif luvChoice<15 and luvChoice>0:
        selphyEmote='selphyCringe'
    elif luvChoice<36 and luvChoice>14:
        selphyEmote='selphyNuu'
    elif luvChoice>35 and luvChoice<65:
        selphyEmote='selphyWTF'
    elif luvChoice>64 and luvChoice<85:
        selphyEmote='selphyTootl2'
    elif luvChoice>84 and luvChoice<100:
        selphyEmote='selphyPray'
    elif luvChoice==100:
        selphyEmote='selphyNANI'
    luvMessage = f"/me @{ctx.author.name} and {luvtarget} have a {luvChoice}% chance to fall in luv {selphyEmote}"
    await ctx.channel.send(luvMessage)

@bot.command(name='credits')
async def credits(ctx):
    creditsCommand = (f"{ctx.author.name}")
    pityC = 300 #Amount of Pity Credits
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
        cchoices = ['yes'] * 20 + ['no'] * 80
        cyes = random.choice(cchoices)
        if cyes=='yes':
            creditsCheckInt = creditsCheckInt+300
            f = open((creditsCommand), "w")
            f.write(str(creditsCheckInt))
            f.close()
            await ctx.channel.send(f"/me I felt bad for @{ctx.author.name} and gave him {pityC} credits. selphyPray {ctx.author.name} now has {creditsCheckInt} credits.")
    else:
        pass

@bot.command(name='gift')
async def gift(ctx):
    giftUser1 = (f"{ctx.author.name}")
    useless, giftR, giftAmount = ctx.content.split(' ')
    giftR = giftR.lower()
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
        try:
            giftAmount = int(giftAmount)
            VEerror = True
        except ValueError:
            VEerror = False
        finally:
            if VEerror:
                giftFile = open((giftUser1), "r")
                giftLines = giftFile.readlines()
                for giftLine in giftLines:
                    giftC = int(giftLine)
                    if giftAmount <= giftC and giftAmount > 0:
                        try:
                            giftRFile = open((giftR), "r")
                            GRError = True
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
                                    await ctx.channel.send(f"/me @{ctx.author.name} sent {giftAmount} credits to {giftR}.")
                            else:
                                break
                    elif giftAmount <= 0:
                        await ctx.channel.send(f"/me @{ctx.author.name} invalid gift amount")
                    elif giftC < giftAmount:
                        await ctx.channel.send(f"/me @{ctx.author.name} not enough credits!")
            elif giftAmount=='all' or giftAmount=='max':
                giftFile = open((giftUser1), "r")
                giftLines = giftFile.readlines()
                for giftLine in giftLines:
                    giftC = int(giftLine)
                    giftAmount = giftC
                    if giftAmount > 0:
                        try:
                            giftRFile = open((giftR), "r")
                            GRError = True
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
                                    await ctx.channel.send(f"/me @{ctx.author.name} sent {giftAmount} credits to {giftR}.")
                            else:
                                break
                    elif giftAmount <= 0:
                        await ctx.channel.send(f"/me @{ctx.author.name} you're broke selphyLUL")
            elif VEerror==False:
                await ctx.channel.send(f"/me @{ctx.author.name} thats not a number! selphyPout")

@bot.command(name='asynctest')
async def asynccommand(ctx):
    await ctx.channel.send("alles husos")

@bot.command(name='commands')
async def commands(ctx):
    cS = "/me Commands: "
    cL = []
    for c in bot.commands:
        cA = "!" + c
        cL.append(cA)
    cL = str(cL)
    cL = cL.replace("[", "")
    cL = cL.replace("]", "")
    cL = cL.replace("'", "")
    await ctx.channel.send(cS + str(cL))
    
########################################
#    Starts the bot                    #
########################################

if __name__ == "__main__":
    bot.run()
