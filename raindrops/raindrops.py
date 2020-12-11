def convert(number):
    texto = ''
    if number % 3 == 0:
        texto += 'Pling'
    if number % 5 == 0:
        texto += 'Plang'
    if number % 7 == 0:
        texto += 'Plong'
    if texto == '':
        texto = str(number)
    return texto