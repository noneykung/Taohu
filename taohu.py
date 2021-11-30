import discord
import requests
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix='/',help_command=None)
slash = SlashCommand(bot, sync_commands=True)

token = ('OTAyMTA0MzM3ODEwMDY3NDU5.YXZkIg.8REqslub1wnvCR3X8TEQF_LJhe8')

guild_id = [698129392257466380]

@bot.event
async def on_ready():
    print('\nLogged in as ' + bot.user.name +" (" + str(bot.user.id) + ")\n------")
    #await setBotName(bot,'Candle_TS')
    await bot.change_presence(activity=discord.Game(name='อยู่ห่างไกลมันเหงาใจ อยากชื่นใจต้องอยู่ใกล้กัน~'))

@slash.slash(
    name="Ping", 
    description="Simple Ping Pong!", 
    guild_ids = guild_id
)
async def ping(ctx):
    await ctx.reply("Pong!")

@slash.slash(
    name = 'announce',
    description = 'ประกาศข่าวสำคัญจร้า',
    guild_ids = guild_id,
    
)
async def announce(ctx):
    ...

bot.run(token)