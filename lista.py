import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultado = cursor.fetchall()
for registro in resultado:
    print(f"nome: {registro [0]}\ntelefone{registro[1]}")
cursor.close()
conexao.close()

import tkinter as tk

def salvar_dados():
    # Função para salvar os dados no banco de dados
    pass

# Criar janela
root = tk.Tk()
root.title("Minha Interface")

# Adicionar um botão
button = tk.Button(root, text="Salvar Dados", command=salvar_dados)
button.pack()

# Rodar o loop principal
root.mainloop()
