import tkinter as tk
from PIL import Image, ImageTk
from functions import Botoes

root = tk.Tk()

class Calculadora:
    def __init__(self):
        self.root = root
        self.botoes = Botoes()
        self.interface()
        self.exibirImagem()
        self.exibirNum()
        self.exibirBotoes()

    def interface(self):
        root.title("Calculadora")
        root.geometry("320x480")
        root.resizable(False, False)

    def exibirNum(self):
        valor_default = self.botoes.get_string()
        if not valor_default:
            valor_default = "0"
        num_frame = tk.Frame(root, bg="#AA125F")
        num_frame.place(x=56, y=28, width=230, height=80)
        num_label = tk.Label(
            num_frame,
            text=valor_default,
            font=("ArchivoBlack", 28),
            fg="#FFFFFF",
            bg="#AA125F",
            anchor="w",
        )
        num_label.config(wraplength=230)
        num_label.pack(fill=tk.BOTH, expand=tk.YES)

    def exibirImagem(self):
        imagem = Image.open("assets/placeholder.png")
        imagem_tk = ImageTk.PhotoImage(imagem)
        img_frame = tk.Frame(root)
        img_frame.place(relwidth=1, relheight=1)
        img_label = tk.Label(img_frame, image=imagem_tk)
        img_label.pack(fill=tk.BOTH, expand=tk.YES)
        img_label.image = imagem_tk

    def exibirBotoes(self):
        botao_img = Image.open("assets/1.png")
        botao_img = ImageTk.PhotoImage(botao_img)
        botao = tk.Button(root, image=botao_img, command=self.botoes.add_um, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img
        botao.place(x=38, y=354)

Calculadora()
root.mainloop()
