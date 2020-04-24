import os
import discord
from dotenv import load_dotenv
import random
from discord.ext import commands
import time
import json
import satzgenerator
import asyncio
from lists import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

ownerImport = os.getenv('DISCORD_OWNER')

# client = discord.Client()
bot = commands.Bot(command_prefix=os.getenv('DISCORD_PREFIX'))

try:
    eventstatus
except NameError:
    eventFile = open("Event", "r")
    eventLines = eventFile.readlines()
    for eventLine in eventLines:
        eventstatus = str(eventLine)
finally:
    if eventstatus == 'close':
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
        # print(f'{member.name}#{member.discriminator} id: {member.id}')
    memberlist = '\n'.join(memberlist)
    # members = '\n - '.join([member.name for member in server.members])# + 'id: '.join(str([member.id for member in server.members]))
    # memberids = '\n - '.join(str([member.id for member in server.members]))
    # print(members)
    # print([member.id for member in server.members])
    memF = open("discordmembers.list", "w+")
    memF.write(memberlist)
    memF.close()


@bot.event
async def on_member_join(member):
    owner = bot.get_user((int(ownerImport)))
    newMember = (f"{member.name}")
    await owner.send(newMember)

@bot.event
async def on_member_update(before, after):
    n = after.nick
    if n: # Check if they updated their username
        if n.lower().count("ey") > 0: # If username contains ey
            pass
        else:
            last = before.nick
            if last: # If they had a username before change it back to that
                await after.edit(nick=last)
            else: # Otherwise set it to "NO STOP THAT"
                await after.edit(nick="NO STOP THAT")

@bot.event
async def on_message(message):
    user = message.author
    if discord.utils.get(user.roles, name="nolinks") is None:
        pass
    else:
        if "http" in message.content:
            await message.delete()
            g = await message.channel.send(f"You are not allowed to send links {message.author.name}")
            await asyncio.sleep(10)
            await g.delete()
    await bot.process_commands(message)


# @bot.event                                            #Absolutly broken dogshit
# async def on_error(event, *args, **kwargs):
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
    else:
        error = str(error)
        if "is not found" not in error:
            errormessage = " Error: " + error
            await ctx.send(errormessage)
        with open("discordcommanderr.log", "a+") as errorfile:
            error = error + "\n"
            errorfile.write(error)


@bot.command(name='test', help='poke the bot')
async def test(ctx):
    owner = bot.get_user((int(ownerImport)))
    await owner.send(f'{ctx.author.name} with id: {ctx.author.id} ran test')
    await ctx.send("no u")


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
        innocentF = (f"{innocentL}.mp4")
        await ctx.send("Trying to send file...")
        try:
            # await ctx.send("", file=discord.File(innocentF))
            await ctx.send(f"https://www.alleshusos.de/clips/archive/{innocentL}.mp4")
        except:
            await ctx.send("File too big!")
            await owner.send(f"{ctx.author.name} tried to convert {Uurl} but the file is too big to upload.")
        finally:
            pass


@bot.command(name='gift', help='send credits to another user, usage: !gift [receiver] [amount]')
async def gift(ctx, giftR, giftAmount):
    balance = 5000  # Default balance for newly added users
    found_user = False  # Default
    everything = False  # Default
    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    partner = None
    user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }

    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']
    for item in entry:
        if item['name'] == giftR:
            giftR = item
            found_user = True

    if found_user == False:
        await ctx.send(f"Receiving user not found {ctx.author.name}")

    elif found_user == True:
        for item in entry:
            if item['id'] == user['id']:
                if partner == 't':
                    entry.remove(item)
                else:
                    Partner = item['partner']
                    User = item['name']
                    ID = item['id']
                    Balance = item['balance']
                    # change name if user changed name
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
                            if not giftLine:
                                giftC = 0
                                giftRC = int(giftR['balance'])
                            else:
                                giftC = int(giftLine)
                            if giftAmount <= giftC and giftAmount > 0:
                                giftRC = int(giftR['balance'])
                                giftRC = giftRC + giftAmount
                                giftC = giftC - giftAmount
                                await ctx.send(f"{ctx.author.name} sent {giftAmount} credits to {giftR['name']}.")
                            elif giftAmount <= 0:
                                await ctx.send(f"{ctx.author.name} invalid gift amount")
                            elif giftC < giftAmount:
                                await ctx.send(f"{ctx.author.name} not enough credits!")
                        elif giftAmount == 'all' or giftAmount == 'max':
                            everything = True
                            giftC = int(giftLine)
                            giftAmount = giftC
                            if giftAmount > 0:
                                giftRC = int(giftR['balance'])
                                giftRC = giftRC + giftAmount
                                giftC = giftC - giftAmount
                                await ctx.send(f"{ctx.author.name} sent {giftAmount} credits to {giftR['name']}.")
                            else:
                                giftRC = int(giftR['balance'])
                                giftRC = giftRC + giftAmount
                                giftC = giftC - giftAmount
                                await ctx.send(f"{ctx.author.name} you're broke selphyLUL")
                        elif VEerror == True and giftAmount <= 0:
                            await ctx.send(f"{ctx.author.name} you're broke selphyLUL")
                        elif VEerror == False:
                            await ctx.send(f"{ctx.author.name} thats not a number! selphyPout")
                if VEerror == True or everything == True:
                    Balance = giftC
                    giftR['balance'] = giftRC
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("serD.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
                break
        else:
            item = None
            with open("serD.json", "w") as f:
                entry.append(user)
                o = json.dumps(ser, indent=2)
                f.write(o)
            await ctx.send(f"Added {ctx.author.name} - {ctx.author.name} has {balance} credits.")


@bot.command(name='checkerrors', help='check how many and what errors were logged (Moderator-only)')
@commands.has_role('Moderator')
async def checkerrors(ctx):
    if 'last' in ctx.content:
        with open("commanderr.log", "r") as f:
            for last_line in f:
                fS = "Last error: " + last_line
            await ctx.send(fS)
    elif 'last' not in ctx.content:
        with open("commanderr.log", "r") as f:
            errorcount = 0
            wnf = 0
            for line in f:
                errorcount = errorcount + 1
                if "was not found" in line:
                    wnf = wnf + 1
            errorcount = errorcount - 1
            errormessage = str(errorcount) + " errors have been logged. " + str(wnf) + " were CommandNotFound errors"
            await ctx.send(errormessage)


@bot.command(name='sg', help='generates a random sentence')
async def sg(ctx):
    message = satzgenerator.satz()
    await ctx.send(message)


@bot.command(name='marry', help='marry the bot')
async def marry(ctx, *pers):
    mchoices = ['yes'] * 1 + ['no'] * 99
    persuade = ['selphyNuu', 'selphyGasm', 'selphyAra', 'selphySad', 'vertik1Geist', 'selphyPat', 'selphySweat']
    persuadePercentage = 4
    if any(word in pers for word in persuade):
        x = 0
        while x < persuadePercentage:
            mchoices.remove('no')
            x = x + 1
        while x > 0:
            mchoices.append('yes')
            x = x - 1
    yes, no = 0, 0
    for p in mchoices:
        if p == 'yes':
            yes = yes + 1
        elif p == 'no':
            no = no + 1
    myes = random.choice(mchoices)
    print(f"{ctx.author.name} used !marry and had a", yes, "% Chance to win, ", no, f"% to lose. Result: {myes}")
    with open("marry", "r") as marryF:
        for mcontent in marryF:
            if mcontent == f"{ctx.author.name}":
                await ctx.send(f"{ctx.author.name} we are already married, are you trying to cheat on me? selphyNANI")
            elif myes == 'yes':
                with open("marry", "w+") as marryF:
                    marryF.write(f"{ctx.author.name}")
                    await ctx.send(f"YES I WILL selphyPog {ctx.author.name}")
            elif myes == 'no':
                with open("marry", "r") as marryF:
                    for mcontent in marryF:
                        mpass = [f"No, never selphyPout @{ctx.author.name}",
                                 f"Not even in your dreams selphyRage {ctx.author.name}",
                                 f"Not like this selphyPout {ctx.author.name}",
                                 f"Get a little more creative selphyIQ {ctx.author.name}"]
                        manswer = random.choice(mpass) + f" (i am still married to {mcontent})"
                        await ctx.send(manswer)


@bot.command(name='divorce', help='unmarry the bot')
async def divorce(ctx):
    with open("marry", "r") as marryF:
        for mcontent in marryF:
            if mcontent == f"{ctx.author.name}":
                with open("marry", "w+") as marryF:
                    marryF.write(f"noone")
                    await ctx.send(
                        f"WHAT? YOU CANT JUST UN-MARRY ME selphyNANI ({bot.user.name} is now married to noone)")
            elif mcontent != f"{ctx.author.name}":
                await ctx.send(f"We are not even married {ctx.author.name} selphyPout")


@bot.command(name='del', help='deletes a user from the serD.json file (Sachsen-only)')
@commands.has_role('Sachsen')
async def delete(ctx, name):
    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    for item in entry:
        if item['name'] == name:
            entry.remove(item)
            await ctx.send(f'''User "{name}" with id {item['id']} sucessfully deleted.''')
            break
    else:
        await ctx.send(f'No user called "{name}" found to delete.')
    with open("serD.json", "w") as f:
        o = json.dumps(ser, indent=2)
        f.write(o)


@bot.command(name='flip', help="flips a given amount of credits, usage: !flip [amount]")
async def flip(ctx, betAmount):
    balance = 5000  # Default balance for newly added users
    mf = 25  # Minimum Flip
    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    partner = None
    user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }

    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner == 't':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                # change name if user changed name
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
                        if betAmount > mf:
                            if betAmount > punkte:
                                flipStatus = 'error'
                                await ctx.send(f"You do not have enough credits! {ctx.author.name}")
                            elif betAmount <= punkte:
                                # define flip
                                coin = ('win', 'loss')
                                flip = random.choice(coin)
                                if flip == "win":
                                    flipStatus = 'won'
                                    punkte = punkte + betAmount
                                    meW = user['name'] + " won, total: " + str(punkte) + " credits!"
                                    await ctx.send((meW))
                                elif flip == "loss":
                                    flipStatus = 'lost'
                                    punkte = punkte - betAmount
                                    meL = + user['name'] + " lost, total: " + str(punkte) + " credits!"
                                    await ctx.send((meL))
                            else:
                                flipStatus = 'error'
                                await ctx.send(f"invalid syntax {ctx.author.name}")
                        elif betAmount < mf:
                            flipStatus = 'error'
                            await ctx.send(f"{mf} is the minimum flipable value {ctx.author.name}")
                        else:
                            flipStatus = 'error'
                            await ctx.send(f"Positive numbers only {ctx.author.name}")
                    elif VEerror == False:
                        if betAmount == 'all' or betAmount == 'max':
                            betAmount = punkte
                            if betAmount >= mf:
                                coin = ('win', 'loss')
                                flip = random.choice(coin)
                                if flip == "win":
                                    flipStatus = 'won'
                                    punkte = punkte + betAmount
                                    meW = f"{ctx.author.name} went all in and won, total: " + str(punkte) + " credits!"
                                    await ctx.send((meW))
                                elif flip == "loss":
                                    flipStatus = 'lost'
                                    punkte = punkte - betAmount
                                    meL = f"{ctx.author.name} went all in and lost, total: " + str(punkte) + " credits!"
                                    await ctx.send((meL))
                            elif betAmount < mf:
                                flipStatus = 'error'
                                await ctx.send(f"{mf} is the minimum flipable value {ctx.author.name}")
                        else:
                            flipStatus = 'error'
                            await ctx.send(f"invalid syntax {ctx.author.name}")
                Balance = punkte
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("serD.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
                if flipStatus == 'lost':
                    with open("jackpot", "r") as jackpotF:
                        for jackpotL in jackpotF:
                            jackpotL = int(jackpotL)
                            jackpotL = betAmount + jackpotL
                            with open("jackpot", "w+") as jackpotF2:
                                jackpotF2.write(str(jackpotL))
                break
    else:
        item = None
        with open("serD.json", "w") as f:
            entry.append(user)
            o = json.dumps(ser, indent=2)
            f.write(o)
        await ctx.send(f"Added {ctx.author.name} - {ctx.author.name} has {balance} credits.")


@bot.command(name='lotto', help='choose any amount of numbers, chance 1:21 - usage: !lotto [number1] [number2] ...')
async def lotto(ctx, *lottoG):
    balance = 5000  # Default balance for newly added users
    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    partner = None
    user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }

    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner == 't':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                # change name if user changed name
                if user['name'] != User:
                    User = user['name']
                lottoUser = User
                lottoUserFC = Balance
                useless, *lottoG = ctx.content.split(' ')
                if 'jackpot' in lottoG:
                    with open("jackpot", "r") as jackpotF:
                        for jackpotL in jackpotF:
                            jackpotL = int(jackpotL)
                            await ctx.send(f"Jackpot is at {jackpotL} credits. {ctx.author.name}")
                            lottoStatus = 'check'
                elif 'jackpot' not in lottoG:
                    with open("jackpot", "r") as jackpotF:
                        for jackpotL in jackpotF:
                            jackpotL = int(jackpotL)
                            price = 2400
                            price = price / (len(lottoG))
                            price = int(price)
                            priceLoss = len(lottoG) * 100
                            lottoN = (
                            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                            '18', '19', '20', '21')
                            lottoR = random.choice(lottoN)
                            lottoGAnzahl = (len(lottoG))
                            if lottoUserFC >= priceLoss:
                                lottoUserFC = lottoUserFC - priceLoss
                                lottoNS = "Lotto Number: " + lottoR
                                await ctx.send(lottoNS)
                                if lottoGAnzahl == 1 and lottoR in lottoG:
                                    await ctx.send(f"{ctx.author.name} won the jackpot. ({jackpotL}) selphyPog")
                                    with open((lottoUser), "w+") as lottoUserF:
                                        lottoUserFC = lottoUserFC + jackpotL
                                        lottoUserFC = str(lottoUserFC)
                                        lottoUserF.write(lottoUserFC)
                                    with open("jackpot", "w+") as jackpotF3:
                                        jackpotWrite = 0
                                        jackpotF3.write(str(jackpotWrite))
                                        lottoStatus = 'jackpot'
                                elif lottoGAnzahl != 1 and lottoR in lottoG:
                                    lottoStatus = 'won'
                                    lottoUserFC = lottoUserFC + price
                                    lottoWS = f"{ctx.author.name} won " + str(price) + " credits. Balance: " + str(
                                        lottoUserFC)
                                    await ctx.send(lottoWS)
                                else:
                                    lottoStatus = 'lost'
                                    lottoLS = f"{ctx.author.name} lost " + str(priceLoss) + " credits. Balance: " + str(
                                        lottoUserFC)
                                    await ctx.send(lottoLS)
                            else:
                                lottoStatus = 'error'
                                await ctx.send("You don't have enough credits!")
                Balance = lottoUserFC
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("serD.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
                if lottoStatus == 'lost':
                    with open("jackpot", "r") as jackpotF:
                        for jackpotL in jackpotF:
                            jackpotL = int(jackpotL)
                            jackpotL = priceLoss + jackpotL
                            with open("jackpot", "w+") as jackpotF2:
                                jackpotF2.write(str(jackpotL))
                break
    else:
        item = None
        with open("serD.json", "w") as f:
            entry.append(user)
            o = json.dumps(ser, indent=2)
            f.write(o)
        await ctx.send(f"Added {ctx.author.name} - {ctx.author.name} has {balance} credits.")


@bot.command(name='pomf', help="even the bot doesn't know what this does")
async def pomf(ctx):
    liste = random.choice([greetAnswer, greetWAnswer, husoAnswer, ripAnswer])
    listeSmol = random.choice(liste)
    listeMessage = listeSmol + f" {ctx.author.name} selphyHae"
    await ctx.send(listeMessage)


@bot.command(name='credits', help="shows the amount of credits you have")
async def credits(ctx):
    balance = 5000  # Default balance for newly added users
    pityC = 300  # Amount of Pity Credits
    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    partner = None
    user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }

    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner == 't':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                # change name if user changed name
                if user['name'] != User:
                    User = user['name']
                if Balance < 100:
                    cchoices = ['yes'] * 20 + ['no'] * 80
                    cyes = random.choice(cchoices)
                    if cyes == 'yes':
                        Balance = Balance + 300
                        await ctx.send(
                            f"I felt bad for @{ctx.author.name} and gave him {pityC} credits. selphyPray {ctx.author.name} now has {Balance} credits.")
                    else:
                        await ctx.send(f"{user['name']} has {Balance} credits")
                else:
                    await ctx.send(f"@{user['name']} has {Balance} credits")
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("serD.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
                break
    else:
        item = None
        with open("serD.json", "w") as f:
            entry.append(user)
            o = json.dumps(ser, indent=2)
            f.write(o)
        await ctx.send(f"Added {ctx.author.name} - {ctx.author.name} has {balance} credits.")


# @bot.command(name='tts', help='testing purposes only. (Sachsen-only)')
# @commands.has_role('Sachsen')
# async def tts(ctx, *speech):
#     if not speech:
#         await ctx.send(f"Atleast one word to read required! {ctx.author.name}")
#     else:
#         speech = '_'.join(speech)
#         speech = speech.replace("'", "")
#         speech = speech.replace('"', '')
#         speech = speech.replace("(", "")
#         speech = speech.replace(")", "")
#         speech = speech.replace("-", "")
#         speech = speech.replace("&", "")
#         speech = speech.replace("/", "")
#         speech = speech.replace(""""\
#                                 """, "")
#         speech = speech.replace("!", "")
#         speech = speech.replace("?", "")
#         speech = speech.replace("$", "")
#         speech = speech.replace("§", "")
#         speech = speech.replace(",", "")
#         speech = speech.replace("%", "")
#         speech = speech.replace("{", "")
#         speech = speech.replace("}", "")
#         speech = 'espeak ' + (speech)
#         os.system(speech)


@bot.command(name='dice', help='roll the dice, usage: !dice [number of sides]')
async def dice(ctx, sides):
    balance = 5000  # Default balance for newly added users
    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    partner = None
    user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }

    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner == 't':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                # change name if user changed name
                if user['name'] != User:
                    User = user['name']
                userCurrency = Balance
                if RepresentsInt(sides):
                    sides = int(sides)
                    if sides < 1:
                        await ctx.send(f'{ctx.author.name} invalid number of sides')
                    else:
                        dice = str(random.choice(range(1, sides + 1)))
                        if sides > 1 and int(dice) == int(sides):
                            reward = 50 * int(sides)  # amount of credits earned per side
                            userCurrency = int(userCurrency) + reward
                            diceMessage = f"{ctx.author.name} " + str(
                                dice) + f" is the same number as the number of sides, congrats take these {reward} credits. selphyPray"
                            await ctx.send(diceMessage)
                        elif dice != sides:
                            diceMessage = f"{ctx.author.name} Your number is: " + dice
                            await ctx.send(diceMessage)
                else:
                    await ctx.send("invalid input")
                Balance = userCurrency
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("serD.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
                break
    else:
        item = None
        with open("serD.json", "w") as f:
            entry.append(user)
            o = json.dumps(ser, indent=2)
            f.write(o)
        await ctx.send(f"Added {ctx.author.name} - {ctx.author.name} has {balance} credits.")


@bot.command(name='calc',
             help="given two numbers and an operator, it calculates the result. Possible Operators: '+' '-' ':' '*'")
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
        # useless, eventstatus = ctx.content.split(' ')
        eventFile = open("Event", "r")
        eventLines = eventFile.readlines()
        for eventLine in eventLines:
            eventSF = str(eventLine)
        if eventstatus == 'open' and eventSF == 'open':
            await ctx.send("Event is already opened.")
            actEv = "Event is: " + eventstatus
            activity = discord.Game(actEv)
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        elif eventstatus == 'open' and eventSF != 'open':
            eventFile.close()
            eventCFile = open("Event", "w+")
            eventCFile.write(eventstatus)
            eventSs = "Event is now " + eventstatus + ". You can now enter !get to recieve 100 credits each time."
            await ctx.send(eventSs)
            actEv = "Event is: " + eventstatus
            activity = discord.Game(actEv)
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        elif eventstatus == 'close' and eventSF == 'close':
            await ctx.send(" Event is already closed")
            eventstatus = 'closed'
            actEv = "Event is: " + eventstatus
            activity = discord.Game(actEv)
            await bot.change_presence(status=discord.Status.idle, activity=activity)
        elif eventstatus == 'close' and eventSF != 'close':
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
    balance = 5000  # Default balance for newly added users
    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    partner = None
    user = {'name': ctx.author.name.lower(),
            'id': ctx.author.id,
            'balance': balance,
            'partner': partner
            }

    with open("serD.json", "r") as f:
        ser = json.load(f)
        entry = ser['user']

    for item in entry:
        if item['id'] == user['id']:
            user['balance'] = item['balance']

    for item in entry:
        if item['id'] == user['id']:
            if partner == 't':
                entry.remove(item)
            else:
                Partner = item['partner']
                User = item['name']
                ID = item['id']
                Balance = item['balance']
                # change name if user changed name
                if user['name'] != User:
                    User = user['name']
                eventstatusF = open("Event", "r")
                eventstatusLines = eventstatusF.readlines()
                for eventstatusLine in eventstatusLines:
                    eventstatusS = str(eventstatusLine)
                l = user['name']
                eventRC = Balance
                if eventstatusS == 'open':
                    if eventstatusS == 'close':
                        await ctx.send("Event currently not running.")
                    if eventstatusS == 'open':
                        eventRC = eventRC + 100
                        eventRsS = l + " has participated. Balance: " + str(eventRC)
                        await ctx.send(eventRsS)
                    else:
                        await ctx.send("Event currently not running.")
                else:
                    await ctx.send(f"Not able to participate, event closed ({eventstatusS})")
                Balance = eventRC
                item['name'] = str(User)
                item['id'] = int(ID)
                item['balance'] = int(Balance)
                item['partner'] = Partner
                with open("serD.json", "w") as f:
                    o = json.dumps(ser, indent=2)
                    f.write(o)
                break
    else:
        item = None
        with open("serD.json", "w") as f:
            entry.append(user)
            o = json.dumps(ser, indent=2)
            f.write(o)
        await ctx.send(f"Added {ctx.author.name} - {ctx.author.name} has {balance} credits.")


bot.run(TOKEN)
