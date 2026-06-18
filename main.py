
import discord
from discord.ext import commands
import os

# تعريف البوت
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# لما البوت يشتغل
@bot.event
async def on_ready():
    print(f'✅ البوت شغال كـ {bot.user}')
    await bot.change_presence(activity=discord.Game(name="السلام عليكم"))

# أمر ping
@bot.command()
async def ping(ctx):
    await ctx.send(f'🏓 بونق! الزمن: {round(bot.latency * 1000)}ms')

# رد على السلام
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'السلام عليكم':
        await message.channel.send('وعليكم السلام ورحمة الله وبركاته 🌹')
    
    await bot.process_commands(message)

# تشغيل البوت (يقرأ التوكن من المتغيرات)
bot.run(os.getenv('TOKEN'))
