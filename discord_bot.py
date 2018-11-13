import discord
from discord.ext import commands
from dice_rolling import wrapper_dice_embed
import dice_rolling as dr
TOKEN = 'NTExMjIxOTA3NzgyMTA3MTM3.DsnwaA.PJRnQv_ITDKTSaFVYomio3gEUrI'

client = commands.Bot(command_prefix='!', case_insensitive=True)
client.remove_command('help')


@client.event
async def on_ready():
    print('I\'m Ready')


@client.command()
async def roll(*dices):
    print(dices)
    dice = ''
    for d in dices:
        dice += d
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def d20():
    dice = '1d20'
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def d12():
    dice = '1d12'
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def d10():
    dice = '1d10'
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def d8():
    dice = '1d8'
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def d6():
    dice = '1d6'
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def d4():
    dice = '1d4'
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def toss_coin():
    dice = '1d2'
    embed = wrapper_dice_embed(dice)
    await client.say(embed=embed)


@client.command()
async def init():
    embed = dr.wrapper_init_embed()
    await client.say(embed=embed)


@client.command(pass_context=True)
async def help(context):
    channel = context.message.channel
    content = 'I\'m helping'
    await client.send_message(channel, content)

client.run(TOKEN)
