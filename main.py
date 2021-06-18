import discord
from discord.ext import commands, tasks
import os, asyncio
from random import choice

#status         =854593444072390657
#commands       =854593471444156427
#commands-error =854979341309181952
#warn-log       =855312734874107925

orange=0xe68a89

presence= [
    discord.Activity(type=discord.ActivityType.playing, name=("Develop by Luminette")),
    discord.Activity(type=discord.ActivityType.playing, name=("prefix: 'minet, '")),
    discord.Activity(type=discord.ActivityType.playing, name=("✨new prefix: '+ '✨")),
    discord.Activity(type=discord.ActivityType.watching, name=("Mayonese ❤️"))
]

PREFIX = [
  "Minet, ", 
  "Minet,", 
  "minet, ", 
  "minet,", 
  "+ ", 
  "+"
  ]

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, help_command=None, intents=intents)

bot.remove_command('help') 

@bot.command()
async def help(ctx):
  pass

@bot.command()
async def invite (ctx):
  embed=discord.Embed(title="__Invite me to your server!__", description="[Click here](https://discord.com/api/oauth2/authorize?client_id=831059612916383764&permissions=8&scope=bot)\n*as Administrator*\n", colour=orange)
  await ctx.send(embed=embed)

@bot.event
async def on_ready():
  channel = bot.get_channel(854593444072390657)
  await channel.send('Rebooting')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("booting...")))
  await asyncio.sleep(5)
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=("development")))
  print('Luminette is online.')
  
@bot.event
async def on_command_error(ctx, error):
  pass

@bot.event
async def on_member_join(member):
  pass

@bot.event
async def on_message(message):
    if message.author == bot.user:
      return
    await bot.process_commands(message)

@bot.event
async def on_command(ctx):
  channel = bot.get_channel(854593471444156427)
  embed = discord.Embed(title=f"{ctx.author.name} used a command!", description=f"{ctx.message.content}",colour=discord.Color.orange())
  await channel.send('––––––––––––––––––––––––––––––––––––––––––––––––',embed=embed)
@bot.event
async def on_command_completion(ctx):
  channel = bot.get_channel(854593471444156427)
  embed = discord.Embed(title=f"Completed {ctx.author.name}'s command!", description=f"{ctx.message.content}",colour=discord.Color.gold())
  await channel.send(embed=embed)

@bot.command(aliases=['echo'])
async def say(ctx, *, msg):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def servers(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    await ctx.send("__**Luminette's active servers:**__")
    activeservers = bot.guilds
    for guild in activeservers:
      await ctx.send(f'Server name:`{guild.name}`,\nServer ID:`{guild.id}`,\nServer Owner:`{guild.owner}`\nOwner ID :`{guild.owner.id}`\nMembers: `{guild.member_count}`')
      await ctx.send('––––––––––––––––––––––––––––––––––––––––––––––––')

@tasks.loop(minutes=5)
async def presence_change():
  await asyncio.sleep(10)
  await bot.change_presence(activity=choice(presence))
  channel = bot.get_channel(854593444072390657)
  await channel.send('Changing Presence')
  print("Changing Presence")
@presence_change.before_loop
async def presence_change_before():
  await bot.wait_until_ready()
@bot.command()
async def pstart(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.start()
    await ctx.send("Auto presence-changing started.")
  else:
    await ctx.send("You are not allowed to use this command!")
@bot.command()
async def pstop(ctx):
  if ctx.author.id == 809244553768861706 or ctx.author.id == 743042741461712897:
    presence_change.cancel()
    await ctx.send("Auto presence-changing has stopped.")
  else:
    await ctx.send("You are not allowed to use this command!")

extensions = [ 
  'cogs.miscellaneous', 
  'cogs.mod', 
  'cogs.reminder', 
  'cogs.voice', 
  'cogs.info'  
]

if __name__ == '__main__':
  for ext in extensions:
    bot.load_extension(ext)
bot.run(os.getenv('TOKEN'))
