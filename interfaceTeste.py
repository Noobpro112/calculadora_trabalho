import tkinter as tk
from tkinter import *

root = tk.Tk()
canvas = Canvas(root)
canvas.pack()

class Calculadora:
    def __init__(self):
        self.root = root
        self.interface()
        self.desenhar_retangulo(30.5, 18.8, 30.5 + 257.5, 18.8 + 96, radius=15, fill="#AA125F")

    def interface(self):
        root.title('Calculadora')
        root.geometry('320x480')
        root.resizable(False, False)
        root.configure(background='#DE2861')

    def desenhar_retangulo(self, x1, y1, x2, y2, radius=0, **kwargs):
        # Calcular as coordenadas dos cantos arredondados
        p1 = [x1 + radius, y1]
        p2 = [x1 + radius, y1]
        p3 = [x2 - radius, y1]
        p4 = [x2 - radius, y1]
        p5 = [x2, y1]
        p6 = [x2, y1 + radius]
        p7 = [x2, y2 - radius]
        p8 = [x2, y2 - radius]
        p9 = [x2, y2]
        p10 = [x2 - radius, y2]
        p11 = [x2 - radius, y2]
        p12 = [x1 + radius, y2]
        p13 = [x1 + radius, y2]
        p14 = [x1, y2]
        p15 = [x1, y2 - radius]
        p16 = [x1, y2 - radius]
        p17 = [x1, y1 + radius]
        p18 = [x1, y1 + radius]
        p19 = [x1, y1]

        points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19]

        # Converter as coordenadas em uma lista plana
        flat_points = [coord for point in points for coord in point]

        return canvas.create_polygon(flat_points, **kwargs, smooth=True)

Calculadora()
root.mainloop()
