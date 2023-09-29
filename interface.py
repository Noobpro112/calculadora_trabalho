import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from functions import Botoes

root = tk.Tk()


class Calculadora:
    def __init__(self):
        self.root = root
        self.botoes = Botoes()
        self.interface()
        self.exibirImagem()  # Primeiro exibir a imagem
        self.exibirNum()  # Depois exibir o texto
        # SIM ISSO FOI IMPORTANTE,

    def interface(self):
        root.title("Calculadora")
        root.geometry("320x480")
        root.resizable(False, False)

    def exibirNum(self):
        valor_default = self.botoes.get_string()
        num_frame = Frame(root, bg="#AA125F")
        num_frame.place(x=56, y=28, width=230, height=80)
        num_label = Label(
            num_frame,
            text=valor_default,
            font=("ArchivoBlack", 28),
            fg="#FFFFFF",
            bg="#AA125F",
            anchor="w",
        )
        num_label.config(wraplength=230)
        num_label.pack(fill=BOTH, expand=YES)

    def exibirImagem(self):
        imagem = Image.open("assets/placeholder.png")
        imagem_tk = ImageTk.PhotoImage(imagem)
        img_frame = Frame(root)
        img_frame.place(relwidth=1, relheight=1)
        img_label = Label(img_frame, image=imagem_tk)
        img_label.pack(fill=BOTH, expand=YES)
        img_label.image = imagem_tk

    def atualizar_valor(self, novo_valor):
        self.botoes.valor_default = novo_valor
        self.exibirNum()


Calculadora()
root.mainloop()
