from tkinter import *
from tkinter.ttk import*
from time import strftime

janela = Tk() # criando janela

janela.title('Clock') # titulo da janela

# Função relogio

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
lbl = Label(janela, font = ('franklin gothic', 40, 'bold'),
            background = 'black',
            foreground = 'white')
lbl.pack(anchor = 'center')
time()
mainloop()
