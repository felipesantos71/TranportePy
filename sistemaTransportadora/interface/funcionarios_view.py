"""
Nome do arquivo: funcionarios_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa, Caio Vinicius
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.funcionario import Funcionario

def abrir_tela_funcionarios():
    janela = Toplevel()
    janela.title("Cadastro de Funcionários")
    janela.geometry("380x500")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Funcionário", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    id_entry = Entry(frame, width=30)
    id_entry.grid(row=0, column=1, pady=5)
    nome_entry = Entry(frame, width=30)
    nome_entry.grid(row=1, column=1, pady=5)
    cpf_entry = Entry(frame, width=30)
    cpf_entry.grid(row=2, column=1, pady=5)
    cargo_entry = Entry(frame, width=30)
    cargo_entry.grid(row=3, column=1, pady=5)
    nascimento_entry = Entry(frame, width=30)
    nascimento_entry.grid(row=4, column=1, pady=5)
    endereco_entry = Entry(frame, width=30)
    endereco_entry.grid(row=5, column=1, pady=5)
    contato_entry = Entry(frame, width=30)
    contato_entry.grid(row=6, column=1, pady=5)

    Label(frame, text="ID Funcionário:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Label(frame, text="Nome:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Label(frame, text="CPF:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Label(frame, text="Cargo:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Label(frame, text="Data de Nascimento:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Label(frame, text="ID Endereço:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Label(frame, text="ID Contato:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    # Funções CRUD
    def inserir_funcionario():
        funcionario = Funcionario(
            id_funcionario=id_entry.get(),
            nome=nome_entry.get(),
            cpf=cpf_entry.get(),
            cargo=cargo_entry.get(),
            dta_nascimento=nascimento_entry.get(),
            id_endereco=endereco_entry.get(),
            id_contato=contato_entry.get()
        )
        funcionario.inserir_funcionario()
        messagebox.showinfo("Sucesso", "Funcionário inserido com sucesso!")

    def pesquisar_funcionario():
        id_funcionario = id_entry.get()
        funcionario = Funcionario("", "", "", "", "", "", "")
        resultado = funcionario.buscar_funcionario(id_funcionario)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            nome_entry.delete(0, END)
            nome_entry.insert(0, dados[1])
            cpf_entry.delete(0, END)
            cpf_entry.insert(0, dados[2])
            cargo_entry.delete(0, END)
            cargo_entry.insert(0, dados[3])
            nascimento_entry.delete(0, END)
            nascimento_entry.insert(0, dados[4])
            endereco_entry.delete(0, END)
            endereco_entry.insert(0, dados[5])
            contato_entry.delete(0, END)
            contato_entry.insert(0, dados[6])
        else:
            messagebox.showerror("Erro", "Funcionário não encontrado.")

    def alterar_funcionario():
        funcionario = Funcionario(
            id_funcionario=id_entry.get(),
            nome=nome_entry.get(),
            cpf=cpf_entry.get(),
            cargo=cargo_entry.get(),
            dta_nascimento=nascimento_entry.get(),
            id_endereco=endereco_entry.get(),
            id_contato=contato_entry.get()
        )
        funcionario.atualizar_funcionario(funcionario.id_funcionario)
        messagebox.showinfo("Sucesso", "Funcionário alterado com sucesso!")

    def excluir_funcionario():
        funcionario = Funcionario("", "", "", "", "", "", "")
        funcionario.excluir_funcionario(id_entry.get())
        messagebox.showinfo("Sucesso", "Funcionário excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2, command=inserir_funcionario).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2, command=pesquisar_funcionario).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2, command=alterar_funcionario).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2, command=excluir_funcionario).grid(row=1, column=1, padx=10, pady=10)
