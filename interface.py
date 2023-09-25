import tkinter as tk

root = tk.Tk()


label = tk.Label(root, text="Olá, mundo!")
label.pack()

button = tk.Button(root, text="Clique aqui")
button.pack()

def button_click():
    label.configure(text="Botão clicado!")

button.configure(command=button_click)
root.mainloop()