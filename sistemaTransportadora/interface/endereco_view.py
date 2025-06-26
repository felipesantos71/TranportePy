"""
Nome do arquivo: endereco_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa, Caio Vinicius
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.endereco import Endereco

def abrir_tela_enderecos():
    janela = Toplevel()
    janela.title("Cadastro de Endereços")
    janela.geometry("400x400")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Endereço", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    id_entry = Entry(frame, width=30)
    id_entry.grid(row=0, column=1, pady=5)
    rua_entry = Entry(frame, width=30)
    rua_entry.grid(row=1, column=1, pady=5)
    numero_entry = Entry(frame, width=30)
    numero_entry.grid(row=2, column=1, pady=5)
    bairro_entry = Entry(frame, width=30)
    bairro_entry.grid(row=3, column=1, pady=5)
    cidade_entry = Entry(frame, width=30)
    cidade_entry.grid(row=4, column=1, pady=5)
    estado_entry = Entry(frame, width=30)
    estado_entry.grid(row=5, column=1, pady=5)
    cep_entry = Entry(frame, width=30)
    cep_entry.grid(row=6, column=1, pady=5)

    Label(frame, text="ID Endereço:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Label(frame, text="Rua:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Label(frame, text="Número:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Label(frame, text="Bairro:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Label(frame, text="Cidade:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Label(frame, text="Estado:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Label(frame, text="CEP:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    # Funções CRUD
    def inserir_endereco():
        endereco = Endereco(
            id_endereco=id_entry.get(),
            rua=rua_entry.get(),
            numero=numero_entry.get(),
            bairro=bairro_entry.get(),
            cidade=cidade_entry.get(),
            estado=estado_entry.get(),
            cep=cep_entry.get()
        )
        endereco.inserir_endereco()
        messagebox.showinfo("Sucesso", "Endereço inserido com sucesso!")

    def pesquisar_endereco():
        id_endereco = id_entry.get()
        endereco = Endereco("", "", "", "", "", "", "")
        resultado = endereco.buscar_endereco(id_endereco)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            rua_entry.delete(0, END)
            rua_entry.insert(0, dados[1])
            numero_entry.delete(0, END)
            numero_entry.insert(0, dados[2])
            bairro_entry.delete(0, END)
            bairro_entry.insert(0, dados[3])
            cidade_entry.delete(0, END)
            cidade_entry.insert(0, dados[4])
            estado_entry.delete(0, END)
            estado_entry.insert(0, dados[5])
            cep_entry.delete(0, END)
            cep_entry.insert(0, dados[6])
        else:
            messagebox.showerror("Erro", "Endereço não encontrado.")

    def alterar_endereco():
        endereco = Endereco(
            id_endereco=id_entry.get(),
            rua=rua_entry.get(),
            numero=numero_entry.get(),
            bairro=bairro_entry.get(),
            cidade=cidade_entry.get(),
            estado=estado_entry.get(),
            cep=cep_entry.get()
        )
        endereco.atualizar_endereco(endereco.id_endereco)
        messagebox.showinfo("Sucesso", "Endereço alterado com sucesso!")

    def excluir_endereco():
        endereco = Endereco("", "", "", "", "", "", "")
        endereco.excluir_endereco(id_entry.get())
        messagebox.showinfo("Sucesso", "Endereço excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2, command=inserir_endereco).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2, command=pesquisar_endereco).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2, command=alterar_endereco).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2, command=excluir_endereco).grid(row=1, column=1, padx=10, pady=10)
