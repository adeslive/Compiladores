import re
from tkinter import *
from tkinter import messagebox


# Patrones:
NUMERO = r'[0-9]+'
DECIMAL = r'Dec'
OCTAL = r'Oct'
HEXADECIMAL = r'Hex'
ROMANO = r'Rom'
BINARIO = r'Bin'
QUINARIO = r'Quint'

regexList = [DECIMAL, OCTAL, HEXADECIMAL, BINARIO, ROMANO, QUINARIO]

OPTIONREGEX = '|'.join(regexList)

REGEX = r'(' + NUMERO + r'(' + OPTIONREGEX + r'){1})+'


def convert(cadena, winConvert):
    if not re.search(REGEX, cadena):
        messagebox.showinfo(message='''Las entradas válidas deben contener un número seguido de el destino como ser:
        Bin, Quint, Oct, Dec, Hex o Rom.
        Ejemplo: 13Bin''', title='Entrada inválida')

    for match in re.findall(REGEX, cadena):
        # Por cada match se debe sacar el numero y el destino
        if re.search(NUMERO, match[0]) and re.search(OPTIONREGEX, match[0]):
            numero = re.search(NUMERO, match[0])[0]
            destino = re.search(OPTIONREGEX, match[0])[0]
            resultado = checkConversion(numero, destino)
            lblReceipt = Label(winConvert, text='Entrada: ' +
                               match[0] + ' => Conversión: ' + resultado)
            lblReceipt.pack()


def decToBase(number, base):
    parsedNumber = int(number)
    result = ''

    while parsedNumber > 0:
        mod = int(parsedNumber % base)
        if base == 16:
            mod = getHexValue(mod)
        parsedNumber = int(parsedNumber / base)
        result = str(mod) + result

    return result


def getHexValue(value):
    values = {
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    }

    value = str(value)

    if value in values:
        return values[value]
    else:
        return value


def checkConversion(numero, destino):
    resultado = ''
    if destino in ['Bin', 'Oct', 'Dec', 'Hex', 'Quint']:
        base = getBase(destino)
        resultado = decToBase(numero, base)
    elif destino == 'Rom':
        resultado = decToRoman(numero)

    return resultado


def getBase(destino):
    return {
        'Bin': 2,
        'Quint': 5,
        'Oct': 8,
        'Dec': 10,
        'Hex': 16
    }[destino]


def decToRoman(normal):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ['I', 'IV', 'V', 'IX', 'X', 'XL',
           'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i = len(sym) - 1
    valor = int(normal)
    resultado = ''
    while valor:
        div = valor // num[i]
        valor %= num[i]
        while div:
            resultado += sym[i]
            div -= 1
        i -= 1

    return resultado
