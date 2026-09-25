vendas = [
    {"produto": "Mouse", "categoria": "Periféricos", "valor": 89.90, "qtd": 3},
    {"produto": "Teclado Mecânico", "categoria": "Periféricos", "valor": 249.90, "qtd": 2},
    {"produto": "Monitor 24\"", "categoria": "Monitores", "valor": 799.00, "qtd": 1},
    {"produto": "Notebook Gamer", "categoria": "Computadores", "valor": 4599.90, "qtd": 1},
    {"produto": "Fone Bluetooth", "categoria": "Áudio", "valor": 159.90, "qtd": 5},
    {"produto": "Cadeira Gamer", "categoria": "Móveis", "valor": 899.90, "qtd": 1},
    {"produto": "SSD 1TB", "categoria": "Armazenamento", "valor": 349.90, "qtd": 4},
    {"produto": "Webcam Full HD", "categoria": "Periféricos", "valor": 199.90, "qtd": 2},
    {"produto": "Mousepad Grande", "categoria": "Periféricos", "valor": 49.90, "qtd": 6},
    {"produto": "Hub USB-C", "categoria": "Acessórios", "valor": 89.00, "qtd": 3},
]

#Teacher

#Tarefa progressiva

#1. Calcular o total geral de vendas (soma acumulada).

def calcular_total(dataset):
    total = 0 

    for i in dataset:
        total += i["valor"] * i["qtd"]
    return total

#2. Calcular a quantidade total de registros.

#3. Calcular o total de vendas por categoria (acumulador com dicionário)

#4. Calcular a participação percentual de cada categoria 
# no total (conexão com a Aula 2).



