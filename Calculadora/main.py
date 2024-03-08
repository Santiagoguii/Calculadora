import tkinter as tk
from tkinter import *

# Armazzenando os operandos 
number1 = ''
number2 = ''

# Flags
adicao = FALSE
subtracao = FALSE
multiplicacao = FALSE
divisao = FALSE


# Configurando interface 
root = Tk()
root.title('Calculadora')
root.geometry("300x500") # Ajuste o tamanho conforme necessário


root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#3d3d3d', font=('futura', 20, 'bold'), justify=RIGHT)
e.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

#Funções para operações básicas
def button_click(num):
    e.insert(END, num)


def button_adiciona():
    global number1
    global adicao
    adicao = TRUE
    number1 = e.get()
    e.delete(0, END)


def button_subrai():
    global number1
    global subtracao
    subtracao = TRUE
    number1 = e.get()
    e.delete(0, END)


def button_multiplica():
    global number1
    global multiplicacao
    multiplicacao = TRUE
    number1 = e.get()
    e.delete(0, END)


def button_divide():
    global number1
    global divisao
    divisao = TRUE
    number1 = e.get()
    e.delete(0, END)


def button_igual():
    global subtracao
    global divisao
    global multiplicacao
    global adicao
    number2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(number1) + int(number2))
        adicao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(number1) * int(number2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(number1) - int(number2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(number1) // int(number2))
        divisao = FALSE


def button_limpa():
    e.delete(0, END)

#Funcões para criar os botões
def button_num(num, row, column):
    button = Button(root,
                   text=num,
                   padx=25,
                   pady=25,
                   command=lambda: button_click(num),
                   fg='#FFFFFF',
                   activebackground='#3d3d3d',
                   activeforeground='#FFFFFF',
                   bg='#1f1f1f',
                   relief=FLAT,
                   font=('futura', 14, 'bold'))
    button.grid(row=row, column=column, padx=5, pady=5)

def button_operator(op, command, row, column):
    operator = Button(root,
                      text=op,
                      padx=25,
                      pady=25,
                      command=command,
                      fg='#FFFFFF',
                      activebackground='#3d3d3d',
                      activeforeground='#FFFFFF',
                      bg='#5d5d5d',
                      relief=FLAT,
                      font=('futura', 14, 'bold'))
    operator.grid(row=row, column=column, padx=5, pady=5)

button_operator('÷', button_divide, 1, 3)
button_operator('×', button_multiplica, 2, 3)
button_operator('-', button_subrai, 3, 3)
button_operator('+', button_adiciona, 4, 3)
button_num(1, 1, 0)
button_num(2, 1, 1)
button_num(3, 1, 2)
button_num(4, 2, 0)
button_num(5, 2, 1)
button_num(6, 2, 2)
button_num(7, 3, 0)
button_num(8, 3, 1)
button_num(9, 3, 2)
button_num(0, 4, 1)
button_operator('C', button_limpa, 4, 0)
button_operator('=', button_igual, 4, 2)

root.mainloop()