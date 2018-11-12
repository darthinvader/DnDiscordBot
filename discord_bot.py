import discord
from discord.ext import commands
from dice_rolling import wrapper_dice
TOKEN = 'NTExMjIxOTA3NzgyMTA3MTM3.DsnwaA.PJRnQv_ITDKTSaFVYomio3gEUrI'

client = commands.Bot(command_prefix='!')


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

client.run(TOKEN)
