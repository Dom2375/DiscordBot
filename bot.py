# discordbot.py
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
from datetime import date
import calendar
my_date = date.today()
day = calendar.day_name[my_date.weekday()] 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.command(name='speak')
async def speak(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    channel = bot.get_channel(568214864091152388)
    if day == "Sunday":
        await channel.send('https://cdn.discordapp.com/attachments/639215690653630467/716676605203972126/sunday.mp4')
        
@bot.event
async def on_member_join(member):
    await member.send(f'Hi {member.name}, get ready for disappointment!'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'my son':
        await message.channel.send('https://cdn.discordapp.com/attachments/639215690653630467/716674135970938890/inthekitchen.mp4')

    if message.content.lower()  == "daddy":
        await message.channel.send(file=discord.File('Daddy.png'))

    if message.content.lower()  == "What day is it?":
        await message.channel.send(day)    

    if message.content.lower()  == '4':
        await message.channel.send('say the line '+ '<@364113725168418819>')

    if message.content.lower()  == 'Combat Rock':
        await message.channel.send('say the line '+ '<@364113725168418819>')    

    if message.content.lower() == 'tory':
        await message.channel.send('<@533349901371965464> ' + 'https://cdn.discordapp.com/attachments/705779705508397068/716295481491324964/4V-iD3NOL0xmcVzk.mp4')
    await bot.process_commands(message)

bot.run(TOKEN)
