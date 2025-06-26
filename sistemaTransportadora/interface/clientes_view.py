### ✅ Nome do arquivo: `clientes.py`


"""
Nome do arquivo: clientes_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.cliente import Cliente

def abrir_clientes():
    janela = Toplevel()
    janela.title("Cadastro de Clientes")
    janela.geometry("500x560")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Cliente", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    # Entrys em variáveis para acessar nos comandos dos botões
    id_entry = Entry(frame, width=35)
    id_entry.grid(row=0, column=1, pady=5)
    tipo_entry = Entry(frame, width=35)
    tipo_entry.grid(row=1, column=1, pady=5)
    data_saida_entry = Entry(frame, width=35)
    data_saida_entry.grid(row=2, column=1, pady=5)
    nome_entry = Entry(frame, width=35)
    nome_entry.grid(row=3, column=1, pady=5)
    cpf_entry = Entry(frame, width=35)
    cpf_entry.grid(row=4, column=1, pady=5)
    cnpj_entry = Entry(frame, width=35)
    cnpj_entry.grid(row=5, column=1, pady=5)
    obs_entry = Entry(frame, width=35)
    obs_entry.grid(row=6, column=1, pady=5)
    endereco_entry = Entry(frame, width=35)
    endereco_entry.grid(row=7, column=1, pady=5)
    motorista_entry = Entry(frame, width=35)
    motorista_entry.grid(row=8, column=1, pady=5)
    contato_entry = Entry(frame, width=35)
    contato_entry.grid(row=9, column=1, pady=5)

    # Labels
    Label(frame, text="ID Cliente:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Label(frame, text="Tipo:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Label(frame, text="Data Saída:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Label(frame, text="Nome:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Label(frame, text="CPF:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Label(frame, text="CNPJ:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Label(frame, text="Observações:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)
    Label(frame, text="Endereço (ID):", bg="#f0f0f0").grid(row=7, column=0, sticky="w", pady=5)
    Label(frame, text="Motorista (ID Funcionário):", bg="#f0f0f0").grid(row=8, column=0, sticky="w", pady=5)
    Label(frame, text="Contato (ID):", bg="#f0f0f0").grid(row=9, column=0, sticky="w", pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=30)

    # Funções CRUD
    def inserir_cliente():
        cliente = Cliente(
            id_cliente=id_entry.get(),
            tipo=tipo_entry.get(),
            nome=nome_entry.get(),
            cpf=cpf_entry.get(),
            cnpj=cnpj_entry.get(),
            observacoes=obs_entry.get(),
            id_endereco=endereco_entry.get(),
            id_contato=contato_entry.get()
        )
        cliente.inserir_cliente()
        messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")

    def pesquisar_cliente():
        id_cliente = id_entry.get()
        cliente = Cliente("", "", "", "", "", "", "", "")
        resultado = cliente.buscar_cliente(id_cliente)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            tipo_entry.delete(0, END)
            tipo_entry.insert(0, dados[1])
            nome_entry.delete(0, END)
            nome_entry.insert(0, dados[2])
            cpf_entry.delete(0, END)
            cpf_entry.insert(0, dados[3])
            cnpj_entry.delete(0, END)
            cnpj_entry.insert(0, dados[4])
            obs_entry.delete(0, END)
            obs_entry.insert(0, dados[5])
            endereco_entry.delete(0, END)
            endereco_entry.insert(0, dados[6])
            contato_entry.delete(0, END)
            contato_entry.insert(0, dados[7])
        else:
            messagebox.showerror("Erro", "Cliente não encontrado.")

    def alterar_cliente():
        cliente = Cliente(
            id_cliente=id_entry.get(),
            tipo=tipo_entry.get(),
            nome=nome_entry.get(),
            cpf=cpf_entry.get(),
            cnpj=cnpj_entry.get(),
            observacoes=obs_entry.get(),
            id_endereco=endereco_entry.get(),
            id_contato=contato_entry.get()
        )
        cliente.atualizar_cliente(cliente.id_cliente)
        messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")

    def excluir_cliente():
        cliente = Cliente("", "", "", "", "", "", "", "")
        cliente.excluir_cliente(id_entry.get())
        messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2, command=inserir_cliente).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2, command=pesquisar_cliente).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2, command=alterar_cliente).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2, command=excluir_cliente).grid(row=1, column=1, padx=10, pady=10)

