import os # for importing env vars for the bot to use
import random
from twitchio.ext import commands
from dotenv import load_dotenv
import asyncio
import datetime as DT
import json

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

@bot.command(name='ranking')
async def ranking(ctx):
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    ranking = []
    for item in entry:
        ranking.append({"name": item['name'], "balance": item['balance']})
    
    ranking = sorted(ranking, key=lambda k: k['balance'], reverse=True)
    ranking = ranking[:10]
    message = f"/me Top {len(ranking)}: " + ', '.join(d['name'] + " " + str(d['balance']) + " credits" for d in ranking)
    await ctx.channel.send(message)

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
                await ctx.channel.send(f"/me invalid operator @{ctx.author.name} - Possible Operators: '+' '-' ':' '*'")
            if ErrorFree:
                calcSend = "/me The Result is: " + str(calcE) + f" @{ctx.author.name}"
                await ctx.channel.send(calcSend)
        else:
            await ctx.channel.send(f"/me Invalid syntax @{ctx.author.name}")

@bot.command(name='marry')
async def marry(ctx, potential_spouse):
    if potential_spouse.lower()==os.environ['TWITCH_BOT_NICK'].lower():
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
    else:
        balance = 5000 #Default balance for newly added users
        found_user = False #Default
        potential_spouse = potential_spouse.lower()
        with open("ser.json", "r") as f:
            ser = json.load(f)
            entry = ser['user']
        
        partner = None
        user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }
    
        with open("ser.json", "r") as f:
            ser = json.load(f)
            entry = ser['user']
        
        for item in entry:
            if item['name'] == potential_spouse:
                potential_spouse = item
                found_user=True
        
        if found_user==False:
            await ctx.channel.send(f"/me Potential Spouse not found @{ctx.author.name}")
    
        elif found_user==True:
            for item in entry:
                if item['id'] == user['id']:
                    if potential_spouse['name'] in item['name']:
                        await ctx.channel.send(f"/me You can't marry yourself @{ctx.author.name}")
                        break
                    else:
                        potential_spouse['proposal'] = ctx.author.name
                        Partner = item['partner']
                        User = item['name']
                        ID = item['id']
                        Balance = item['balance']
                        #change name if user changed name
                        if user['name'] != User:
                            User = user['name']
                        item['name'] = str(User)
                        item['id'] = int(ID)
                        item['balance'] = int(Balance)
                        item['partner'] = Partner
                        await ctx.channel.send(f"/me @{ctx.author.name} sent a proposal to {potential_spouse['name']}")
                        with open("ser.json", "w") as f:
                                    o = json.dumps(ser, indent=2)
                                    f.write(o)
                        break
            else:
                item = None
                with open("ser.json", "w") as f:
                        entry.append(user)    
                        o = json.dumps(ser, indent=2)
                        f.write(o)
                await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")

@bot.command(name='accept')
async def accept(ctx, proposal):
    balance = 5000 #Default balance for newly added users
    proposal = proposal.lower()
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['name'] == proposal:
            spouse = item
    
    for item in entry:
        if item['id'] == user['id']:
            if proposal==item['proposal']:
               spouse['proposal'] = None
               spouse['partner'] = ctx.author.name
               item['proposal'] = None
               item['partner'] = proposal
               await ctx.channel.send(f"/me @{ctx.author.name} is now married to {proposal}")
               with open("ser.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
               break
    else:
        await ctx.channel.send(f"/me No proposal from user {proposal} found. @{ctx.author.name}")

@bot.command(name='marriage')
async def marriage(ctx):
    balance = 5000 #Default balance for newly added users
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    for item in entry:
        if item['id'] == user['id']:
            if item['proposal'] != None:
                prop = "a proposal from" + item['proposal']
            else:
                prop = "no proposal"
            if item['partner'] != None:
                part = "married to " + item['partner']
            else:
                part = "single"
            await ctx.channel.send(f"/me @{ctx.author.name} is currently {part} and has {prop}!")
            break

@bot.command(name='decline')
async def decline(ctx, proposal):
    balance = 5000 #Default balance for newly added users
    proposal = proposal.lower()
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    for item in entry:
        if item['id'] == user['id']:
            if proposal==item['proposal']:
               item['proposal'] = None
               await ctx.channel.send(f"/me @{ctx.author.name} declined the proposal from {proposal}")
               with open("ser.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
               break
    else:
        await ctx.channel.send(f"/me No proposal from user {proposal} found. @{ctx.author.name}")

@bot.command(name='divorce')
async def divorce(ctx, *yes):
    isbot = [isbot.lower() for isbot in yes]
    if os.environ['TWITCH_BOT_NICK'].lower() in isbot:
        with open("marry", "r") as marryF:
            for mcontent in marryF:
                if mcontent==f"{ctx.author.name}":
                    with open("marry", "w+") as marryF:
                        marryF.write(f"noone")
                        await ctx.channel.send(f"/me WHAT? YOU CANT JUST UN-MARRY ME selphyNANI ({os.environ['TWITCH_BOT_NICK']} is now married to noone)")
                elif mcontent!=f"{ctx.author.name}":
                    await ctx.channel.send(f"/me We are not even married @{ctx.author.name} selphyPout")
    else:
        balance = 5000 #Default balance for newly added users
        with open("ser.json", "r") as f:
            ser = json.load(f)
            entry = ser['user']
        
        partner = None
        user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }
    
        with open("ser.json", "r") as f:
            ser = json.load(f)
            entry = ser['user']
            
        for item in entry:
            if item['id'] == user['id']:
                Partner = item['partner']
                for spouse in entry:
                    if spouse['name'] == Partner:
                        spouse['partner'] = None
                item['partner'] = None
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                #change name if user changed name
                if user['name'] != User:
                    User = user['name']
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                if Partner==None:
                    candivorce = False
                else:
                    candivorce = True
                if candivorce==True:
                    await ctx.channel.send(f"/me @{ctx.author.name} got divorced from {Partner}")
                else:
                    await ctx.channel.send(f"/me @{ctx.author.name} is not married")
                with open("ser.json", "w") as f:
                            o = json.dumps(ser, indent=2)
                            f.write(o)
                break

@bot.command(name='operators')
async def operators(ctx):
    await ctx.channel.send("/me Possible Operators: '+' '-' ':' '*'")

@bot.command(name='clip')
async def clip(ctx):
    await bot.create_clip((os.environ['TWITCH_TMI_TOKEN']), (bot.get_channel))

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
async def lotto(ctx):
    balance = 5000 #Default balance for newly added users
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    partner = None
    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance,
        'partner': partner
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner=='t':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                #change name if user changed name
                if user['name'] != User:
                    User = user['name']
                lottoUser = User
                lottoUserFC = Balance
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
                                    lottoWS = f"/me {ctx.author.name} won " + str(price) + " credits. Balance: " + str(lottoUserFC)
                                    await ctx.channel.send(lottoWS)
                                else:
                                    lottoStatus = 'lost'
                                    lottoLS = f"/me {ctx.author.name} lost " + str(priceLoss) + " credits. Balance: " + str(lottoUserFC)
                                    await ctx.channel.send(lottoLS)
                            else:
                                lottoStatus = 'error'
                                await ctx.channel.send("/me You don't have enough credits!")
                Balance = lottoUserFC
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("ser.json", "w") as f:
                            o = json.dumps(ser, indent=2)
                            f.write(o)
                if lottoStatus=='lost':
                    with open("jackpot", "r") as jackpotF:
                        for jackpotL in jackpotF:
                            jackpotL = int(jackpotL)
                            jackpotL = priceLoss+jackpotL
                            with open("jackpot", "w+") as jackpotF2:
                                jackpotF2.write(str(jackpotL))
                break
    else:
        item = None
        with open("ser.json", "w") as f:
                entry.append(user)    
                o = json.dumps(ser, indent=2)
                f.write(o)
        await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")

@bot.command(name='del')
async def delete(ctx, name):
    if ctx.author.name==CHANNEL1:
        with open("ser.json", "r") as f:
            ser = json.load(f)
            entry = ser['user']
        
        for item in entry:
            if item['name'] == name:
                entry.remove(item)
                await ctx.channel.send(f'''/me User "{name}" with id {item['id']} sucessfully deleted.''')
                break
        else:
            await ctx.channel.send(f'/me No user called "{name}" found to delete.')
        with open("ser.json", "w") as f:
            o = json.dumps(ser, indent=2)
            f.write(o)
    else:
        await ctx.channel.send("/me Netter Versuch, der Command ist nur für Mods :)")

@bot.command(name='tts')
async def tts(ctx, *speech):
    balance = 5000 #Default balance for newly added users
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    partner = None
    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance,
        'partner': partner
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner=='t':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                #change name if user changed name
                if user['name'] != User:
                    User = user['name']
                ttsUserFC = Balance
                if not speech:
                    await ctx.channel.send(f"/me Atleast one word to read required! @{ctx.author.name}")
                else:
                    if ttsUserFC>=ttsCost:
                        ttsUserFC -= ttsCost
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
                Balance = ttsUserFC
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("ser.json", "w") as f:
                            o = json.dumps(ser, indent=2)
                            f.write(o)
                break
    else:
        item = None
        with open("ser.json", "w") as f:
                entry.append(user)    
                o = json.dumps(ser, indent=2)
                f.write(o)
        await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")

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
            eventSs = "/me Event is now " + eventstatus + ". You can now enter !get to receive 100 credits each time."
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
    balance = 5000 #Default balance for newly added users
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    partner = None
    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance,
        'partner': partner
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner=='t':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                #change name if user changed name
                if user['name'] != User:
                    User = user['name']
                userCurrency = Balance
                if RepresentsInt(sides):
                    sides = int(sides)
                    if sides<1:
                        await ctx.send(f'/me @{ctx.author.name} invalid number of sides')
                    else:
                        dice = str(random.choice(range(1, sides + 1)))
                        if sides>1 and int(dice) == int(sides):
                            reward = 50 * int(sides) # amount of credits earned per side
                            userCurrency = int(userCurrency) + reward
                            diceMessage = f"/me @{ctx.author.name} " + str(dice) + f" is the same number as the number of sides, congrats. Take these {reward} credits. selphyPray"
                            await ctx.channel.send(diceMessage)
                        elif dice != sides:
                            diceMessage = f"/me @{ctx.author.name} Your number is: " + dice
                            await ctx.channel.send(diceMessage)
                else:
                    await ctx.channel.send("invalid input")
                Balance = userCurrency
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("ser.json", "w") as f:
                            o = json.dumps(ser, indent=2)
                            f.write(o)
                break
    else:
        item = None
        with open("ser.json", "w") as f:
                entry.append(user)    
                o = json.dumps(ser, indent=2)
                f.write(o)
        await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")

@bot.command(name='get')
async def get(ctx):
    balance = 5000 #Default balance for newly added users
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    partner = None
    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance,
        'partner': partner
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner=='t':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                #change name if user changed name
                if user['name'] != User:
                    User = user['name']
                eventstatusF = open("Event", "r")
                eventstatusLines = eventstatusF.readlines()
                for eventstatusLine in eventstatusLines:
                    eventstatusS = str(eventstatusLine)
                l = user['name']
                eventRC = Balance
                if eventstatusS=='open':
                    if eventstatusS=='close':
                        await ctx.channel.send("/me Event currently not running.")
                    if eventstatusS == 'open':
                            eventRC = eventRC+100
                            eventRsS = "/me " + l + " has participated. Balance: " + str(eventRC)
                            await ctx.channel.send(eventRsS)
                    else:
                        await ctx.channel.send("/me Event currently not running.")
                else:
                    await ctx.channel.send(f"/me Not able to participate, event closed ({eventstatusS})")
                Balance = eventRC
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("ser.json", "w") as f:
                            o = json.dumps(ser, indent=2)
                            f.write(o)
                break
    else:
        item = None
        with open("ser.json", "w") as f:
                entry.append(user)    
                o = json.dumps(ser, indent=2)
                f.write(o)
        await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")
            
@bot.command(name='flip')
async def flip(ctx):
    balance = 5000 #Default balance for newly added users
    mf = 25 # Minimum Flip
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    partner = None
    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance,
        'partner': partner
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner=='t':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                #change name if user changed name
                if user['name'] != User:
                    User = user['name']
                punkte = Balance
                useless, betAmount = ctx.content.split(' ')
                try:
                    betAmount = int(betAmount)
                    VEerror = True
                except ValueError:
                    VEerror = False
                finally:
                    if VEerror:
                        if betAmount >= mf:
                            if betAmount > punkte:
                                flipStatus = 'error'
                                await ctx.channel.send("/me You do not have enough credits! @{ctx.author.name}")
                            elif betAmount <= punkte:
                                #define flip
                                coin = ('win', 'loss')
                                flip = random.choice(coin)
                                if flip=="win":
                                    flipStatus = 'won'
                                    punkte=punkte+betAmount
                                    meW = "/me " + user['name'] + " won, total: " + str(punkte) + " credits!"
                                    await ctx.channel.send((meW))
                                elif flip=="loss":
                                    flipStatus = 'lost'
                                    punkte=punkte-betAmount
                                    meL = "/me " + user['name'] + " lost, total: " + str(punkte) + " credits!"
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
                Balance = punkte
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("ser.json", "w") as f:
                            o = json.dumps(ser, indent=2)
                            f.write(o)
                if flipStatus=='lost':
                    with open("jackpot", "r") as jackpotF:
                        for jackpotL in jackpotF:
                            jackpotL = int(jackpotL)
                            jackpotL = betAmount+jackpotL
                            with open("jackpot", "w+") as jackpotF2:
                                jackpotF2.write(str(jackpotL))
                break
    else:
        item = None
        with open("ser.json", "w") as f:
                entry.append(user)    
                o = json.dumps(ser, indent=2)
                f.write(o)
        await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")

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
    balance = 5000 #Default balance for newly added users
    pityC = 300 #Amount of Pity Credits
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    partner = None
    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance,
        'partner': partner
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner=='t':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                #change name if user changed name
                if user['name'] != User:
                    User = user['name']
                if Balance < 100:
                    cchoices = ['yes'] * 20 + ['no'] * 80
                    cyes = random.choice(cchoices)
                    if cyes=='yes':
                        Balance = Balance+300
                        await ctx.channel.send(f"/me I felt bad for @{ctx.author.name} and gave him {pityC} credits. selphyPray {ctx.author.name} now has {Balance} credits.")
                    else:
                        await ctx.channel.send(f"/me @{user['name']} has {Balance} credits")
                else:
                    await ctx.channel.send(f"/me @{user['name']} has {Balance} credits")
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("ser.json", "w") as f:
                            o = json.dumps(ser, indent=2)
                            f.write(o)
                break
    else:
        item = None
        with open("ser.json", "w") as f:
                entry.append(user)    
                o = json.dumps(ser, indent=2)
                f.write(o)
        await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")

@bot.command(name='gift')
async def gift(ctx, giftR, giftAmount):
    balance = 5000 #Default balance for newly added users
    giftR = giftR.lower()
    found_user = False #Default
    everything = False #Default
    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
    
    user = {'name': ctx.author.name.lower(),
        'id': ctx.author.id,
        'balance': balance
        }

    with open("ser.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']
        
    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']
    for item in entry:
        if item['name'] == giftR:
            giftR = item
            found_user = True
            break
    
    if found_user==False:
        await ctx.channel.send(f"/me Receiving user not found @{ctx.author.name}")

    elif found_user==True:
        for item in entry:
            if item['id'] == user['id']:
                    Partner = item['partner']
                    User = item['name']
                    ID = item['id']
                    Balance = item['balance']
                    #change name if user changed name
                    if user['name'] != User:
                        User = user['name']
                    giftLine = Balance
                    try:
                        int(giftAmount)
                        VEerror = True
                    except ValueError:
                        VEerror = False
                    finally:
                        if VEerror:
                            giftAmount = int(giftAmount)
                            if not giftLine:
                                giftC = 0
                                giftRC = int(giftR['balance'])
                            else:
                                giftC = int(giftLine)
                            if giftAmount <= giftC and giftAmount > 0:
                                giftRC = int(giftR['balance'])
                                giftRC = giftRC+giftAmount
                                giftC = giftC-giftAmount
                                await ctx.channel.send(f"/me @{ctx.author.name} sent {giftAmount} credits to {giftR['name']}.")
                            elif giftAmount <= 0:
                                await ctx.channel.send(f"/me @{ctx.author.name} invalid gift amount")
                            elif giftC < giftAmount:
                                await ctx.channel.send(f"/me @{ctx.author.name} not enough credits!")
                        elif giftAmount=='all' or giftAmount=='max':
                            everything = True
                            giftC = int(giftLine)
                            giftAmount = giftC
                            if giftAmount > 0:
                                giftRC = int(giftR['balance'])
                                giftRC = giftRC+giftAmount
                                giftC = giftC-giftAmount
                                await ctx.channel.send(f"/me @{ctx.author.name} sent {giftAmount} credits to {giftR['name']}.")
                            else:
                                giftRC = int(giftR['balance'])
                                giftRC = giftRC+giftAmount
                                giftC = giftC-giftAmount
                                await ctx.channel.send(f"/me @{ctx.author.name} you're broke selphyLUL")
                        elif VEerror==False:
                            await ctx.channel.send(f"/me @{ctx.author.name} thats not a number! selphyPout")
                        if VEerror==True and giftAmount > 0 or everything==True and giftAmount > 0:
                            Balance = giftC
                            giftR['balance'] = giftRC
                        item['name'] = str(User)
                        item['id'] = int(ID)
                        item['balance'] = int(Balance)
                        item['partner'] = Partner
                        with open("ser.json", "w") as f:
                                    o = json.dumps(ser, indent=2)
                                    f.write(o)
                        break
        else:
            item = None
            with open("ser.json", "w") as f:
                    entry.append(user)    
                    o = json.dumps(ser, indent=2)
                    f.write(o)
            await ctx.channel.send(f"/me Added {ctx.author.name} - @{ctx.author.name} has {balance} credits.")

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
