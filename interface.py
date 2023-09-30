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
        self.root.title("Calculadora")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        #Icone
        icon = Image.open("assets/icone.ico")
        icon_tk = ImageTk.PhotoImage(icon)
        self.root.tk.call('wm', 'iconphoto', self.root._w, icon_tk)
        #Barra de tarefas
        taskbar = Image.open("assets/icone_taskbar.png")
        taskbar = taskbar.resize((16, 16))
        taskbar_tk = ImageTk.PhotoImage(taskbar)
        self.root.iconphoto(True, taskbar_tk)

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
        botao = tk.Button(root, image=botao_img0, command=self.botao_click_zero, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img0
        botao.place(x=38, y=354)

        botao_img1 = Image.open("assets/1.png")
        botao_img1 = ImageTk.PhotoImage(botao_img1)
        botao = tk.Button(root, image=botao_img1, command=self.botao_click_um, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img1
        botao.place(x=38, y=280)

        botao_img2 = Image.open("assets/2.png")
        botao_img2 = ImageTk.PhotoImage(botao_img2)
        botao = tk.Button(root, image=botao_img2, command=self.botao_click_dois, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img2
        botao.place(x=100, y=280)

        botao_img3 = Image.open("assets/3.png")
        botao_img3 = ImageTk.PhotoImage(botao_img3)
        botao = tk.Button(root, image=botao_img3, command=self.botao_click_tres, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img3
        botao.place(x=163, y=280)

        botao_img4 = Image.open("assets/4.png")
        botao_img4 = ImageTk.PhotoImage(botao_img4)
        botao = tk.Button(root, image=botao_img4, command=self.botao_click_quatro, borderwidth=0, bg="#DE2861",)
        botao.image = botao_img4
        botao.place(x=36, y=206)

        botao_img5 = Image.open("assets/5.png")
        botao_img5 = ImageTk.PhotoImage(botao_img5)
        botao = tk.Button(root, image=botao_img5, command=self.botao_click_cinco, borderwidth=0, bg="#DE2861")
        botao.image = botao_img5
        botao.place(x=99, y=206)

        botao_img6 = Image.open("assets/6.png")
        botao_img6 = ImageTk.PhotoImage(botao_img6)
        botao = tk.Button(root, image=botao_img6, command=self.botao_click_seis, borderwidth=0, bg="#DE2861")
        botao.image = botao_img6
        botao.place(x=161, y=206)

        botao_img7 = Image.open("assets/7.png")
        botao_img7 = ImageTk.PhotoImage(botao_img7)
        botao = tk.Button(root, image=botao_img7, command=self.botao_click_sete, borderwidth=0, bg="#DE2861")
        botao.image = botao_img7
        botao.place(x=38, y=133)

        botao_img8 = Image.open("assets/8.png")
        botao_img8 = ImageTk.PhotoImage(botao_img8)
        botao = tk.Button(root, image=botao_img8, command=self.botao_click_oito, borderwidth=0, bg="#DE2861")
        botao.image = botao_img8
        botao.place(x=100, y=133)

        botao_img9 = Image.open("assets/9.png")
        botao_img9 = ImageTk.PhotoImage(botao_img9)
        botao = tk.Button(root, image=botao_img9, command=self.botao_click_nove, borderwidth=0, bg="#DE2861")
        botao.image = botao_img9
        botao.place(x=163, y=133)

        botao_imgce = Image.open("assets/CE.png")
        botao_imgce = ImageTk.PhotoImage(botao_imgce)
        botao = tk.Button(root, image=botao_imgce, command=self.botao_click_clear, borderwidth=0, bg="#DE2861")
        botao.image = botao_imgce
        botao.place(x=100, y=354)

        botao_imgigu = Image.open("assets/=.png")
        botao_imgigu = ImageTk.PhotoImage(botao_imgigu)
        botao = tk.Button(root, image=botao_imgigu, command=self.botao_igual_click, borderwidth=0, bg="#DE2861")
        botao.image = botao_imgigu
        botao.place(x=163, y=354)

        botao_imgmais = Image.open("assets/+.png")
        botao_imgmais = ImageTk.PhotoImage(botao_imgmais)
        botao = tk.Button(root, image=botao_imgmais, command=self.botao_click_mais, borderwidth=0, bg="#DE2861")
        botao.image = botao_imgmais
        botao.place(x=229, y=354)

        botao_imgmenos = Image.open("assets/-.png")
        botao_imgmenos = ImageTk.PhotoImage(botao_imgmenos)
        botao = tk.Button(root, image=botao_imgmenos, command=self.botao_click_menos, borderwidth=0, bg="#DE2861")
        botao.image = botao_imgmenos
        botao.place(x=226, y=280)

        botao_imgx = Image.open("assets/x.png")
        botao_imgx = ImageTk.PhotoImage(botao_imgx)
        botao = tk.Button(root, image=botao_imgx, command=self.botao_click_mult, borderwidth=0, bg="#DE2861")
        botao.image = botao_imgx
        botao.place(x=224, y=206)

        botao_imgdiv = Image.open("assets/div.png")
        botao_imgdiv = ImageTk.PhotoImage(botao_imgdiv)
        botao = tk.Button(root, image=botao_imgdiv, command=self.botao_click_div, borderwidth=0, bg="#DE2861")
        botao.image = botao_imgdiv
        botao.place(x=226, y=132)

        botao_imgponto = Image.open("assets/ponto.png")
        botao_imgponto = ImageTk.PhotoImage(botao_imgponto)
        botao = tk.Button(root, image=botao_imgponto, command=self.botao_click_ponto, borderwidth=0, bg="#DE2861")
        botao.image = botao_imgponto
        botao.place(x=7, y=420)

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

    def botao_click_mais(self):
        self.botoes.add_mais()
        self.exibirNum()

    def botao_click_menos(self):
        self.botoes.add_menos()
        self.exibirNum()

    def botao_click_mult(self):
        self.botoes.add_mult()
        self.exibirNum()

    def botao_click_div(self):
        self.botoes.add_div()
        self.exibirNum()

    def botao_click_ponto(self):
        self.botoes.add_ponto_decimal()
        self.exibirNum()

    def botao_click_clear(self):
        self.botoes.clear()
        self.exibirNum()

    def botao_igual_click(self):
        self.valor = self.botoes.evaluate()
        self.exibirNum()

if __name__ == "__main__":
    calculadora = Calculadora()
    root.mainloop()