import os

arquivos = [
    "data/cliente.txt",
    "data/funcionario.txt",
    "data/produtos.txt",
    "data/fornecedor.txt",
    "data/endereco.txt",
    "data/contato.txt",
    "data/manutencao.txt",
    "data/caminhao.txt",
    "data/entrada.saida.txt"
]

for arquivo in arquivos:
    if not os.path.exists(arquivo):
        open(arquivo, "w").close()
        print(f"Arquivo criado: {arquivo}")
    else:
        print(f"Arquivo já existe: {arquivo}")