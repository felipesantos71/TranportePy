"""
Nome do arquivo: endereco.py
Equipe: Felipe, Igor, Lucas Barbosa e Fabrício
Turma: 91164
Semestre: 2025.1
"""

class Endereco:
    def __init__(self, id_endereco, rua, numero, bairro, cidade, estado, cep):
        self.id_endereco = id_endereco
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.caminho_arquivo = "data/endereco.txt"

    def __str__(self):
        return (f"ID: {self.id_endereco}, Rua: {self.rua}, Número: {self.numero}, Bairro: {self.bairro}, "
                f"Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")

    def to_line(self):
        return f"{self.id_endereco},{self.rua},{self.numero},{self.bairro},{self.cidade},{self.estado},{self.cep}\n"

    # CRUD

    # Create
    def inserir_endereco(self):
        with open(self.caminho_arquivo, "a") as arquivo:
            arquivo.write(self.to_line())

    # Read
    def buscar_endereco(self, id_endereco):
        try:
            with open(self.caminho_arquivo, "r") as arquivo:
                for linha in arquivo:
                    if linha.startswith(f"{id_endereco},"):
                        return linha.strip()
        except FileNotFoundError:
            return None
        return None

    # Update
    def atualizar_endereco(self, id_endereco):
        enderecos = self.listar_enderecos()
        with open(self.caminho_arquivo, "w") as arquivo:
            for endereco in enderecos:
                if endereco.startswith(f"{id_endereco},"):
                    arquivo.write(self.to_line())
                else:
                    arquivo.write(endereco)

    # Delete
    def excluir_endereco(self, id_endereco):
        enderecos = self.listar_enderecos()
        with open(self.caminho_arquivo, "w") as arquivo:
            for endereco in enderecos:
                if not endereco.startswith(f"{id_endereco},"):
                    arquivo.write(endereco)

    # Listar todos
    def listar_enderecos(self):
        try:
            with open(self.caminho_arquivo, "r") as arquivo:
                return arquivo.readlines()
        except FileNotFoundError:
            return []


