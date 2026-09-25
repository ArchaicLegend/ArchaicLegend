''' Funções '''

#Declarando uma função
def somar():
    return 10 + 10

#Invocando uma função
var = somar() # o valor 20 será armazenado em var

print(somar())
print(var)
print(somar() * 10)

#Declarando uma função com parâmetros
def subtrair(valor_1, valor_2):
    try:
        return valor_1 - valor_2
    except:
        return 'Valores Inválidos!'

#Invocando a função passando os argumentos
print(subtrair(100, 2))
print(subtrair("2", 100))

# Prática Rápida
'''
Escreva uma função que receba a base e a altura de um triângulo
e retorne sua área (A = (base x altura) / 2).
'''

def area(base, altura):
    return (base * altura) / 2


in_base = int(input('Digite a base: '))
in_altura = int(input('Digite a altura: '))
print(f'Área do Triângulo: {area(in_base, in_altura)}')

print(f'Área do Triângulo: {area(10, 15)}')

print(f'Área do Triângulo: {area(int(input('Digite a base: ')), int(input('Digite a altura: ')))}')

'''
Escreva uma função que receba uma lista e um número para ser pesquisado na lista.
Se o número existir na lista retorne a(as) posição(ões) do número na lista.
Se o número não existir retorne 'Valor não encontrado!'
'''

def pesquisar_lista(lista, numero):
    list_index = []
    for index, value in enumerate(lista):
        if value == numero:
            list_index.append(index)

    if len(list_index) > 0:
        return list_index

    return 'Valor não encontrado!'

list_ex = [5, 1, -10, 5, 2]
print(pesquisar_lista(list_ex, 5))