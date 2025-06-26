"""
Nome do arquivo: contato_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa, Caio Vinicius
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.contato import Contato

def abrir_tela_contatos():
    janela = Toplevel()
    janela.title("Cadastro de Contatos")
    janela.geometry("400x350")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Contato", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    id_entry = Entry(frame, width=30)
    id_entry.grid(row=0, column=1, pady=5)
    telefone_entry = Entry(frame, width=30)
    telefone_entry.grid(row=1, column=1, pady=5)
    email_entry = Entry(frame, width=30)
    email_entry.grid(row=2, column=1, pady=5)

    Label(frame, text="ID Contato:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Label(frame, text="Telefone:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Label(frame, text="E-mail:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    # Funções CRUD
    def inserir_contato():
        contato = Contato(
            id_contato=id_entry.get(),
            telefone=telefone_entry.get(),
            email=email_entry.get()
        )
        contato.inserir_contato()
        messagebox.showinfo("Sucesso", "Contato inserido com sucesso!")

    def pesquisar_contato():
        id_contato = id_entry.get()
        contato = Contato("", "", "")
        resultado = contato.buscar_contato(id_contato)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            telefone_entry.delete(0, END)
            telefone_entry.insert(0, dados[1])
            email_entry.delete(0, END)
            email_entry.insert(0, dados[2])
        else:
            messagebox.showerror("Erro", "Contato não encontrado.")

    def alterar_contato():
        contato = Contato(
            id_contato=id_entry.get(),
            telefone=telefone_entry.get(),
            email=email_entry.get()
        )
        contato.atualizar_contato(contato.id_contato)
        messagebox.showinfo("Sucesso", "Contato alterado com sucesso!")

    def excluir_contato():
        contato = Contato("", "", "")
        contato.excluir_contato(id_entry.get())
        messagebox.showinfo("Sucesso", "Contato excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2, command=inserir_contato).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2, command=pesquisar_contato).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2, command=alterar_contato).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2, command=excluir_contato).grid(row=1, column=1, padx=10, pady=10)
