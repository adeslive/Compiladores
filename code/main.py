import re

# Patrones:
NUMERO = r'[0-9]+'
DECIMAL = r'Decimal'
OCTAL = r'Octal'
HEXADECIMAL = r'Hexadecimal'
ROMANO = r'Romano'
BINARIO = r'Binario'

regexList = [DECIMAL, OCTAL, HEXADECIMAL, BINARIO, ROMANO]

OPTIONREGEX = '|'.join(regexList)

REGEX = NUMERO + OPTIONREGEX


def showOptions():
    cadena = input('Por favor, ingrese una cadena valida:')
    print(re.findall(REGEX, cadena))
    print(re.findall(NUMERO, cadena))
    print(re.findall(OPTIONREGEX, cadena))


def main():
    print('Multiconversor')
    showOptions()


if __name__ == '__main__':
    main()
