def dice_parser(text):
    """
    A basic dice parser that takes a string of the type:
    x_1 D y_1 + x_2 D y_2 + .... x_n D y_n
    and converts it into two lists of dice ammount and dice type
    Parameters:
    -----
        text: string
            contains the text we want to parse
    Returns:
    -----
        k:

    """

    text = text.upper()
    text_list = text.replace(' ', '').split('+')

    dice_ammount = list()
    dice_type = list()

    for t in text_list:
        splitter = t.split('D')
        if len(splitter) <1 or len(splitter)>2:
            return 0,0
        try:
            x1 = int(splitter[0])
        except ValueError:
            return 0, 0
        try:
            x2 = int(splitter[1])
        except ValueError:
            return 0, 0

        dice_ammount.append(x1)
        dice_type.append(x2)

    return dice_ammount, dice_type