"""
Nome do arquivo: caminhao.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício, Caio Vinicius
Turma: 91164
Semestre: 2025.1
"""

class Caminhao:
    def __init__(self, id_caminhao, renavan, modelo, marca, cor, placa, chassi, status, tipo, peso):
        self.id_caminhao = id_caminhao
        self.renavan = renavan
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.placa = placa
        self.chassi = chassi
        self.status = status
        self.tipo = tipo
        self.peso = peso
        self.caminho_arquivo = "data/caminhao.txt"

    def __str__(self):
        return (f"ID: {self.id_caminhao}, Renavan: {self.renavan}, Modelo: {self.modelo}, Marca: {self.marca}, "
                f"Cor: {self.cor}, Placa: {self.placa}, Chassi: {self.chassi}, Status: {self.status}, "
                f"Tipo: {self.tipo}, Peso: {self.peso}")

    def to_line(self):
        return (f"{self.id_caminhao},{self.renavan},{self.modelo},{self.marca},{self.cor},"
                f"{self.placa},{self.chassi},{self.status},{self.tipo},{self.peso}\n")

    # CRUD

    # Create
    def inserir_caminhao(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    # Read
    def buscar_caminhao(self, id_caminhao):
        try:
            with open(self.caminho_arquivo, "r") as arquivo:
                for linha in arquivo:
                    if linha.startswith(f"{id_caminhao},"):
                        return linha.strip()
        except FileNotFoundError:
            return None
        return None

    # Update
    def atualizar_caminhao(self, id_caminhao):
        caminhoes = self.listar_caminhoes()
        with open(self.caminho_arquivo, "w") as arquivo:
            for caminhao in caminhoes:
                if caminhao.startswith(f"{id_caminhao},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(caminhao)

    # Delete
    def excluir_caminhao(self, id_caminhao):
        caminhoes = self.listar_caminhoes()
        with open(self.caminho_arquivo, "w") as arquivo:
            for caminhao in caminhoes:
                if not caminhao.startswith(f"{id_caminhao},"):
                    arquivo.write(caminhao)

    # Listar todos
    def listar_caminhoes(self):
        try:
            with open(self.caminho_arquivo, "r") as arquivo:
                return arquivo.readlines()
        except FileNotFoundError:
            return []