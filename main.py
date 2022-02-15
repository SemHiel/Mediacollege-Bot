from os import stat
import json
import discord
from discord.ext import commands

# Prefix Changer
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

# On_Ready event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('MediaCollege'))
    print('[!] Bot staat aan')

# Guild Join Event (Prefix)
@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
# Guild remove event (Prefix)
@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

# prefix Changer
@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open ('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

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

# Geen commando error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Geen bekend commando')

# Clear
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

# Clear Error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Vul het aantal berichten in dat je wilt verwijderen.', delete_after=5)


client.run('Token Here')