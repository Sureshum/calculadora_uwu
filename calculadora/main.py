from tkinter import *
from tkinter import ttk
import math 
from mensajito import click

def TemaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#4C478B")

    estilos_label.configure('Label.TLabel', background="#4E4894", foreground="white")
    estilos_label1.configure('Label1.TLabel', background="#4E4894", foreground="white")

    estilos_botones_num.configure('Botones_numeros.TButton', background="#2B2673", foreground="white")
    estilos_botones_num.map('Botones_numeros.TButton', background=[('active', '#020A90')])
    estilos_botones_borrar.configure('botones_borrar.TButton', background="#3E3A75", foreground="white")
    estilos_botones_num.map('botones_borrar.TButton', background=[('active', '#3444AB')])
    estilos_botones.configure('botones.TButton', background="#3E3A75", foreground="white")
    estilos_botones_num.map('botones.TButton', background=[('active', '#3444AB')])

def TemaClaro(*args):
    estilos.configure('mainframe.TFrame', background="#DBDBDB", foreground="black")

    estilos_label.configure('Label.TLabel', background="#DBDBDB", foreground="black")
    estilos_label1.configure('Label1.TLabel', background="#DBDBDB", foreground="black")

    estilos_botones_num.configure('Botones_numeros.TButton', background="#FFFFFF", foreground="black")
    estilos_botones_num.map('Botones_numeros.TButton', background=[('active', '#CECECE')])
    estilos_botones_borrar.configure('botones_borrar.TButton', background="#CECECE", foreground="black")
    estilos_botones_num.map('botones_borrar.TButton', background=[('active', '#9e9d9d')])
    estilos_botones.configure('botones.TButton', background="#CECECE", foreground="black")
    estilos_botones_num.map('botones.TButton', background=[('active', '#9e9d9d')])

def borrar(*args):
    inicio = 0
    final = len(entrada1.get())
    entrada1.set(entrada1.get()[inicio:final-1])

def ingresar_valores(tecla):
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada1.set(entrada1.get() + tecla)

    if tecla == '+' or tecla == '-' or tecla == '*' or tecla == '/':
        if tecla == '*':
            entrada.set(entrada1.get()+ '*')
        elif tecla == '/':
            entrada.set(entrada1.get() + '/')
        elif tecla == '+':
            entrada.set(entrada1.get() + '+')
        elif tecla == '-':
            entrada.set(entrada1.get() + '-')

        entrada1.set('')

    if tecla == '=':
        entrada.set(entrada.get() + entrada1.get())
        resultado = eval(entrada.get())
        entrada1.set(resultado)

def raiz():
    entrada.set('')
    resultado = math.sqrt(float(entrada1.get()))
    entrada1.set(resultado)

def borrar_todo(*args):
    entrada.set('')
    entrada1.set('')

def ingresaValorTecla(event):
    tecla = event.char
    print(event)

    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        entrada1.set(entrada1.get() + tecla)

    if tecla == '+' or tecla == '-' or tecla == '*' or tecla == '/':
        if tecla == '*':
            entrada.set(entrada1.get()+ '*')
        elif tecla == '/':
            entrada.set(entrada1.get() + '/')
        elif tecla == '+':
            entrada.set(entrada1.get() + '+')
        elif tecla == '-':
            entrada.set(entrada1.get() + '-')

        entrada1.set('')

    if tecla == '=':
        entrada.set(entrada.get() + entrada1.get())
        resultado = eval(entrada.get())
        entrada1.set(resultado)


root = Tk()
root.title("calculadora :v")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.configure('mainframe.TFrame', background ="#DBDBDB")
estilos.theme_use('clam')

mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)


estilos_label = ttk.Style()
estilos_label.configure('Label.TLabel', font="arial 15", anchor= "e")

estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 40", anchor= "e")

entrada = StringVar()
label_entrada = ttk.Label(mainframe, textvariable=entrada, style="Label.TLabel")
label_entrada.grid(column=0, row=0, columnspan=4, sticky=(W,E,S,N))

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=1, columnspan=4, sticky=(W,E,S,N))

estilos_botones_num = ttk.Style()
estilos_botones_num.configure('Botones_numeros.TButton', font="arial 22", width=5, background ="#FFFFFF", relief='flat')
estilos_botones_num.map('Botones_numeros.TButton', background=[('active', '#898989')])

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('botones_borrar.TButton', font="arial 22", width= 5, relief="flat", background="#CECECE")
estilos_botones_borrar.map('botones_borrar.TButton', foreground=[('active', '#ff0000')], background=[('active', '#858585')])

estilos_botones = ttk.Style()
estilos_botones.configure('botones.TButton', font="arial 22", width = 5, relief="flat", background="#CECECE")
estilos_botones.map('botones.TButton', background=[('active', '#858585')])

button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: ingresar_valores('0'))
button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: ingresar_valores('1'))
button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: ingresar_valores('2'))
button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: ingresar_valores('3'))
button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: ingresar_valores('4'))
button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: ingresar_valores('5'))
button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: ingresar_valores('6'))
button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: ingresar_valores('7'))
button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: ingresar_valores('8'))
button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: ingresar_valores('9'))

button_borrar = ttk.Button(mainframe, text=chr(9003), style="botones_borrar.TButton", command=lambda: borrar())
button_borrar_todo = ttk.Button(mainframe, text="C", style="botones_borrar.TButton", command=lambda: borrar_todo())
button_parentesis1 = ttk.Button(mainframe, text="(", style="botones.TButton", command=lambda: ingresar_valores('('))
button_parentesis2 = ttk.Button(mainframe, text=")", style="botones.TButton", command=lambda: ingresar_valores(')'))
button_punto = ttk.Button(mainframe, text=".", style="botones.TButton", command=lambda: ingresar_valores('.'))

button_suma = ttk.Button(mainframe, text="+", style="botones.TButton", command=lambda: ingresar_valores('+'))
button_resta = ttk.Button(mainframe, text="-", style="botones.TButton", command=lambda: ingresar_valores('-'))
button_multi = ttk.Button(mainframe, text="x", style="botones.TButton", command=lambda: ingresar_valores('*'))
button_division = ttk.Button(mainframe, text=chr(247), style="botones.TButton", command=lambda: ingresar_valores('/'))

button_igual = ttk.Button(mainframe, text="=", style="botones.TButton", command=lambda: ingresar_valores('='))
button_raiz_cuadrada = ttk.Button(mainframe, text="√", style="botones.TButton", command=lambda: raiz())

button_parentesis1.grid(column=0, row=2, sticky=(W,E,S,N))
button_parentesis1.grid(column=0, row=2, sticky=(W,E,S,N))
button_parentesis2.grid(column=1, row=2, sticky=(W,E,S,N))
button_borrar_todo.grid(column=2, row=2, sticky=(W,E,S,N))
button_borrar.grid(column=3, row=2, sticky=(W,E,S,N))

button7.grid(column=0, row=3, sticky=(W,E,S,N))
button8.grid(column=1, row=3, sticky=(W,E,S,N))
button9.grid(column=2, row=3, sticky=(W,E,S,N))
button_division.grid(column=3, row=3, sticky=(W,E,S,N))

button4.grid(column=0, row=4, sticky=(W,E,S,N))
button5.grid(column=1, row=4, sticky=(W,E,S,N))
button6.grid(column=2, row=4, sticky=(W,E,S,N))
button_multi.grid(column=3, row=4, sticky=(W,E,S,N))

button1.grid(column=0, row=5, sticky=(W,E,S,N))
button2.grid(column=1, row=5, sticky=(W,E,S,N))
button3.grid(column=2, row=5, sticky=(W,E,S,N))
button_suma.grid(column=3, row=5, sticky=(W,E,S,N))

button1.grid(column=0, row=5, sticky=(W,E,S,N))
button2.grid(column=1, row=5, sticky=(W,E,S,N))
button3.grid(column=2, row=5, sticky=(W,E,S,N))
button_resta.grid(column=3, row=5, sticky=(W,E,S,N))

button0.grid(column=0, row=6, columnspan=2, sticky=(W,E,S,N))
button_punto.grid(column=2, row=6, sticky=(W,E,S,N))
button_resta.grid(column=3, row=6, sticky=(W,E,S,N))

button_igual.grid(column=0, row=7, columnspan=3, sticky=(W,E,S,N))
button_raiz_cuadrada.grid(column=3, row=7, sticky=(W,E,S,N))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-o>', TemaOscuro)
root.bind('<KeyPress-c>', TemaClaro)
root.bind('<Key>', ingresaValorTecla)
root.bind('<KeyPress-b>', borrar)
root.bind('<KeyPress-n>', borrar_todo)

root.mainloop()

