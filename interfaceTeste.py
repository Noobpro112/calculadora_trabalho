import tkinter as tk
from tkinter import *

root = tk.Tk()

class Calculadora:
    def __init__(self):
        self.root = root
        self.interface()
        self.exibirNum(30.5, 18.8, 30.5 + 257.5, 18.8 + 96, radius=15, fill="#DE2861")  # Define a cor de fundo como a cor desejada

    def interface(self):
        root.title('Calculadora')
        root.geometry('320x480')
        root.resizable(False, False)
        root.configure(background="#DE2861")

    def exibirNum(self, x1, y1, x2, y2, radius=0, **kwargs):
        self.valor_inteiro = 0
        self.label = Label(root, text=str(self.valor_inteiro), font=("ArchivoBlack", 38), fg="#FFFFFF", bg="#AA125F")  # Defina a cor de fundo como a cor desejada
        self.label.place(x=240, y=48)  # Ajustar posição

    def atualizar_valor(self, novo_valor):
        # Atualiza o valor inteiro e atualiza o texto na Label
        self.valor_inteiro = novo_valor
        self.label.config(text=str(self.valor_inteiro))

Calculadora()
root.mainloop()
