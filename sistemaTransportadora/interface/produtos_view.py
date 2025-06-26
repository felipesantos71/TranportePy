"""
Nome do arquivo: produtos_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.produtos import Produtos

def abrir_tela_produtos():
    janela = Toplevel()
    janela.title("Cadastro de Produtos")
    janela.geometry("500x400")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Produtos", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    id_entry = Entry(frame, width=35)
    id_entry.grid(row=0, column=1, pady=5)
    descricao_entry = Entry(frame, width=35)
    descricao_entry.grid(row=1, column=1, pady=5)
    tipo_entry = Entry(frame, width=35)
    tipo_entry.grid(row=2, column=1, pady=5)
    quantidade_entry = Entry(frame, width=35)
    quantidade_entry.grid(row=3, column=1, pady=5)
    validade_entry = Entry(frame, width=35)
    validade_entry.grid(row=4, column=1, pady=5)
    observacoes_entry = Entry(frame, width=35)
    observacoes_entry.grid(row=5, column=1, pady=5)

    Label(frame, text="ID Produto:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
    Label(frame, text="Descrição:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
    Label(frame, text="Tipo:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
    Label(frame, text="Quantidade:", bg="#f0f0f0").grid(row=3, column=0, sticky="w")
    Label(frame, text="Validade:", bg="#f0f0f0").grid(row=4, column=0, sticky="w")
    Label(frame, text="Observações:", bg="#f0f0f0").grid(row=5, column=0, sticky="w")

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    # Funções CRUD
    def inserir_produto():
        produto = Produtos(
            id_produto=id_entry.get(),
            descricao=descricao_entry.get(),
            tipo=tipo_entry.get(),
            quantidade=quantidade_entry.get(),
            validade=validade_entry.get(),
            observacoes=observacoes_entry.get()
        )
        produto.inserir_produto()
        messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")

    def pesquisar_produto():
        id_produto = id_entry.get()
        produto = Produtos("", "", "", "", "", "")
        resultado = produto.buscar_produto(id_produto)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            descricao_entry.delete(0, END)
            descricao_entry.insert(0, dados[1])
            tipo_entry.delete(0, END)
            tipo_entry.insert(0, dados[2])
            quantidade_entry.delete(0, END)
            quantidade_entry.insert(0, dados[3])
            validade_entry.delete(0, END)
            validade_entry.insert(0, dados[4])
            observacoes_entry.delete(0, END)
            observacoes_entry.insert(0, dados[5])
        else:
            messagebox.showerror("Erro", "Produto não encontrado.")

    def alterar_produto():
        produto = Produtos(
            id_produto=id_entry.get(),
            descricao=descricao_entry.get(),
            tipo=tipo_entry.get(),
            quantidade=quantidade_entry.get(),
            validade=validade_entry.get(),
            observacoes=observacoes_entry.get()
        )
        produto.atualizar_produto(produto.id_produto)
        messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")

    def excluir_produto():
        produto = Produtos("", "", "", "", "", "")
        produto.excluir_produto(id_entry.get())
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=15, bg="#4CAF50", fg="white", height=2, command=inserir_produto).grid(row=0, column=0, padx=5)
    Button(frame_botoes, text="Pesquisar", width=15, bg="#2196F3", fg="white", height=2, command=pesquisar_produto).grid(row=0, column=1, padx=5)
    Button(frame_botoes, text="Alterar", width=15, bg="#FFA500", fg="white", height=2, command=alterar_produto).grid(row=1, column=0, padx=5, pady=10)
    Button(frame_botoes, text="Excluir", width=15, bg="#B22222", fg="white", height=2, command=excluir_produto).grid(row=1, column=1, padx=5, pady=10)
