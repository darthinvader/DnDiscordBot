import discord


def dice_roll_embed(dice_amount, dice_types, rolls):
    embed = discord.Embed(title='Dice Roll', colour=0x000080)
    total_amount = 0
    for da, dt, dr in zip(dice_amount, dice_types, rolls):
        stringer = ''
        amount = sum(dr)
        total_amount += amount
        for r in dr:
            stringer += str(r) + ','
        stringer += "total for these dice is " + str(amount)
        embed.add_field(name="For the D" + str(dt) + ' you rolled:', value=stringer, inline=False)
    embed.add_field(name='You rolled in total:', value=str(total_amount), inline=False)
    return embed


def initiative_embed(roll):
    embed = discord.Embed(title='On initiative you rolled:', colour=0x006400)
    embed.add_field(name='Initiative', value=str(roll), inline=False)
    return embed


def initiative_sorted_embed(initiatives):
    embed = discord.Embed(title='Initiative Rolls', colour =0x000000)
    for i in initiatives:
        embed.add_field(name=i[0] + ' rolled:', value=str(i[1]))
    return embed
