"""
Nome do arquivo: manutencao_view.py
Equipe: Fabrício Bomfim, Felipe Mateus, Igor Santos, Lucas Barbosa
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.manutencao import Manutencao

def abrir_tela_manutencao():
    janela = Toplevel()
    janela.title("Cadastro de Manutenção de Caminhões")
    janela.geometry("500x450")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    Label(janela, text="Cadastro de Manutenção", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)

    frame = Frame(janela, bg="#f0f0f0")
    frame.pack(pady=10)

    id_entry = Entry(frame, width=30)
    id_entry.grid(row=0, column=1, pady=5)
    ingresso_entry = Entry(frame, width=30)
    ingresso_entry.grid(row=1, column=1, pady=5)
    saida_entry = Entry(frame, width=30)
    saida_entry.grid(row=2, column=1, pady=5)
    caminhao_entry = Entry(frame, width=30)
    caminhao_entry.grid(row=3, column=1, pady=5)
    mecanico_entry = Entry(frame, width=30)
    mecanico_entry.grid(row=4, column=1, pady=5)
    servico_entry = Entry(frame, width=30)
    servico_entry.grid(row=5, column=1, pady=5)
    pecas_entry = Entry(frame, width=30)
    pecas_entry.grid(row=6, column=1, pady=5)

    Label(frame, text="ID Manutenção:", bg="#f0f0f0").grid(row=0, column=0, sticky="w", pady=5)
    Label(frame, text="Data de Ingresso:", bg="#f0f0f0").grid(row=1, column=0, sticky="w", pady=5)
    Label(frame, text="Data de Saída:", bg="#f0f0f0").grid(row=2, column=0, sticky="w", pady=5)
    Label(frame, text="Caminhão (ID/Placa):", bg="#f0f0f0").grid(row=3, column=0, sticky="w", pady=5)
    Label(frame, text="Mecânico Responsável:", bg="#f0f0f0").grid(row=4, column=0, sticky="w", pady=5)
    Label(frame, text="Serviço Realizado:", bg="#f0f0f0").grid(row=5, column=0, sticky="w", pady=5)
    Label(frame, text="Peças Utilizadas:", bg="#f0f0f0").grid(row=6, column=0, sticky="w", pady=5)

    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    # Funções CRUD
    def inserir_manutencao():
        manutencao = Manutencao(
            id_manutencao=id_entry.get(),
            data_ingresso=ingresso_entry.get(),
            data_saida=saida_entry.get(),
            id_caminhao=caminhao_entry.get(),
            id_funcionario=mecanico_entry.get(),
            servico=servico_entry.get(),
            id_produtos=pecas_entry.get()
        )
        manutencao.inserir_manutencao()
        messagebox.showinfo("Sucesso", "Manutenção inserida com sucesso!")

    def pesquisar_manutencao():
        id_manutencao = id_entry.get()
        manutencao = Manutencao("", "", "", "", "", "", "")
        resultado = manutencao.buscar_manutencao(id_manutencao)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            ingresso_entry.delete(0, END)
            ingresso_entry.insert(0, dados[1])
            saida_entry.delete(0, END)
            saida_entry.insert(0, dados[2])
            caminhao_entry.delete(0, END)
            caminhao_entry.insert(0, dados[3])
            mecanico_entry.delete(0, END)
            mecanico_entry.insert(0, dados[4])
            servico_entry.delete(0, END)
            servico_entry.insert(0, dados[5])
            pecas_entry.delete(0, END)
            pecas_entry.insert(0, dados[6])
        else:
            messagebox.showerror("Erro", "Manutenção não encontrada.")

    def alterar_manutencao():
        manutencao = Manutencao(
            id_manutencao=id_entry.get(),
            data_ingresso=ingresso_entry.get(),
            data_saida=saida_entry.get(),
            id_caminhao=caminhao_entry.get(),
            id_funcionario=mecanico_entry.get(),
            servico=servico_entry.get(),
            id_produtos=pecas_entry.get()
        )
        manutencao.atualizar_manutencao(manutencao.id_manutencao)
        messagebox.showinfo("Sucesso", "Manutenção alterada com sucesso!")

    def excluir_manutencao():
        manutencao = Manutencao("", "", "", "", "", "", "")
        manutencao.excluir_manutencao(id_entry.get())
        messagebox.showinfo("Sucesso", "Manutenção excluída com sucesso!")

    Button(frame_botoes, text="Inserir", width=20, bg="#4CAF50", fg="white", height=2, command=inserir_manutencao).grid(row=0, column=0, padx=10)
    Button(frame_botoes, text="Pesquisar", width=20, bg="#2196F3", fg="white", height=2, command=pesquisar_manutencao).grid(row=0, column=1, padx=10)
    Button(frame_botoes, text="Alterar", width=20, bg="#FFA500", fg="white", height=2, command=alterar_manutencao).grid(row=1, column=0, padx=10, pady=10)
    Button(frame_botoes, text="Excluir", width=20, bg="#B22222", fg="white", height=2, command=excluir_manutencao).grid(row=1, column=1, padx=10, pady=10)
