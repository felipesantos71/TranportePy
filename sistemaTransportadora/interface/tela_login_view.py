"""
Nome do arquivo: tela_login_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa, Caio Vinicius
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
import os
from interface.tela_cadastro import abrir_tela_cadastro
from interface.menu_inicial import abrir_menu_inicial  # menu_inicial.py deve ter a função abrir_menu_inicial(tipo_usuario)

ARQUIVO_USUARIOS = "data/usuarios.txt"

def verificar_credenciais(usuario, senha):
    print(f"Tentando login: '{usuario}' senha: '{senha}'")
    if not os.path.exists(ARQUIVO_USUARIOS):
        print("Arquivo de usuários não encontrado!")
        return None
    with open(ARQUIVO_USUARIOS, "r") as arquivo:
        for linha in arquivo:
            print(f"Linha lida: '{linha.strip()}'")
            dados = linha.strip().split(";")
            print(f"Dados splitados: {dados}")
            if len(dados) == 3 and usuario == dados[0] and senha == dados[1]:
                print("Login OK!")
                return dados[2]
    print("Login inválido!")
    return None

def abrir_tela_login():
    def realizar_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()

        tipo_usuario = verificar_credenciais(usuario, senha)
        if tipo_usuario:
            messagebox.showinfo("Login", f"Login realizado como {tipo_usuario}!")
            login.destroy()
            abrir_menu_inicial(tipo_usuario)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    def abrir_cadastro():
        login.destroy()
        abrir_tela_cadastro()

    login = Tk()
    login.title("Login - TransportGuard")
    login.geometry("350x250")
    login.configure(bg="#f4f4f4")

    Label(login, text="Login do Sistema", font=("Arial", 16, "bold"), bg="#f4f4f4").pack(pady=10)

    Label(login, text="Usuário (e-mail):", bg="#f4f4f4").pack()
    entrada_usuario = Entry(login, width=30)
    entrada_usuario.pack(pady=5)

    Label(login, text="Senha:", bg="#f4f4f4").pack()
    entrada_senha = Entry(login, show="*", width=30)
    entrada_senha.pack(pady=5)

    Button(login, text="Entrar", width=25, bg="#4682B4", fg="white", command=realizar_login).pack(pady=10)
    Button(login, text="Cadastrar", width=25, command=abrir_cadastro).pack()

    login.mainloop()


if __name__ == "__main__":
    abrir_tela_login()
