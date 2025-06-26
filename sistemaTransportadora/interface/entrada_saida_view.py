"""
Nome do arquivo: entrada_saida_view.py
Equipe:  Fabrício Bomfim, Felipe Mateus, Igor Santos,  Lucas Barbosa, Caio Vinicius
Turma: DB - 91164
Semestre: 2025.1
"""

from tkinter import *
from tkinter import messagebox
from models.entrada_saida import Entrada_Saida

def abrir_tela_entrada_saida():
    janela = Toplevel()
    janela.title("Registro de Entrada/Saída de Caminhões")
    janela.geometry("700x400")
    janela.configure(bg="#f0f0f0")
    janela.resizable(False, False)

    frame_principal = Frame(janela, bg="#f0f0f0")
    frame_principal.pack(pady=10)

    # ======= ENTRADA ========
    frame_entrada = LabelFrame(frame_principal, text="Entrada", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#f0f0f0")
    frame_entrada.grid(row=0, column=0, padx=20, pady=10)

    id_entry = Entry(frame_entrada)
    id_entry.grid(row=0, column=1)
    Label(frame_entrada, text="ID Registro:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")

    data_entrada_entry = Entry(frame_entrada)
    data_entrada_entry.grid(row=1, column=1)
    Label(frame_entrada, text="Data Entrada:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")

    hora_entrada_entry = Entry(frame_entrada)
    hora_entrada_entry.grid(row=2, column=1)
    Label(frame_entrada, text="Hora Entrada:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")

    km_chegada_entry = Entry(frame_entrada)
    km_chegada_entry.grid(row=3, column=1)
    Label(frame_entrada, text="KM Chegada:", bg="#f0f0f0").grid(row=3, column=0, sticky="w")

    # ======= SAÍDA ========
    frame_saida = LabelFrame(frame_principal, text="Saída", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#f0f0f0")
    frame_saida.grid(row=0, column=1, padx=20, pady=10)

    data_saida_entry = Entry(frame_saida)
    data_saida_entry.grid(row=0, column=1)
    Label(frame_saida, text="Data Saída:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")

    hora_saida_entry = Entry(frame_saida)
    hora_saida_entry.grid(row=1, column=1)
    Label(frame_saida, text="Hora Saída:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")

    km_saida_entry = Entry(frame_saida)
    km_saida_entry.grid(row=2, column=1)
    Label(frame_saida, text="KM Saída:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")

    destino_entry = Entry(frame_saida)
    destino_entry.grid(row=3, column=1)
    Label(frame_saida, text="Destino:", bg="#f0f0f0").grid(row=3, column=0, sticky="w")

    roteiro_entry = Entry(frame_saida)
    roteiro_entry.grid(row=4, column=1)
    Label(frame_saida, text="Roteiro:", bg="#f0f0f0").grid(row=4, column=0, sticky="w")

    peso_entry = Entry(frame_saida)
    peso_entry.grid(row=5, column=1)
    Label(frame_saida, text="Peso (kg):", bg="#f0f0f0").grid(row=5, column=0, sticky="w")

    # ======= DADOS GERAIS ========
    frame_dados = LabelFrame(janela, text="Dados Complementares", font=("Arial", 12, "bold"), padx=10, pady=10, bg="#f0f0f0")
    frame_dados.pack(pady=10)

    caminhao_entry = Entry(frame_dados)
    caminhao_entry.grid(row=0, column=1)
    Label(frame_dados, text="Caminhão (ID/Placa):", bg="#f0f0f0").grid(row=0, column=0, sticky="w")

    motorista_entry = Entry(frame_dados)
    motorista_entry.grid(row=1, column=1)
    Label(frame_dados, text="Motorista (ID/Nome):", bg="#f0f0f0").grid(row=1, column=0, sticky="w")

    # ======= BOTÕES ========
    frame_botoes = Frame(janela, bg="#f0f0f0")
    frame_botoes.pack(pady=20)

    def inserir_entrada_saida():
        registro = Entrada_Saida(
            id_entrada_saida=id_entry.get(),
            data_entrada=data_entrada_entry.get(),
            data_saida=data_saida_entry.get(),
            hora_entrada=hora_entrada_entry.get(),
            hora_saida=hora_saida_entry.get(),
            destino=destino_entry.get(),
            roteiro=roteiro_entry.get(),
            peso=peso_entry.get(),
            km_saida=km_saida_entry.get(),
            km_chegada=km_chegada_entry.get(),
            id_caminhao=caminhao_entry.get(),
            id_funcionario=motorista_entry.get()
        )
        registro.inserir_entrada_saida()
        messagebox.showinfo("Sucesso", "Registro inserido com sucesso!")

    def pesquisar_entrada_saida():
        id_registro = id_entry.get()
        registro = Entrada_Saida("", "", "", "", "", "", "", "", "", "", "")
        resultado = registro.buscar_entrada_saida(id_registro)
        if resultado:
            dados = resultado.split(",")
            id_entry.delete(0, END)
            id_entry.insert(0, dados[0])
            data_entrada_entry.delete(0, END)
            data_entrada_entry.insert(0, dados[1])
            data_saida_entry.delete(0, END)
            data_saida_entry.insert(0, dados[2])
            hora_entrada_entry.delete(0, END)
            hora_entrada_entry.insert(0, dados[3])
            hora_saida_entry.delete(0, END)
            hora_saida_entry.insert(0, dados[4])
            destino_entry.delete(0, END)
            destino_entry.insert(0, dados[5])
            roteiro_entry.delete(0, END)
            roteiro_entry.insert(0, dados[6])
            peso_entry.delete(0, END)
            peso_entry.insert(0, dados[7])
            km_saida_entry.delete(0, END)
            km_saida_entry.insert(0, dados[8])
            km_chegada_entry.delete(0, END)
            km_chegada_entry.insert(0, dados[9])
            caminhao_entry.delete(0, END)
            caminhao_entry.insert(0, dados[10])
            motorista_entry.delete(0, END)
            motorista_entry.insert(0, dados[11])
        else:
            messagebox.showerror("Erro", "Registro não encontrado.")

    def alterar_entrada_saida():
        registro = Entrada_Saida(
            id_entrada_saida=id_entry.get(),
            data_entrada=data_entrada_entry.get(),
            data_saida=data_saida_entry.get(),
            hora_entrada=hora_entrada_entry.get(),
            hora_saida=hora_saida_entry.get(),
            destino=destino_entry.get(),
            roteiro=roteiro_entry.get(),
            peso=peso_entry.get(),
            km_saida=km_saida_entry.get(),
            km_chegada=km_chegada_entry.get(),
            id_caminhao=caminhao_entry.get(),
            id_funcionario=motorista_entry.get()
        )
        registro.atualizar_entrada_saida(registro.id_entrada_saida)
        messagebox.showinfo("Sucesso", "Registro alterado com sucesso!")

    def excluir_entrada_saida():
        registro = Entrada_Saida("", "", "", "", "", "", "", "", "", "", "")
        registro.excluir_entrada_saida(id_entry.get())
        messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")

    Button(frame_botoes, text="Inserir", width=12, bg="#4CAF50", fg="white", command=inserir_entrada_saida).grid(row=0, column=0, padx=5)
    Button(frame_botoes, text="Pesquisar", width=12, bg="#2196F3", fg="white", command=pesquisar_entrada_saida).grid(row=0, column=1, padx=5)
    Button(frame_botoes, text="Alterar", width=12, bg="#FFC107", fg="black", command=alterar_entrada_saida).grid(row=0, column=2, padx=5)
    Button(frame_botoes, text="Excluir", width=12, bg="#B22222", fg="white", command=excluir_entrada_saida).grid(row=0, column=3, padx=5)
