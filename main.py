import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(
    command_prefix=settings['prefix'])  #Определение префикса из config.py


@bot.event  #Отладка, что бот запущен (в консоли)
async def on_ready():
	print("Готов к работе")


@bot.command()  #Регистрация игрока
async def Начать(ctx):
	guild = ctx.message.guild
	category = guild.get_channel(920739979972448307)
	author = ctx.message.author.name + '-уровень-' + settings['level']
	await category.create_text_channel(author)
	await ctx.send(f'Чтож, начнем!')


@bot.command()  #Тест приветствия
async def Привет(ctx):
	author = ctx.message.author
	await ctx.send(f'Привет, {author.mention}, Бог-Барсук рад встрече!')


bot.run(settings['token'])  #Запуск бота, финальная строка
