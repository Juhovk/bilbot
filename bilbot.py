import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix='!')

@Bot.command()
async def ping(ctx):
	await ctx.send('pong')

@Bot.command()
async def bilbo(ctx):
	await ctx.send('https://pbs.twimg.com/profile_images/2103522855/Scary_Bilbo_400x400.jpg')

token = ""
with open("token.txt") as file:
	token = file.read()

Bot.run(token)
