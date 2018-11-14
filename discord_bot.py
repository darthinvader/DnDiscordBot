import discord
from discord.ext import commands
from dice_rolling import wrapper_dice_embed
import dice_rolling as dr
import dnd_system

TOKEN = 'NTExMjIxOTA3NzgyMTA3MTM3.DsnwaA.PJRnQv_ITDKTSaFVYomio3gEUrI'

client = commands.Bot(command_prefix='!', case_insensitive=True)
client.remove_command('help')
dnd_system = dnd_system.DnDSystem()

extensions = {'dnd_system'}

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


@client.command(pass_context=True)
async def init(context):
    name = context.message.author.name
    name_id = context.message.author
    embed, dice_roll = dr.wrapper_init_embed()
    message, code = dnd_system.set_player_initiative_name(name_id, str(name), dice_roll)
    if code == 0:
        await client.say(embed=embed)
    await client.say(message)


@client.command()
async def monster_init(monster_name):
    embed, dice_roll = dr.wrapper_init_embed()
    dnd_system.set_monster_initiative(monster_name, dice_roll)
    await client.say(embed=embed)


@client.command(pass_context=True)
async def get_inits(context):
    inits = str(dnd_system.get_all_initiatives_in_order_embed())
    await client.say(inits)


@client.command(pass_context=True)
async def clear_inits(context):
    dnd_system.clear_inits()
    await client.say('Cleared Initiatives')



@client.command(pass_context=True)
async def help(context):
    channel = context.message.channel
    content = 'I\'m helping'
    await client.send_message(channel, content)


@client.command(pass_context=True)
async def join(context):
    channel = context.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def leave(context):
    for x in client.voice_clients:
        if x.server == context.message.server:
            return await x.disconnect()



"""
#music_player = None

This code is best left to a server bot where i don't get to make it download the music from the local host
@client.command(pass_context=True)
async def play(context, url):
    global music_player

    if music_player is not None:
        print('what')
        return
    server = context.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    music_player = player
    player.start()

@client.command()
async def pause():
    global music_player
    music_player.pause()

@client.command()
async def resume():
    global music_player
    music_player.resume()

@client.command()
async def stop():
    global music_player
    music_player.stop()

"""
client.run(TOKEN)
