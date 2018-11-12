from random import randint

def dice_parser(text):
    """
    A basic dice parser that takes a string of the type:
    x_1 D y_1 + x_2 D y_2 + .... x_n D y_n
    and converts it into two lists of dice amount and dice type
    Parameters:
    -----
        text: string
            contains the text we want to parse
    Returns:
    -----
        dice_amount: list of ints
            the amount of dice being rolled
        dice_types: list of ints
            the types of dices being rolled

    """

    text = text.upper()
    text_list = text.replace(' ', '').split('+')

    dice_amount = list()
    dice_types = list()

    for t in text_list:
        splitter = t.split('D')
        if len(splitter) < 1 or len(splitter) > 2:
            return 0, 0
        try:
            x1 = int(splitter[0])
        except ValueError:
            return 0, 0
        try:
            x2 = int(splitter[1])
        except ValueError:
            return 0, 0

        dice_amount.append(x1)
        dice_types.append(x2)

    return dice_amount, dice_types


def throw_dice(dice_amount, dice_types):
    rolls = list()
    for (d1, d2) in zip(dice_amount, dice_types):

        current_dice_roll = tuple()
        for k in range(0, d1):
            current_dice_roll = current_dice_roll + (randint(1, d2),)
        rolls.append(current_dice_roll)
    return rolls


def dice_printer(dice_amount, dice_types, rolls):
    stringer = ''
    total_amount = 0
    for da,dt,dr in zip(dice_amount, dice_types, rolls):
        stringer += "For " + str(da) + "D" + str(dt) + " you rolled "
        amount = 0
        for roll in dr:
            stringer += str(roll) + ", "
            amount += roll
            total_amount += roll
        stringer += "total for these dice is " + str(amount) + ".\n"
    stringer += "You rolled in total " + str(total_amount) + "."
    return stringer

dice_amount, dice_types = dice_parser('4d12 + 3d20 + 1d4 + 2d6 + 5d8 + 10d10')
print(dice_amount, dice_types)
rolls = throw_dice(dice_amount, dice_types)
print(rolls)

string = dice_printer(dice_amount, dice_types, rolls)
print(string)
