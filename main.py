import discord
import random
from discord.ext import commands
from keep_alive import keep_alive
import os
from mcstatus import MinecraftServer
import youtube_dl
import json

client = commands.Bot(command_prefix = '!j ')

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="7 Servers!"))
    print('SpaceManBot is ready for action!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=["mc"])
async def member_count(ctx):

    a=ctx.guild.member_count
    b=discord.Embed(title=f"Total Members in {ctx.guild.name} (Including Bots)",description=a,color=discord.Color((0xffff00)))
    await ctx.send(embed=b)

@client.command(aliases=['8ball', 'eightball','8 ball', '8-ball', 'eight ball', 'eight-ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def website(ctx):
  embed=discord.Embed(title="SMP Website", description="http://smpjaxwebsite.ml/", color=8791295)
  await ctx.send(embed=embed)

# Upload your image/gif to repl.it, then put the file name where 'mp4.gif' is.
@client.command()
async def nobodycares(ctx):
  await ctx.send(file=discord.File('mp4.gif'))

@client.command()
async def duck(ctx):
  await ctx.send(file=discord.File('unknown (1).gif'))

@client.command()
async def die(ctx):
  await ctx.send(file=discord.File('unknown (2).gif'))

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
 
@client.command(aliases=['help-1', 'help 1'])
async def help(ctx):
    embed=discord.Embed(title="Help", description="Here is the 1st page of commands. This page will be filled with commands for the SMP. There will be other help pages so you can also do j! help2\n\n!j help ~ Shows this help page\n!j credits ~ Shows the credits\n!j status ~ displays the ping and players of SMPJax\n!j latency ~ displays the current ping of SMPJax\n!j website ~ displays the link to the SMPJax website", color=8791295)
    embed.add_field(name="Other", value="Server IP: smpjax.tk", inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['help 2', 'help-2'])
async def help2(ctx):
    embed=discord.Embed(title="Help 2", description="Here is the 2nd page of commands. This page will be filled with fun commands.\n\n!j 8 ball ~ Ask a question and the bot will answer!\n!j echo ~ Say something and the bot will repeat you!\n!j ping ~ Displays the bots ping\n!j slap ~ Slap someone!\n!j kill ~ Stab someone!\n!j coinflip ~ Flips a coin and tells you the outcome\n!j nobodycares ~ Express your true feelings", color=8791295)
    await ctx.send(embed=embed)

@client.command()
async def help3(ctx):
    embed=discord.Embed(title="Help 3", description="Here is the 3rd page of commands. This will be filled is misc commands.\n\n!j version ~ Shows the version of SpaceManBot\n!j news ~ News\n!j radio ~ Your local radio news.\n!j mc ~ Displays the member count\n!j suggest ~ Suggest something\n!j duck ~ Duck dance\n!j die ~ Dies", color=8791295)
    await ctx.send(embed=embed)

@client.command()
async def help4(ctx):
    embed=discord.Embed(title="Help 4", description="Here is the 4th page of commands. This will be filled is economy commands.\n\n!j rob ~ Rob someone\n!j bet ~ Bet coins\n!j work ~ Earn some coins\n!j beg ~ Beg for some coins\n!j send ~ Send someone coins\n!j shop ~ Look at the shop\n!j buy ~ Buy an item\n!j sell ~ Sell an item\n!j dep ~ Deposit coins\n!j with ~ Withdraw coins", color=8791295)
    await ctx.send(embed=embed)

@client.command()
async def help5(ctx):
    embed=discord.Embed(title="Help 5", description="Here is the 5th page of commands. This will be filled is music commands. NOTE: No songs over 10 minutes\n\n!j play ~ Play a song\n!j leave ~ Leaves the vc\n!j pause ~ Pause the song\n!j resume ~ Resumes the currently paused song\n!j stop ~ Stops the song", color=8791295)
    await ctx.send(embed=embed)

@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

@client.command()
async def kill(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got stabbed for {}'.format(slapped, reason))

@client.command()
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

@client.command()
async def version(ctx):
    embed=discord.Embed(title="Version", description="**[SpaceManBot is on version 1.9.4]**\nThis bot is a work in progress", color=8791295)
    await ctx.send(embed=embed)

@client.command()
async def news(ctx):
    choices = ["The radio station has shutdown for some unknown reason.", "Gamorad is silencing news reporters. This is an outrage", "Mavlent is dead! Hooray!", "While 1 of the Aractian cannons has been destroyed, Aractus forces have managed to push back Imperials and completed 9 of the 10 cannons. This makes 10 completed cannons, each capable of destroying cities. Gamorad will need to immediately mobilize his 'top forces' to quickly take care of the problem.", "Aractus Leaders are ordering the construction of several large cannons. Only one of these cannons currently exists, the Aractian Thunderbolt. These cannons, once completed, will be able to level small towns. They are planning to use them in the war to destroy Imperial forces and controlled territories.", "Gamorad has promised to find all of these cannons and destroy them before they are completed.", "Gamorad has mobilized police forces immediately in response to a Violent Riot in Terra. The Rebels managed to burn down a building and cause 23 deaths. Gamorad has instructed the construction of a memorial on the beach to honor these 23 people.", "Random disapperances of people are rapidly growing.", "A new resturant opened downtown this week.", "[redacted]",]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command()
async def radio(ctx):
    embed=discord.Embed(title="Radio", description="You tune into your local radio station...\n\n... Pzzzt \n Line failed to ping. [Error 102: Signal Failed To Connect.] \n You are overwhelmed with static. You shut off your radio and smash it to the ground", color=8791295)
    await ctx.send(embed=embed)

# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
server = MinecraftServer.lookup("smpjax.tk:25565")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
@client.command()
async def status(ctx):
  status = server.status()
  await ctx.send("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))
  usersConnected = [ user['name'] for user in status.raw['players']['sample'] ]
  await ctx.send(usersConnected)

# 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
# It is included in a 'status' call, but is exposed separate if you do not require the additional info.
@client.command()
async def latency(ctx):
  latency = server.ping()
  await ctx.send("The server replied in {0} ms".format(latency))
  
@client.command()
async def query(ctx):
  query = server.query()
  await ctx.send("The server has the following players online: {0}".format(", ".join(query.players.names)))

emoji = '\N{THUMBS UP SIGN}'
emoji2 = '\N{THUMBS DOWN SIGN}'

@client.command()
async def suggest(ctx, command, *, description):
    ': Suggest a command. Provide the Suggestion name and description'
    embed = discord.Embed(title='Suggestion', description=f'Suggested by: {ctx.author.mention}\nSuggestion Name: {command}', color=discord.Color.green())
    embed.add_field(name='Description', value=description)
    channel = ctx.guild.get_channel(751194158919843870)
    message = await channel.send(embed=embed)
    await message.add_reaction(emoji)
    await message.add_reaction(emoji2)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")

def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel=ctx.message.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

mainshop = [{"name":"Watch","price":100,"description":"Tells the time"},{"name":"Mining_Computer","price":1000,"description":"Get more Jackcoins when mining!"},{"name":"*Anime*","price":500,"description":"Your normal collection of *anime*."},{"name":"Jackcoin_Stock","price":500,"description":"Invest in Jackcoin!"}]

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = '**Still on cooldown**, please try again in {:.2f}s'.format(error.retry_after)
    await ctx.send(msg)

@client.command(aliases = ["bal"])
async def balance(ctx):
  await open_account(ctx.author)
  user = ctx.author
  users = await get_bank_data()

  wallet_amt = users[str(user.id)]["wallet"]
  bank_amt = users[str(user.id)]["bank"]

  em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.red())
  em.add_field(name = "Wallet balance",value = wallet_amt)
  em.add_field(name = "Bank balance",value = bank_amt)
  await ctx.send(embed = em)

@client.command()
@commands.cooldown(1,30,commands.BucketType.user)
async def beg(ctx):
  await open_account(ctx.author)

  users = await get_bank_data()

  user = ctx.author

  earnings = random.randrange(20)


  await ctx.send(f"Someone gave you {earnings} Jackcoins.")


  users[str(user.id)]["wallet"] += earnings

  with open("mainbank.json", "w") as f:
    json.dump(users,f)

@client.command()
@commands.cooldown(1,3600,commands.BucketType.user)
async def work(ctx):
  await open_account(ctx.author)

  users = await get_bank_data()

  user = ctx.author

  earnings = random.randrange(500)


  await ctx.send(f"You pulled an all-nighter to mine Jackcoin, your mining paid you {earnings} coins for the hard work.")


  users[str(user.id)]["wallet"] += earnings

  with open("mainbank.json", "w") as f:
    json.dump(users,f)

@client.command(aliases = ["with"])
async def withdraw(ctx,amount = None):
  await open_account(ctx.author)

  if amount == None:
    await ctx.send("Please enter the amount")
    return
  
  bal = await update_bank(ctx.author)

  amount = int(amount) 
  if amount>bal[1]:
    await ctx.send("Insufficient Funds")
    return
  if amount<0: 
    await ctx.send("Amount must be positive")
    return
    
  await update_bank(ctx.author,amount)
  await update_bank(ctx.author,-1*amount, "bank")

  await ctx.send(f"You withdrew {amount} coins")

@client.command(aliases = ["dep"])
async def deposit(ctx,amount = None):
  await open_account(ctx.author)

  if amount == None:
    await ctx.send("Please enter the amount")
    return
  
  bal = await update_bank(ctx.author)

  amount = int(amount) 
  if amount>bal[0]:
    await ctx.send("Insufficient Funds")
    return
  if amount<0: 
    await ctx.send("Amount must be positive")
    return
    
  await update_bank(ctx.author,-1*amount)
  await update_bank(ctx.author,amount, "bank")

  await ctx.send(f"You deposited {amount} coins")


@client.command(aliases = ["share","give"])
async def send(ctx,member:discord.Member,amount = None):
  await open_account(ctx.author)
  await open_account(member)

  if amount == None:
    await ctx.send("Please enter the amount")
    return
  
  bal = await update_bank(ctx.author)
  if amount == "all":
    amount = bal[0]

  amount = int(amount) 
  if amount>bal[1]:
    await ctx.send("Insufficient Funds")
    return
  if amount<0: 
    await ctx.send("Amount must be positive")
    return
    
  await update_bank(ctx.author,-1*amount,"bank")
  await update_bank(member,amount, "bank")

  await ctx.send(f"You gave {amount} coins")

@client.command(aliases = ["steal"])
@commands.cooldown(1,120,commands.BucketType.user)
async def rob(ctx,member:discord.Member):
  await open_account(ctx.author)
  await open_account(member)
  
  bal = await update_bank(member)

  if bal[0]<100:
    await ctx.send("It's not worth it to rob this person!")
    return
    
  earnings = random.randrange(0, bal[0])

  await update_bank(ctx.author,earnings)
  await update_bank(member,-1*earnings)

  await ctx.send(f"You stole {earnings} coins!")


@client.command(aliases = ["bet"])
async def slots(ctx,amount = None):
  await open_account(ctx.author)

  if amount == None:
    await ctx.send("Please enter the amount")
    return
  
  bal = await update_bank(ctx.author)

  amount = int(amount) 
  if amount>bal[0]:
    await ctx.send("Insufficient Funds")
    return
  if amount<0: 
    await ctx.send("Amount must be positive")
    return
    
  final = []
  for i in range(3):
    a = random.choice(["X","O","Q"])

    final.append(a)

  await ctx.send(str(final))

  if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
    await update_bank(ctx.author,2*amount)
    await ctx.send("You won!")
  else:
    await update_bank(ctx.author,-1*amount)
    await ctx.send("You lost")
  

@client.command()
async def shop(ctx):
  em = discord.Embed(title = "Shop")

  for item in mainshop:
    name = item["name"]
    price = item["price"]
    description = item["description"]
    em.add_field(name = name, value = f"${price} | {description}")

  await ctx.send(embed = em)



@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")



@client.command(aliases = ["inv","inventory"])
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.send(embed = em)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

async def open_account(user):
  
  users = await get_bank_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 0
    users[str(user.id)]["bank"] = 0

  with open("mainbank.json", "w") as f:
    json.dump(users,f)
  return True



async def get_bank_data():
  with open("mainbank.json", "r") as f:
    users = json.load(f)
  
  return users


async def update_bank(user,change = 0,mode = "wallet"):
  users = await get_bank_data()

  users[str(user.id)][mode] +=change

  with open("mainbank.json", "w") as f:
    json.dump(users,f)


  bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
  return bal

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)



keep_alive()
client.run(os.getenv('TOKEN'))
