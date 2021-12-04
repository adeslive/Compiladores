import re
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def conversion(cadena):
    opt = ['Bin','Oct', 'Hex', 'Quint', 'Rom']
    remp = random.choice(opt)
    cadena = cadena.replace('Ale',remp)
    NUMERO = r'[0-9]+'
    DECIMAL = r'Dec'
    OCTAL = r'Oct'
    HEXADECIMAL = r'Hex'
    ROMANO = r'Rom'
    BINARIO = r'Bin'
    QUINTARIO = r'Quint'

    regexList = [DECIMAL, OCTAL, HEXADECIMAL, BINARIO, ROMANO, QUINTARIO]

    OPTIONREGEX = '|'.join(regexList)

    REGEX = r'(' + NUMERO + r'(' + OPTIONREGEX + r'){1})+'
    if not re.search(REGEX, cadena):
        messagebox.showerror(message='''Las entradas válidas deben contener un número seguido de el destino como ser:
        Bin, Quint, Oct, Dec, Hex o Rom.
        Ejemplo: 13Bin''', title='Entrada inválida')
        return False

    result = []

    for match in re.findall(REGEX, cadena):
        # Por cada match se debe sacar el numero y el destino
        if re.search(NUMERO, match[0]) and re.search(OPTIONREGEX, match[0]):
            numero = re.search(NUMERO, match[0])[0]
            destino = re.search(OPTIONREGEX, match[0])[0]
            resultado = checkConversion(numero, destino)
            result.append([numero, destino, resultado])
    return result

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

class ventanaBienvenida():

    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.config(bg= '#A1D6E2')
        self.f1 = Frame(self.root, bg = '#A1D6E2')
        self.f1.grid(row = 0, column = 0)
        self.lbl = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl.grid(row = 0, column = 0,padx=20, pady=20)
        self.lbl2 = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl2.grid(row = 0, column = 2,padx=20, pady=20)
        self.f2 = Frame(self.f1, bg = 'white')
        self.f2.grid(row = 1, column = 1)
        img = Image.open("tuerca.gif")
        imgg = img.resize((150,150))
        tuerca= ImageTk.PhotoImage(imgg)
        self.img =Label(self.f2, image = tuerca, bg = 'white')
        self.img.grid(row =0 , column= 0, padx =30, sticky= E)
        self.f3 = Frame(self.f2, bg = 'white')
        self.f3.grid(row =0, column=1)
        self.lblTitle = Label(self.f3, bg= 'white', fg = '#1995AD',font = ('Roboto', 16, 'bold') , text= 'Proyecto\nConvertidor de Numeros', justify = 'left')
        self.lblTitle.grid(row= 0, column= 0, sticky = 'W', padx = (10,96), pady =10)
        self.lblTitle3 = Label(self.f3, bg= 'white', fg = '#1995AD', text= 'Diseño de Compiladores', font = ('Roboto', 14))
        self.lblTitle3.grid(row= 1, column= 0,  sticky = 'W', padx = 10)
        self.f4 = Frame(self.f1, bg = 'white')
        self.f4.grid(row = 4, column= 1)
        self.line = Canvas(self.f4, width= 550, height= 8, bg = 'white')
        self.line.create_line(0,2,550,2, fill= '#1995AD')
        self.line.create_line(0,6,550,6, fill= '#1995AD')
        self.line.grid(row=0, column= 0, columnspan= 2, padx = 10)
        # self.line2 = Canvas(self.f4, width= 400, height= 5, bg = 'white')
        # self.line2.create_line(0,2,400,2, fill= 'blue')
        # self.line2.grid(row=1, column= 0, columnspan= 2, padx = 9)
        self.lblcat = Label(self.f4, bg= 'white', fg = '#1995AD', text= '    Catedratico: Ing. Alex Hernan Moncada', font = ('Roboto', 12, 'bold'))
        self.lblcat.grid(row= 2, column= 0, columnspan= 2,padx=7.5, sticky= 'W')
        self.lblgroup = Label(self.f4, bg= 'white', fg = '#1995AD', text= '    Grupo #3', font = ('Roboto', 12))
        self.lblgroup.grid(row= 3, column= 0, columnspan= 2,padx=7.5, sticky= 'W')
        self.lblnombres = Label(self.f4, bg= 'white', fg = '#1995AD', text= '       Abner Ebiezer Betancourt', font = ('Roboto', 12))
        self.lblnombres.grid(row= 4, column= 0,padx=7.5, sticky= 'W')
        self.lblnombres2 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '       Andres Fernando Lizardo', font = ('Roboto', 12))
        self.lblnombres2.grid(row= 5, column= 0,padx=7.5, sticky= 'W')
        self.lblnombres3 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '       Fidel Ernesto Garcia', font = ('Roboto', 12))
        self.lblnombres3.grid(row= 6, column= 0,padx=7.5, sticky= 'W')
        self.lblnombres4 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '       Jose Carlos Velasquez', font = ('Roboto', 12))
        self.lblnombres4.grid(row= 7, column= 0,padx=7.5, sticky= 'W')
        self.lblnombres5 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '       Roger Alfredo Molina', font = ('Roboto', 12))
        self.lblnombres5.grid(row= 8, column= 0,padx=7.5, sticky= 'W')
        self.lblnombres6 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '       Victor Elias Vasquez', font = ('Roboto', 12))
        self.lblnombres6.grid(row= 9, column= 0,padx=7.5, sticky= 'W')
        self.lblnombres7 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '       Tomasa Clementina Meza', font = ('Roboto', 12))
        self.lblnombres7.grid(row= 10, column= 0,padx=7.5, sticky= 'W')
        self.lblcuentas = Label(self.f4, bg= 'white', fg = '#1995AD', text= '20151021802', font = ('Roboto', 12))
        self.lblcuentas.grid(row= 4, column= 1,padx=7.5, sticky= 'W')
        self.lblcuentas2 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '20161001202', font = ('Roboto', 12))
        self.lblcuentas2.grid(row= 5, column= 1,padx=7.5, sticky= 'W')
        self.lblcuentas3 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '20151001680', font = ('Roboto', 12))
        self.lblcuentas3.grid(row= 6, column= 1,padx=7.5, sticky= 'W')
        self.lblcuentas4 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '20141031775', font = ('Roboto', 12))
        self.lblcuentas4.grid(row= 7, column= 1,padx=7.5, sticky= 'W')
        self.lblcuentas5 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '20161001463', font = ('Roboto', 12))
        self.lblcuentas5.grid(row= 8, column= 1,padx=7.5, sticky= 'W')
        self.lblcuentas6 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '20161003401', font = ('Roboto', 12))
        self.lblcuentas6.grid(row= 9, column= 1,padx=7.5, sticky= 'W')
        self.lblcuentas7 = Label(self.f4, bg= 'white', fg = '#1995AD', text= '20131000142', font = ('Roboto', 12))
        self.lblcuentas7.grid(row= 10, column= 1,padx=7.5, sticky= 'W')
        # self.lblcuentas = Label(self.f4, bg= 'white', fg = '#1995AD', text= '\n20151021802\n20161001202\n20151001680\n20141031775\n20161001463\n20161003401\n20131000142')
        # self.lblcuentas.grid(row= 4, column= 1,padx=7.5)
        self.lbl = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl.grid(row = 5, column = 0,padx=20, pady=20)
        self.lbl2 = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl2.grid(row = 5, column = 2,padx=20, pady=20)
        self.btn = Button(self.f4, command= self.avanzar, text = 'Iniciar', bg = '#1995AD', fg = 'white', font = ('Roboto', 12, 'bold'), width=15)
        self.btn.grid(row =11, column= 1, padx = 10, pady = 10)
        self.root.mainloop()

    def avanzar(self):
        self.root.destroy()
        ventana = ventanaMenu()







class ventanaMenu():

    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.config(bg= '#A1D6E2')
        self.f1 = Frame(self.root, bg = '#A1D6E2')
        self.f1.grid(row = 0, column = 0)
        self.lbl = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl.grid(row = 0, column = 0,padx=20, pady=20)
        self.lbl2 = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl2.grid(row = 0, column = 2,padx=20, pady=20)
        self.f2 = Frame(self.f1, bg = 'white')
        self.f2.grid(row = 1, column = 1)
        self.lblIns = Label(self.f2, bg ='white',text = 'Instrucciones', fg = '#1995AD',font = ('Roboto', 14, 'bold'))
        self.lblIns.grid(row = 0, column= 0, pady = (20,0))
        self.lblIns1 = Label(self.f2, bg ='white',text = 'Ingrese la(s) cadenas a convertir en formato [Numero][Sistema], separados por espacios.', fg = '#1995AD',font = ('Roboto', 12))
        self.lblIns1.grid(row = 1, column= 0, sticky = 'W', padx = 10, pady =(20,0))
        self.lblIns2 = Label(self.f2, bg ='white',text = 'Ejemplo: 125Bin 321Rom 456Quint', fg = '#1995AD',font = ('Roboto', 12))
        self.lblIns2.grid(row = 2, column= 0, sticky = 'W', padx = 10, pady =(10,0))
        self.lblIns3 = Label(self.f2, bg ='white',text = 'Sistemas Disponibles:', fg = '#1995AD',font = ('Roboto', 12))
        self.lblIns3.grid(row = 3, column= 0, sticky = 'W', padx = 10, pady =(10,0))
        self.lblSis1 = Label(self.f2, bg ='white',text = '    Bin\t>    Binario', fg = '#1995AD',font = ('Roboto', 12))
        self.lblSis1.grid(row = 4, column= 0, sticky = 'W', padx = 10)
        self.lblSis1 = Label(self.f2, bg ='white',text = '    Quint\t>    Quinario', fg = '#1995AD',font = ('Roboto', 12))
        self.lblSis1.grid(row = 5, column= 0, sticky = 'W', padx = 10)
        self.lblSis1 = Label(self.f2, bg ='white',text = '    Oct\t>    Octal', fg = '#1995AD',font = ('Roboto', 12))
        self.lblSis1.grid(row = 6, column= 0, sticky = 'W', padx = 10)
        self.lblSis1 = Label(self.f2, bg ='white',text = '    Hex\t>    Hexadecimal', fg = '#1995AD',font = ('Roboto', 12))
        self.lblSis1.grid(row = 7, column= 0, sticky = 'W', padx = 10)
        self.lblSis1 = Label(self.f2, bg ='white',text = '    Rom\t>    Romano', fg = '#1995AD',font = ('Roboto', 12))
        self.lblSis1.grid(row = 8, column= 0, sticky = 'W', padx = 10)
        self.lblSis1 = Label(self.f2, bg ='white',text = '    Ale\t>    Aleatorio', fg = '#1995AD',font = ('Roboto', 12))
        self.lblSis1.grid(row = 9, column= 0, sticky = 'W', padx = 10)
        self.txtVal = StringVar()
        self.txt = Entry(self.f2, bg = '#f1f1f2', textvariable = self.txtVal,font = ('Roboto',12), width= 50)
        self.txt.grid(row = 10, column = 0, padx = 15, pady =10)
        self.btn = Button(self.f2, command= self.avanzar, text = 'Convertir', bg = '#1995AD', fg = 'white',font = ('Roboto', 12, 'bold'), width=15)
        self.btn.grid(row =11, column= 0)
        self.lbl = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl.grid(row = 2, column = 0,padx=20, pady=20)
        self.lbl2 = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl2.grid(row = 2, column = 2,padx=20, pady=20)
        self.root.mainloop()

    def avanzar(self):
        text = self.txtVal.get()
        if text == '':
            messagebox.showerror(message="Favor ingrese la cadena a convertir", title="Error")
        else:
            res = conversion(text)
            if res:
                self.root.destroy()
                ventana = ventanaResultado([text,res])

class ventanaResultado():

    def __init__(self, resultado):
        self.resultado = resultado
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.config(bg= '#A1D6E2')
        self.f1 = Frame(self.root, bg = '#A1D6E2')
        self.f1.grid(row = 0, column = 0)
        self.lbl = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl.grid(row = 0, column = 0,padx=20, pady=20)
        self.lbl2 = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl2.grid(row = 0, column = 2,padx=20, pady=20)
        self.f2 = Frame(self.f1, bg = 'white')
        self.f2.grid(row = 1, column = 1)
        self.lblTitl = Label(self.f2, bg ='white',text = 'Resultados de la Conversion', font = ('Roboto', 14,'bold'), fg = '#1995AD')
        self.lblTitl.grid(row = 0, column= 0, padx = 120, pady = 10)
        self.f3 = Frame(self.f2, bg= '#f1f1f2')
        self.f3.grid(row = 1, column = 0, sticky= 'W', padx = 15)
        self.lblL1 = Label(self.f3, bg='#f1f1f2', text = 'Analizador Lexico', font = ('Roboto', 12, 'bold'), fg = '#1995AD')
        self.lblL1.grid(row = 0, column = 0, columnspan= 3,sticky= 'W', padx = (15,500))
        self.lblL2 = Label(self.f3, bg='#f1f1f2', text = 'Linea de Token: '+resultado[0], font = ('Roboto', 12), fg = '#1995AD')
        self.lblL2.grid(row = 1, column = 0, sticky= 'W', padx = 15, pady =20)
        c = 0
        self.lblsTipo = []
        self.lblsValor = []
        self.lblsCol = []
        resTemp = []
        for i,token in enumerate(resultado[1]):
            self.lblsTipo.append(Label(self.f3, bg='#f1f1f2', text = 'Tipo de Token: [digitos]+[sistema]', font = ('Roboto', 12), fg = '#1995AD'))
            self.lblsTipo[i].grid(row = 2 + i, column = 0, sticky= 'W', padx = 15)
            self.lblsValor.append(Label(self.f3, bg='#f1f1f2', text = 'Valor de Token: ' + token[0]+token[1], font = ('Roboto', 12), fg = '#1995AD'))
            self.lblsValor[i].grid(row = 2 + i, column = 1, sticky= 'W', padx = 15)
            self.lblL5 = Label(self.f3, bg='#f1f1f2', text = 'Columna del Token: ' + str(c), font = ('Roboto', 12), fg = '#1995AD')
            self.lblL5.grid(row = 2 + i, column = 2, sticky= 'W', padx = 15)
            c += len(token[0]) + len(token[1]) + 1
            resTemp.append('Entrada: ' + token[0]+token[1] + ' => Conversión: ' + token[2])
        self.lbll = Label(self.f2, bg='white', text = '', font = ('Roboto', 12), fg = '#1995AD')
        self.lbll.grid(row = 2, column = 0)
        self.f4 = Frame(self.f2, bg= '#f1f1f2')
        self.f4.grid(row = 3, column = 0, sticky= 'W', padx = 15)
        self.lblL6 = Label(self.f4, bg='#f1f1f2', text = 'Analizador Sintactico', font = ('Roboto', 12, 'bold'), fg = '#1995AD')
        self.lblL6.grid(row = 0, column = 0, sticky= 'W', padx = (15,500))
        self.lblL7 = Label(self.f4, bg='#f1f1f2', text = 'Salida de Operacion:', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL7.grid(row = 1, column = 0, sticky= 'W', padx = 15)
        self.lblsRes = []
        for i,res in enumerate(resTemp):
            self.lblsRes.append(Label(self.f4, bg='#f1f1f2', text = res, font = ('Roboto', 12), fg = '#1995AD'))
            self.lblsRes[i].grid(row = 2+i, column = 0, sticky= 'W', padx = 15)
        
        self.btn = Button(self.f2, bg = '#1995AD',fg='white' ,command = self.avanzar, text = 'Finalizar', font = ('Roboto', 12, 'bold'), width= 15)
        self.btn.grid(row = 7, column = 0,padx=20, pady=(10,20))
        self.lbl = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl.grid(row = 2, column = 0,padx=20, pady=20)
        self.lbl2 = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl2.grid(row = 2, column = 2,padx=20, pady=20)
        self.root.mainloop()

    def avanzar(self):
        res = messagebox.askyesno(message="¿Desea Realizar otra conversion?", title="Salir")
        self.root.destroy()
        if res:
            ventana = ventanaMenu()
        
        
        
v = ventanaBienvenida()
