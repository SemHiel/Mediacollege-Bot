from os import stat
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

# On_Ready event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('MediaCollege'))
    print('[!] Bot staat aan')

# Server Join Event
@client.event
async def on_member_join(member):
    print(f'{member} is het nieuwste lid van de Server!')

# Server Leave Event
@client.event
async def on_member_remove(member):
    print(f'{member} heeft de server verlaten!')

# GeboorteDatum Input/output
@client.command()
async def verjaardag(ctx, arg):
    channel = client.get_channel(942704940902649906)
    await ctx.send('Je hebt je verjaardag toegevoegd!', delete_after=3)
    await channel.send(f"{ctx.author.mention} zijn verjaardag is **{arg}**")
    await ctx.message.delete()



client.run('OTQyNzAyODA3MTEzNDIwODEw.YgoWZw.x3aWuQnpNyshPZFHOb8ZF5VdAVo')