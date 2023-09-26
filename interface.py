import tkinter as tk
from tkinter import * 
from tkinter.ttk import * 
from time import strftime

# Estanciação das libs
root = tk.Tk()
root.title('Calculadora')
root.geometry('320x480')

label = tk.Label(root, text="")
label.pack()

# Função para adicionar o texto do botão ao visor
def button_click(event):
    current_text = label["text"]
    button_text = event.widget["text"]

    if button_text == "<-":
        # Se o botão for "<-", remove o último caractere
        label.configure(text=current_text[:-1])
    elif button_text == "CE":
        # Se o botão for "CE", limpa todo o texto
        label.configure(text="")
    elif button_text == "C":
        # Se o botão for "C", limpa apenas o último caractere
        label.configure(text="")
    elif button_text == "=":
        # Se o botão for "=", avalia a expressão no visor
        try:
            result = eval(current_text)
            label.configure(text=str(result))
        except Exception as e:
            label.configure(text="Erro")
    else:
        # Caso contrário, adiciona o texto do botão ao visor
        label.configure(text=current_text + button_text)

# Lista de botões para a calculadora
button_texts = [
    "%", "CE", "C", "<-",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Criação dos botões e atribuição da função button_click
for text in button_texts:
    button = tk.Button(root, text=text)
    button.pack()
    button.configure(command=lambda btn=button: button_click(btn))

root.resizable(False, False)
root.mainloop()
