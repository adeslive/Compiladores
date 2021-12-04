import re
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def conversion(origen, destino, cadena):
    binPattern = r'^[0-1]+$'
    decPattern = r'^[0-9]+$'
    hexPattern = r'^([0-9]|[A-F])+$'
    octPattern = r'^[0-9]*[0-7]+$'
    quiPattern = r'^[0-9]*[0-4]+$'
    romPattern = r'Rom'

    patternMap = {
        1: decPattern,
        2: binPattern,
        3: octPattern,
        4: hexPattern,
        5: quiPattern,
        6: romPattern
    }
    bases = [10,2,8,16,5]
    if re.match(patternMap[origen], cadena):
        if origen == destino:
            return cadena
        elif origen != 6:
            if origen == 1:
                return decToBase(cadena, bases[destino-1])
            elif destino != 6:
                return decToBase(baseToDec(cadena, bases[origen-1]), bases[destino-1])
            else:
                #Aqui va cuando el destino es romano
                return False
        else:
            #Aqui va cuando el origen es el romano
            return False
    else:
        messagebox.showerror(message="La cadena no coincide con el sistema de Origen", title="Error")
        return False


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


def getDecValue(value):
    values = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
    }

    value = str(value)

    if value in values:
        return values[value]
    else:
        return value


def baseToDec(number, base):
    position = 0
    result = 0
    binary = number[::-1]

    for n in binary:
        value = base**position
        if base == 16:
            n = getDecValue(n)
        result += value*int(n)
        position += 1
    return result

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
        self.lblIns1 = Label(self.f2, bg ='white',text = '1. Seleccione el sistema en que ingresara la cadena a convertir', fg = '#1995AD',font = ('Roboto', 12))
        self.lblIns1.grid(row = 1, column= 0, sticky = 'W', padx = 10, pady =(20,0))
        opciones = [
            ('Decimal', 1),
            ('Binario', 2),
            ('Octal', 3),
            ('Hexadecimal', 4),
            ('Quintal', 5),
            ('Romano', 6)
        ]
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.opt1 = []
        self.opt2 = []
        for texto, valor in opciones:
            self.opt1.append(Radiobutton(self.f2, text = texto, variable= self.v1, value = valor, bg= 'white', fg = '#1995AD',font = ('Roboto', 12)))
            self.opt1[valor-1].grid(row = valor +1, column = 0, sticky = 'W', padx = 15)
        # self.lblIns.grid(row = 0, column= 0)
        self.lblIns2 = Label(self.f2, bg ='white',text = '2. Ingrese la cadena a convertir', fg = '#1995AD',font = ('Roboto', 12))
        self.lblIns2.grid(row = 8, column= 0, sticky = 'W' , padx = 10, pady =(20,0))
        self.txtVal = StringVar()
        self.txt = Entry(self.f2, bg = '#f1f1f2', textvariable = self.txtVal,font = ('Roboto',12))
        self.txt.grid(row = 9, column = 0, sticky = 'W', padx = 15, pady =10)
        self.lblIns1 = Label(self.f2, bg ='white',text = '3. Seleccione el sistema al cual convertir la cadena', fg = '#1995AD',font = ('Roboto', 12))
        self.lblIns1.grid(row = 10, column= 0, sticky = 'W', padx = 10, pady =(20,0))
        for texto, valor in opciones:
            self.opt2.append(Radiobutton(self.f2, text = texto, variable= self.v2, value = valor, bg = 'white', fg = '#1995AD',font = ('Roboto', 12)))
            self.opt2[valor-1].grid(row = valor +10, column = 0, sticky = 'W', padx = 15)
        self.btn = Button(self.f2, command= self.avanzar, text = 'Convertir', bg = '#1995AD', fg = 'white',font = ('Roboto', 12, 'bold'), width=15)
        self.btn.grid(row =17, column= 0)
        self.lbl = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl.grid(row = 2, column = 0,padx=20, pady=20)
        self.lbl2 = Label(self.f1, bg ='#A1D6E2',text = '')
        self.lbl2.grid(row = 2, column = 2,padx=20, pady=20)
        self.root.mainloop()

    def avanzar(self):
        opt1 = self.v1.get()
        text = self.txtVal.get()
        opt2 = self.v2.get()
        if opt1 == 0:
            messagebox.showerror(message="Favor seleccione el sistema de la cadena", title="Error")
        elif text == '':
            messagebox.showerror(message="Favor ingrese la cadena a convertir", title="Error")
        elif opt2 == 0:
            messagebox.showerror(message="Favor seleccione el sistema a convertir de la cadena", title="Error")
        else:
            res = conversion(opt1, opt2, text)
            if res:
                self.root.destroy()
                ventana = ventanaResultado(res)

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
        self.lblL1.grid(row = 0, column = 0, sticky= 'W', padx = (15,500))
        self.lblL2 = Label(self.f3, bg='#f1f1f2', text = 'Linea de Token: ', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL2.grid(row = 1, column = 0, sticky= 'W', padx = 15)
        self.lblL3 = Label(self.f3, bg='#f1f1f2', text = 'Tipo de Token: ', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL3.grid(row = 2, column = 0, sticky= 'W', padx = 15)
        self.lblL4 = Label(self.f3, bg='#f1f1f2', text = 'Valor o Elemento de Operacion: ', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL4.grid(row = 3, column = 0, sticky= 'W', padx = 15)
        self.lblL5 = Label(self.f3, bg='#f1f1f2', text = 'Otro: ', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL5.grid(row = 4, column = 0, sticky= 'W', padx = 15)
        self.lbll = Label(self.f2, bg='white', text = '', font = ('Roboto', 12), fg = '#1995AD')
        self.lbll.grid(row = 2, column = 0)
        self.f4 = Frame(self.f2, bg= '#f1f1f2')
        self.f4.grid(row = 3, column = 0, sticky= 'W', padx = 15)
        self.lblL6 = Label(self.f4, bg='#f1f1f2', text = 'Analizador Sintactico', font = ('Roboto', 12, 'bold'), fg = '#1995AD')
        self.lblL6.grid(row = 0, column = 0, sticky= 'W', padx = (15,500))
        self.lblL7 = Label(self.f4, bg='#f1f1f2', text = '¿Arbol?', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL7.grid(row = 1, column = 0, sticky= 'W', padx = 15)
        self.lblL8 = Label(self.f4, bg='#f1f1f2', text = '', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL8.grid(row = 2, column = 0)
        self.lblL9 = Label(self.f4, bg='#f1f1f2', text = '', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL9.grid(row = 3, column = 0)
        self.lblL10 = Label(self.f4, bg='#f1f1f2', text = '', font = ('Roboto', 12), fg = '#1995AD')
        self.lblL10.grid(row = 4, column = 0)
        self.lblres = Label(self.f2, bg = '#E3DB8A', text = 'Resultado Final: '+self.resultado, font = ('Roboto', 12))
        self.lblres.grid(row = 5, column = 0,padx=20, pady=20)
        self.lblres = Button(self.f2, bg = '#1995AD',fg='white' ,command = self.avanzar, text = 'Finalizar', font = ('Roboto', 12, 'bold'), width= 15)
        self.lblres.grid(row = 6, column = 0,padx=20, pady=(0,20))
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