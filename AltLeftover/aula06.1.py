'''
Função Enumerate
'''
salarios = [1005.45, 800, 6500.49, 4500, 2500.45]

for i in enumerate(salarios):
    print(i)

#desempacotamento
for i, e in enumerate(salarios):
    print(f'Index: [{i}] | Elemento: [{e}]')

# Lista de listas
turma_dados = [
    [4.5, 8, 10],
    [0, 5, 10],
    [2, 4, 4.5],
    [6.5, 6.5, 8],
    [10, 10, 10]
]

for index, element  in enumerate(turma_dados):
    txt = f"Aluno {index+1}: "

    for j in element:
        txt += f"{float(j):^7}"

    media = sum(element)/len(element)
    print(txt + f'| Média Final: {media:.2f}')

#Organização de textos com f-string
'''
^ -> centralizar texto
< -> alinhar texto à esquerda
> -> alinhar texto à direita

Ex. 
print(f'{texto:^5}') centraliza o texto e distribui os espaços dos dois lados
print(f'{texto:<5}') alinha o texto à esquerda
print(f'{texto:>5}') alinha o texto à direita
'''

alunos_dados = ['Francisco', 'Antonio', 'Maria', 'John', 'Karl', 'Ana', 'Samanta']

turma_dados = [
    [4.5, 8, 10],
    [0, 5, 10],
    [2, 4, 4.5],
    [6.5, 6.5, 8],
    [10, 10, 10],
    [4, 6, 8],
    [2.5, 4.5, 7.9]
]

media = 0

for index, row in enumerate(turma_dados):
    txt = f"{alunos_dados[index]}: "

    for column in row:
        txt += f"{float(column):^7}"
        
    media = sum(row)/len(row)
    print(txt + f'| Média Final: {media:.2f}')