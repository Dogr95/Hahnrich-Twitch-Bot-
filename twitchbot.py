import os # for importing env vars for the bot to use
import random
from twitchio.ext import commands
import time

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

channelid=[os.environ['CHANNELID']]


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me is watching!")

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
    #shortened channelsend
    greet = ctx.content.lower()
    
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return
    await bot.handle_commands(ctx)
    #await ctx.channel.send(ctx.content) | annoying repeating messages
    if "hello" in greet or "hi" in greet or "tag" in greet or "hallo" in greet or "selphyHi" in greet or "servus" in greet or "grüß gott" in greet:
        await ctx.channel.send(f"Hi, @{ctx.author.name}! HeyGuys")
    if "wie gehts" in greet:
        await ctx.channel.send(f"Ganz okay... hoffentlich bald Feierabend NotLikeThis @{ctx.author.name}")
    if "und dir?" in greet or "und selbst?" in greet or "und selber?" in greet:
        await ctx.channel.send(f"pah fragt mich nichtmal DansGame")
        

@bot.event
async def event_command_error(ctx, error):
    await ctx. channel.send(f'Error running command: {error} @{ctx.message.author.name}')

@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed')
    print(ctx.author.id, "ran test")
    print((os.environ['CHANNEL']))

@bot.command(name='clip')
async def clip(ctx):
    await bot.create_clip((os.environ['TMI_TOKEN']), (os.environ['CHANNEL']))

@bot.command(name='listusers')
async def listusers(ctx):
    #Chatters = await bot.get_chatters((os.environ['CHANNEL']))
    #print(Chatters)
    await ctx.channel.send(await bot.get_chatters((os.environ['CHANNEL'])))

@bot.command(name='timeout')
async def timeout(ctx, user):
    if str(ctx.author.is_mod)=="True":
        useless, cU, cT, cR = ctx.content.split(' ')
        await ctx.timeout(str(cU), int(cT), str(cR))
        mTs = "Set " + str(cU) + " for " + str(cT) + " seconds in timeout. Reason: " + str(cR)
        await ctx.channel.send((mTs))
    else:
        await ctx.channel.send("Netter Versuch, der Command ist nur für Mods :)")

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
        await ctx.channel.send(f"File for {ctx.author.name} created.")
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
                await ctx.channel.send(f"invalid syntax @{ctx.author.name}")
                VEerror = False
            finally:
                if VEerror:
                    if betAmount >= 0 :
                        if betAmount > punkte:
                            await ctx.channel.send("You do not have enough credits!")
                        elif betAmount <=punkte:
                            #define flip
                            coin = ('win', 'loss')
                            flip = random.choice(coin)
                            if flip=="win":
                                punkte=punkte+betAmount
                                meW = l + " won, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meW))
                            elif flip=="loss":
                                punkte=punkte-betAmount
                                meL = l + " lost, total: " + str(punkte) + " credits!"
                                await ctx.channel.send((meL))
                        else:
                            await ctx.channel.send(f"invalid syntax @{ctx.author.name}")
                    else:
                        await ctx.channel.send(f"Positive numbers only @{ctx.author.name}")
            
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
        await ctx.channel.send(f"File for {ctx.author.name} created.")
    finally:
        creditsCommandCheck = open((creditsCommand), "r")
        creditsLines = creditsCommandCheck.readlines()
        for creditsLine in creditsLines:
            creditsCheckInt = int(creditsLine)
            await ctx.channel.send(f"{ctx.author.name} has {creditsCheckInt} credits.")
    if creditsCheckInt < 100:
        await ctx.channel.send(f"i felt bad for @{ctx.author.name} and gave him 300 credits.")
        creditsCheckInt = creditsCheckInt+300
        f = open((creditsCommand), "w")
        f.write(str(creditsCheckInt))
        f.close()
        await ctx.channel.send(f"{ctx.author.name} now has {creditsCheckInt} credits.")
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
        await ctx.channel.send(f"File for {ctx.author.name} created.")
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
                    await ctx.channel.send(f"Receiving user not found or invalid amount")
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
                            await ctx.channel.send (f"@{ctx.author.name} sent {giftAmount} credits to {giftR}.")
                    else:
                        break
            elif giftAmount < 0:
                ctx.channel.send("invalid gift amount")

@bot.command(name='commands')
async def commands(ctx):
    await ctx.channel.send("!flip [betAmount]")
    await ctx.channel.send("!gift [user] [giftAmount]")
    await ctx.channel.send("!credits")
    await ctx.channel.send("(mod-only) !timeout [user] [time] [reason]")
    await ctx.channel.send("!listusers")
    await ctx.channel.send("(broken) !clip")
    await ctx.channel.send("!test")

#async def franzosen(ctx):
#    if "bonjour" in frG:  
#        await ctx.channel.send(f"huso, keine franzsosen in diesem stream DansGame")
#        franzosen = str(ctx.author.name)
#        await ctx.timeout((franzosen), int(60), str("Keine Franzosen")) #Timeout 60 Sekunden
    
min_call_freq = 5
used = {}

def call_command(command):
    print('Calling command %s.' % command)
    # do whatever

def cooldown(command):
    print('You have used command %s in the last %u seconds.' % (command, min_call_freq))

def process_command(command):
    if (
        command not in used or
        time.time() - used[command] > min_call_freq
    ):
        used[command] = time.time()
        call_command(command)
    else:
        cooldown(command)

if __name__ == "__main__":
    bot.run()

