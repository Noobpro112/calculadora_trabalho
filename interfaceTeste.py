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
        botao_img0 = Image.open("assets/0.png")
        botao_img0 = ImageTk.PhotoImage(botao_img0)
        botao = tk.Button(root, image=botao_img0, command=self.botoes.add_zero, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img0
        botao.place(x=38, y=354)

        botao_img1 = Image.open("assets/1.png")
        botao_img1 = ImageTk.PhotoImage(botao_img1)
        botao = tk.Button(root, image=botao_img1, command=self.botao_click_um, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img1
        botao.place(x=38, y=280)

        botao_img2 = Image.open("assets/2.png")
        botao_img2 = ImageTk.PhotoImage(botao_img2)
        botao = tk.Button(root, image=botao_img2, command=self.botoes.add_dois, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img2
        botao.place(x=100, y=280)

    def botao_click_zero(self):
        self.botoes.add_zero()
        self.exibirNum()

    def botao_click_um(self):
        self.botoes.add_um()
        self.exibirNum()

    def botao_click_dois(self):
        self.botoes.add_dois()
        self.exibirNum()

    def botao_click_tres(self):
        self.botoes.add_tres()
        self.exibirNum()

    def botao_click_quatro(self):
        self.botoes.add_quatro()
        self.exibirNum()

    def botao_click_cinco(self):
        self.botoes.add_cinco()
        self.exibirNum()

    def botao_click_seis(self):
        self.botoes.add_seis()
        self.exibirNum()

    def botao_click_sete(self):
        self.botoes.add_sete()
        self.exibirNum()

    def botao_click_oito(self):
        self.botoes.add_oito()
        self.exibirNum()

    def botao_click_nove(self):
        self.botoes.add_nove()
        self.exibirNum()


if __name__ == "__main__":
    calculadora = Calculadora()
    root.mainloop()
