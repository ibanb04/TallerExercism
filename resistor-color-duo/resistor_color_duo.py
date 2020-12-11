def value(colors):
    colorCodes = {
        'black': '0',
        'brown': '1',
        'red': '2',
        'orange': '3',
        'yellow': '4',
        'green': '5',
        'blue': '6',
        'violet': '7',
        'grey': '8',
        'white': '9'
    }

    res = ''
    for color in colors:
        if len(res) < 2:
            res += colorCodes[color]

    return int(res)