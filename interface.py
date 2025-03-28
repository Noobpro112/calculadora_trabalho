import tkinter as tk
from PIL import Image, ImageTk
from functions import Botoes

class CalculadoraInterface:
    def __init__(self, root):
        self.root = root
        self.botoes_backend = Botoes()
        self.botoes_interface = {}
        self.setup_interface()

    def setup_interface(self):
        self.root.title("Calculadora")
        self.root.geometry("320x480")
        self.root.resizable(False, False)
        self.setup_icons()
        self.setup_background()
        self.setup_display()
        self.load_buttons()
        self.position_buttons()

    def setup_icons(self):
        try:
            self.root.iconbitmap("assets/icone.ico")
            
            taskbar_icon = Image.open("assets/icone_taskbar.png")
            taskbar_photo = ImageTk.PhotoImage(taskbar_icon)
            
            self.root.tk.call('wm', 'iconphoto', self.root._w, taskbar_photo)
            
            self.root.iconphoto(False, taskbar_photo)
            
        except Exception as e:
            print(f"icones não carregados {e}")

    def setup_background(self):
        try:
            bg_image = Image.open("assets/placeholder.png")
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.image = self.bg_photo
        except:
            bg_frame = tk.Frame(self.root, bg="#F0F0F0")
            bg_frame.place(x=0, y=0, relwidth=1, relheight=1)

    def setup_display(self):
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        display_frame = tk.Frame(self.root, bg="#AA125F")
        display_frame.place(x=56, y=28, width=230, height=80)
        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("ArchivoBlack", 28),
            fg="#FFFFFF",
            bg="#AA125F",
            anchor="e",
            padx=10
        )
        display_label.pack(fill=tk.BOTH, expand=True)

    def load_buttons(self):
        button_map = {
            '0.png': self.botoes_backend.add_zero,
            '1.png': self.botoes_backend.add_um,
            '2.png': self.botoes_backend.add_dois,
            '3.png': self.botoes_backend.add_tres,
            '4.png': self.botoes_backend.add_quatro,
            '5.png': self.botoes_backend.add_cinco,
            '6.png': self.botoes_backend.add_seis,
            '7.png': self.botoes_backend.add_sete,
            '8.png': self.botoes_backend.add_oito,
            '9.png': self.botoes_backend.add_nove,
            'CE.png': self.botoes_backend.clear,
            'div.png': self.botoes_backend.add_div,
            'ponto.png': self.botoes_backend.add_ponto_decimal,
            'x.png': self.botoes_backend.add_mult,
            '+.png': self.botoes_backend.add_mais,
            '-.png': self.botoes_backend.add_menos,
            '=.png': lambda: [self.botoes_backend.evaluate(), self.update_display()],
            'back.png': self.botoes_backend.backspace,
            'exp.png': self.botoes_backend.calcular_potencia
        }

        for img_file, command in button_map.items():
            try:
                img_path = f"assets/{img_file}"
                img = Image.open(img_path)
                img = ImageTk.PhotoImage(img)
                btn = tk.Button(
                    self.root,
                    image=img,
                    command=lambda cmd=command: [cmd(), self.update_display()],
                    borderwidth=0,
                    bg="#DE2861",
                    activebackground="#DE2861"
                )
                btn.image = img
                self.botoes_interface[img_file] = btn
            except Exception as e:
                print(f"Erro ao carregar {img_file}: {e}")
                print(f"Caminho tentado: {img_path}")

    def position_buttons(self):
        COLUNA_1 = 38
        COLUNA_2 = 103
        COLUNA_3 = 167
        COLUNA_4 = 233
        LINHA_1 = 128
        LINHA_2 = 200
        LINHA_3 = 274
        LINHA_4 = 348
        LINHA_5 = 417

        button_positions = {
            
            'CE.png': (COLUNA_1, LINHA_1),
            'back.png': (COLUNA_2, LINHA_1),
            'porcento.png': (COLUNA_3, LINHA_1),
            'div.png': (COLUNA_4, LINHA_1),
            '7.png': (COLUNA_1, LINHA_2),
            
            '8.png': (COLUNA_2, LINHA_2),
            '9.png': (COLUNA_3, LINHA_2),
            'x.png': (COLUNA_4, LINHA_2),

            '4.png': (COLUNA_1, LINHA_3),
            '5.png': (COLUNA_2, LINHA_3),
            '6.png': (COLUNA_3, LINHA_3),
            '-.png': (COLUNA_4, LINHA_3),

            '1.png': (COLUNA_1, LINHA_4),
            '2.png': (COLUNA_2, LINHA_4),
            '3.png': (COLUNA_3, LINHA_4),
            '+.png': (COLUNA_4, LINHA_4),
            
            'exp.png': (COLUNA_1, LINHA_5),
            '0.png': (COLUNA_2, LINHA_5),
            'ponto.png': (COLUNA_3, LINHA_5),
            '=.png': (COLUNA_4, LINHA_5)
        }
        
        for img_file, (x, y) in button_positions.items():
            if img_file in self.botoes_interface:
                self.botoes_interface[img_file].place(x=x, y=y)

    def update_display(self):
        self.display_var.set(self.botoes_backend.get_string() or "0")

if __name__ == "__main__":
    root = tk.Tk()
    calc = CalculadoraInterface(root)
    root.mainloop()