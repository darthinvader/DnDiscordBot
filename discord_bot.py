import discord
from discord.ext import commands
from dice_rolling import wrapper_dice, roll_initiative
TOKEN = 'NTExMjIxOTA3NzgyMTA3MTM3.DsnwaA.PJRnQv_ITDKTSaFVYomio3gEUrI'

client = commands.Bot(command_prefix='!', case_insensitive=True)
client.remove_command('help')


@client.event
async def on_ready():
    print('I\'m Ready')


@client.command(pass_context=True)
async def roll(context, *dices):
    print(dices)
    dice = ''
    for d in dices:
        dice += d
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def d20(context):
    dice = '1d20'
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def d12(context):
    dice = '1d12'
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def d10(context):
    dice = '1d10'
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def d8(context):
    dice = '1d8'
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def d6(context):
    dice = '1d6'
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def d4(context):
    dice = '1d4'
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def toss_coin(context):
    dice = '1d2'
    channel = context.message.channel
    content = wrapper_dice(dice)
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def init(context):
    channel = context.message.channel
    content, dice = roll_initiative()
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def help(context):
    channel = context.message.channel
    content = 'I\'m helping'
    await client.send_message(channel, content)


client.run(TOKEN)
