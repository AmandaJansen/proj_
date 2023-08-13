import tkinter as tk
import pandas as pd
from tkinter import  messagebox
import importlib  


import pyrebase


config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "",
  "pojectId": "",
  "storageBucket": "",
  "messagingSenderId": "",
  "appId": ""
}


firebase = pyrebase.initialize_app(config)
auth = firebase.database()


def validate_login():
    username = username_entry.get()
    password = password_entry.get()


    db = firebase.database()


    users = db.child("clientes").get().val()  # Obter todos os usuários
    for user in users.values():
        if user['Usuario'] == username and user['Senha'] == password:
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            window.destroy()  # Fecha a janela de login
            telaPrincipal = importlib.import_module('telaPrincipal')  # Importa telaPrincipal somente depois de um login bem-sucedido
            telaPrincipal.show_main_screen()  # Abre a tela principal
            break
    else:
        messagebox.showerror("Erro", "Usuário não encontrado ou senha incorreta.")# Cria a janela de login
window = tk.Tk()
window.title("Login")
window.geometry('300x200')


username_label = tk.Label(window, text='Usuário:')
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()


password_label = tk.Label(window, text='Senha:')
password_label.pack()
password_entry = tk.Entry(window, show='*')
password_entry.pack()


submit_button = tk.Button(window, text='Login', command=validate_login)
submit_button.pack()


