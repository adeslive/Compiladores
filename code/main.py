from tkinter import *
import re

# Patrones:
NUMERO = r'[0-9]+'
DECIMAL = r'Dec'
OCTAL = r'Oct'
HEXADECIMAL = r'Hex'
ROMANO = r'Rom'
BINARIO = r'Bin'

regexList = [DECIMAL, OCTAL, HEXADECIMAL, BINARIO, ROMANO]

OPTIONREGEX = r'(' + '|'.join(regexList) + r'){1}'

REGEX = r'(' + NUMERO + OPTIONREGEX + r')+'


winConvert = Tk()
winConvert.geometry("600x250")
winConvert.eval('tk::PlaceWindow . center')

lblTitle = Label(winConvert, text='Multiconversor')
lblTitle.pack(pady=5)
lblInstruction = Label(
    winConvert, text='Ingrese una cadena valida (Número decimal + destino de conversión)')
lblInstruction.pack()
iptUserString = Entry(winConvert, width=70, text='Multiconversor')
iptUserString.pack(pady=5)


def convert():
    cadena = iptUserString.get()
    for match in re.findall(REGEX, cadena):
        print(match[0])
        lblReceipt = Label(winConvert, text='Entrada: ' +
                           match[0] + ' => Conversión: (a desarrollar)')
        lblReceipt.pack()


btnAccept = Button(winConvert, text="Convertir", command=convert)
btnAccept.pack(pady=5)


def main():
    print('Multiconversor')
    winConvert.mainloop()


if __name__ == '__main__':
    main()
