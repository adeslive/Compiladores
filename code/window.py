import logic as lgc
from tkinter import *


winConvert = Tk()
winConvert.title('Multiconversor')
winConvert.geometry("600x250")
winConvert.eval('tk::PlaceWindow . center')

lblTitle = Label(winConvert, text='Multiconversor')
lblTitle.pack(pady=5)
lblInstruction = Label(
    winConvert, text='Ingrese una cadena valida (Número decimal + destino de conversión)')
lblInstruction.pack()
iptUserString = Entry(winConvert, width=70, text='Multiconversor')
iptUserString.pack(pady=5)


def convertClick():
    lgc.convert(iptUserString.get(), winConvert)
    iptUserString.delete(0, 'end')


btnAccept = Button(winConvert, text="Convertir",
                   command=convertClick)
btnAccept.pack(pady=5)


def open():
    winConvert.mainloop()
