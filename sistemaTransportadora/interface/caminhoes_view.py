"""
Nome do arquivo: caminhoes_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.caminhao import Caminhao

def abrir_tela_caminhoes():
    janela = Toplevel()
    janela.title("Cadastro de Caminhões")
    janela.geometry("400x550")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Caminhão", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    id_entry = Entry(frame, width=30)
    id_entry.grid(row=0, column=1, pady=5)
    renavan_entry = Entry(frame, width=30)
    renavan_entry.grid(row=1, column=1, pady=5)
    modelo_entry = Entry(frame, width=30)
    modelo_entry.grid(row=2, column=1, pady=5)
    marca_entry = Entry(frame, width=30)
    marca_entry.grid(row=3, column=1, pady=5)
    cor_entry = Entry(frame, width=30)
    cor_entry.grid(row=4, column=1, pady=5)
    placa_entry = Entry(frame, width=30)
    placa_entry.grid(row=5, column=1, pady=5)
    chassi_entry = Entry(frame, width=30)
    chassi_entry.grid(row=6, column=1, pady=5)
    status_entry = Entry(frame, width=30)
    status_entry.grid(row=7, column=1, pady=5)
    tipo_entry = Entry(frame, width=30)
    tipo_entry.grid(row=8, column=1, pady=5)
    peso_entry = Entry(frame, width=30)
    peso_entry.grid(row=9, column=1, pady=5)

    Label(frame, text="ID Caminhão:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Label(frame, text="Renavan:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Label(frame, text="Modelo:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Label(frame, text="Marca:", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Label(frame, text="Cor:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Label(frame, text="Placa:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Label(frame, text="Chassi:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)
    Label(frame, text="Status:", bg="#f0f0f0").grid(row=7, column=0, sticky="w", pady=5)
    Label(frame, text="Tipo:", bg="#f0f0f0").grid(row=8, column=0, sticky="w", pady=5)
    Label(frame, text="Peso (kg):", bg="#f0f0f0").grid(row=9, column=0, sticky="w", pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    # Funções CRUD
    def inserir_caminhao():
        caminhao = Caminhao(
            id_caminhao=id_entry.get(),
            renavan=renavan_entry.get(),
            modelo=modelo_entry.get(),
            marca=marca_entry.get(),
            cor=cor_entry.get(),
            placa=placa_entry.get(),
            chassi=chassi_entry.get(),
            status=status_entry.get(),
            tipo=tipo_entry.get(),
            peso=peso_entry.get()
        )
        caminhao.inserir_caminhao()
        messagebox.showinfo("Sucesso", "Caminhão inserido com sucesso!")

    def pesquisar_caminhao():
        id_caminhao = id_entry.get()
        caminhao = Caminhao("", "", "", "", "", "", "", "", "", "")
        resultado = caminhao.buscar_caminhao(id_caminhao)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            renavan_entry.delete(0, END)
            renavan_entry.insert(0, dados[1])
            modelo_entry.delete(0, END)
            modelo_entry.insert(0, dados[2])
            marca_entry.delete(0, END)
            marca_entry.insert(0, dados[3])
            cor_entry.delete(0, END)
            cor_entry.insert(0, dados[4])
            placa_entry.delete(0, END)
            placa_entry.insert(0, dados[5])
            chassi_entry.delete(0, END)
            chassi_entry.insert(0, dados[6])
            status_entry.delete(0, END)
            status_entry.insert(0, dados[7])
            tipo_entry.delete(0, END)
            tipo_entry.insert(0, dados[8])
            peso_entry.delete(0, END)
            peso_entry.insert(0, dados[9])
        else:
            messagebox.showerror("Erro", "Caminhão não encontrado.")

    def alterar_caminhao():
        caminhao = Caminhao(
            id_caminhao=id_entry.get(),
            renavan=renavan_entry.get(),
            modelo=modelo_entry.get(),
            marca=marca_entry.get(),
            cor=cor_entry.get(),
            placa=placa_entry.get(),
            chassi=chassi_entry.get(),
            status=status_entry.get(),
            tipo=tipo_entry.get(),
            peso=peso_entry.get()
        )
        caminhao.atualizar_caminhao(caminhao.id_caminhao)
        messagebox.showinfo("Sucesso", "Caminhão alterado com sucesso!")

    def excluir_caminhao():
        caminhao = Caminhao("", "", "", "", "", "", "", "", "", "")
        caminhao.excluir_caminhao(id_entry.get())
        messagebox.showinfo("Sucesso", "Caminhão excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2, command=inserir_caminhao).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2, command=pesquisar_caminhao).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2, command=alterar_caminhao).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2, command=excluir_caminhao).grid(row=1, column=1, padx=10, pady=10)
