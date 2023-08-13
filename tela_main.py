import tkinter as tk
import subprocess
from PIL import Image, ImageTk


def abrir_cadastro_cliente():
    subprocess.run (["python", "cadastro_cliente.py"])


def abrir_cadastro_produto():
    subprocess.run(["python", "cadastro_produto.py"])


# criação da janela

window = tk.Tk()
window.configure(bg="white")
window.title ("Menu Loja")
window.geometry ("400x300")


image = Image.open("logo.png")
foto = ImageTk.PhotoImage(image)


label_imagem = tk.Label(window, image=foto)
label_imagem.pack()


botao_clientes = tk.Button(window, text = "Cadastro de Clientes", command=abrir_cadastro_cliente)
botao_clientes.pack(pady=14)


botao_produto = tk.Button (window,text="Cadastro de Produto", command=abrir_cadastro_produto)
botao_produto.pack()

window.mainloop()
