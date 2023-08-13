import tkinter as tk
from openpyxl import Workbook, load_workbook
from tkinter import messagebox


import pyrebase


import api_gmail


config = {
  "apiKey": "AIzaSyC9-RdrYzOB3tfuxaiQDS1RxlLQAnojFgI",
  "authDomain": "python-1c86a.firebaseapp.com",
  "databaseURL": "https://python-1c86a-default-rtdb.firebaseio.com",
  "pojectId": "python-1c86a",
  "storageBucket": "python-1c86a.appspot.com",
  "messagingSenderId": "48968104594",
  "appId": "1:48968104594:web:e24e04b38f44cb26ae044b"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()




def cadastrar_produto():
    nome = entry_nome.get()
    valor = float(entry_valor.get())
    categoria = entry_categoria.get()


    produtos.append({"Nome": nome, "Valor": valor, "Categoria": categoria})


    # Enviando e-mail
    assunto = "Novo Produto Adicionado"
    destinatario = "amandagracielly58@gmail.com"  # Coloque o seu e-mail aqui
    corpo_do_email = f"Um novo produto foi adicionado:\n\nNome: {nome}\nValor: R${valor:.2f}\nCategoria: {categoria}"
    try:
        api_gmail.enviar_email(assunto, destinatario, corpo_do_email)
        messagebox.showinfo("Sucesso", "Produto cadastrado e e-mail enviado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Produto cadastrado, mas houve um erro ao enviar o e-mail: {e}")


    # Limpando as entradas
    entry_nome.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
   


def exibir_produtos():
    resultado_text.delete(1.0, tk.END)
    for produto in produtos:
        resultado_text.insert(tk.END, f"Nome: {produto['Nome']}\n")
        resultado_text.insert(tk.END, f"Valor: R$ {produto['Valor']:.2f}\n")
        resultado_text.insert(tk.END, f"Categoria: {produto['Categoria']}\n")
        resultado_text.insert(tk.END, "----------------\n")


produtos = []
   


def salvar_produtos_no_firebase():
    try:
        for produto in produtos:
            db.child("produtos").push(produto)
       
        produtos.clear()
       
        messagebox.showinfo("Sucesso", "Dados salvos no Firebase!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar no Firebase: {str(e)}")
        
        
window = tk.Tk()
window.title("Cadastro de Produtos")
window.configure(bg="lightyellow")
window.geometry("300x500")

label_nome = tk.Label(window, text="Nome:", bg="lightyellow")
label_nome.pack()

entry_nome = tk.Entry(window)
entry_nome.pack()

label_valor = tk.Label(window, text="Valor:",bg="lightyellow")
label_valor.pack()

entry_valor = tk.Entry(window)
entry_valor.pack()

label_categoria = tk.Label(window, text="Categoria:",bg="lightyellow")
label_categoria.pack()

entry_categoria = tk.Entry(window)
entry_categoria.pack()

button_cadastrar = tk.Button(window, text="Cadastrar", command=cadastrar_produto)
button_cadastrar.pack(pady=8)

button_exibir = tk.Button(window, text="Exibir Produtos", command=exibir_produtos)
button_exibir.pack(pady=8)

resultado_text = tk.Text(window, height=10, width=30)
resultado_text.pack()

button_salvar_excel = tk.Button(window, text="Salvar Produtos no Firebase", command=salvar_produtos_no_firebase)
button_salvar_excel.pack(pady=8)

window.mainloop()
        
        
        
