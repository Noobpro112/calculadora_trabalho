import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()

class Calculadora:
    def __init__(self):
        self.root = root
        self.interface()
        self.exibirNum()
        self.exibirImagem()

    def interface(self):
        root.title('Calculadora')
        root.geometry('320x480')
        root.resizable(False, False)

    def exibirNum(self):
        self.valor_inteiro = 0
        self.label = Label(root, text=str(self.valor_inteiro), font=("ArchivoBlack", 38), fg="#FFFFFF", bg="#AA125F")
        self.label.place(x=240, y=48)

    def exibirImagem(self):
        imagem = Image.open("assets/placeholder.png")
        imagem_tk = ImageTk.PhotoImage(imagem)

        self.background_label = Label(root, image=imagem_tk)
        self.background_label.place(relwidth=1, relheight=1)
        self.background_label.image = imagem_tk

    def atualizar_valor(self, novo_valor):
        self.valor_inteiro = novo_valor
        self.label.config(text=str(self.valor_inteiro))

Calculadora()
root.mainloop()
