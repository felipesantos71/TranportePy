"""
Nome do arquivo: fornecedores_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa, Caio Vinicius
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.fornecedor import Fornecedor

def abrir_tela_fornecedores():
    janela = Toplevel()
    janela.title("Cadastro de Fornecedores")
    janela.geometry("500x500")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Fornecedor", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    id_entry = Entry(frame, width=30)
    id_entry.grid(row=0, column=1, pady=5)
    cnpj_entry = Entry(frame, width=30)
    cnpj_entry.grid(row=1, column=1, pady=5)
    razao_entry = Entry(frame, width=30)
    razao_entry.grid(row=2, column=1, pady=5)
    fantasia_entry = Entry(frame, width=30)
    fantasia_entry.grid(row=3, column=1, pady=5)
    area_entry = Entry(frame, width=30)
    area_entry.grid(row=4, column=1, pady=5)
    contato_entry = Entry(frame, width=30)
    contato_entry.grid(row=5, column=1, pady=5)
    produtos_entry = Entry(frame, width=30)
    produtos_entry.grid(row=6, column=1, pady=5)

    Label(frame, text="ID Fornecedor:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Label(frame, text="CNPJ:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Label(frame, text="Razão Social:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Label(frame, text="Nome Fantasia:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Label(frame, text="Área de Atuação:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Label(frame, text="Contato (ID):", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Label(frame, text="Produtos (ID):", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    # Funções CRUD
    def inserir_fornecedor():
        fornecedor = Fornecedor(
            id_fornecedor=id_entry.get(),
            cnpj=cnpj_entry.get(),
            razao_social=razao_entry.get(),
            nome_fantasia=fantasia_entry.get(),
            area_atuacao=area_entry.get(),
            id_contato=contato_entry.get(),
            id_produtos=produtos_entry.get()
        )
        fornecedor.inserir_fornecedor()
        messagebox.showinfo("Sucesso", "Fornecedor inserido com sucesso!")

    def pesquisar_fornecedor():
        id_fornecedor = id_entry.get()
        fornecedor = Fornecedor("", "", "", "", "", "", "")
        resultado = fornecedor.buscar_fornecedor(id_fornecedor)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            cnpj_entry.delete(0, END)
            cnpj_entry.insert(0, dados[1])
            razao_entry.delete(0, END)
            razao_entry.insert(0, dados[2])
            fantasia_entry.delete(0, END)
            fantasia_entry.insert(0, dados[3])
            area_entry.delete(0, END)
            area_entry.insert(0, dados[4])
            contato_entry.delete(0, END)
            contato_entry.insert(0, dados[5])
            produtos_entry.delete(0, END)
            produtos_entry.insert(0, dados[6])
        else:
            messagebox.showerror("Erro", "Fornecedor não encontrado.")

    def alterar_fornecedor():
        fornecedor = Fornecedor(
            id_fornecedor=id_entry.get(),
            cnpj=cnpj_entry.get(),
            razao_social=razao_entry.get(),
            nome_fantasia=fantasia_entry.get(),
            area_atuacao=area_entry.get(),
            id_contato=contato_entry.get(),
            id_produtos=produtos_entry.get()
        )
        fornecedor.atualizar_fornecedor(fornecedor.id_fornecedor)
        messagebox.showinfo("Sucesso", "Fornecedor alterado com sucesso!")

    def excluir_fornecedor():
        fornecedor = Fornecedor("", "", "", "", "", "", "")
        fornecedor.excluir_fornecedor(id_entry.get())
        messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2, command=inserir_fornecedor).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2, command=pesquisar_fornecedor).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2, command=alterar_fornecedor).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2, command=excluir_fornecedor).grid(row=1, column=1, padx=10, pady=10)
