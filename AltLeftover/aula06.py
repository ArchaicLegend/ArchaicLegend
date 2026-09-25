import os
'''
Estrutura de Dados
'''

#Listas (array)
#Armazenamento por referência
list_a = [10, 20, 30] #lista pré-definida
list_b = list_a

print(list_a.__dir__)
print(list_b.__dir__)

#Declaração de lista
lista_vazia = [] #utilizando colchetes
lista_vazia_const = list() #utilizando construtor

lista_valores_number = [10, 5, 5.4]
lista_valores_string = ['a', 'b', 'João']
lista_valores_bool = [True, False, True]
lista_valores_list = [lista_valores_number, lista_valores_bool, lista_valores_string]

#Descobrindo o tamanho de uma lista
print(len(list_a))
print(len(lista_valores_list))

#Iterando uma lista
for i in lista_valores_string:
    print(i)

cont = 0
while cont < len(list_a):
    print(list_a[cont])
    cont += 1
os.system("cls") #limpar o terminal
#------------------------------------
#append(x) -> método para adicionar elementos na lista, sendo x o elemento para adicionar
lista_notas = list()

for i in range(5):
    lista_notas.append(float(input(f"{i+1}º Nota: ")))

#sum(x) -> retorna a soma do elementos do objeto iterável x
print(f"Média Final: {sum(lista_notas)/len(lista_notas):.2f}")

os.system("cls") #limpar o terminal
'''
Desafio 01: Crie um algoritmo que pergunte ao usuário quantas temperaturas serão lidas, 
posteriormente armazene essas temperaturas em uma lista e no final retorne a média,
a maior e menor temperatura registrada. Caso alguma temperatura ultrapasse 50° exiba
um alerta '❌ Temperatura Muito Alta' e registre quantas vezes foi registrado temperaturas
acima de 50°
'''
quant_temperatura  = int(input('Quantas temperaturas serão lidas? '))
list_temperatura = [] #list()
temp_acima_50 = 0

for i in range(quant_temperatura):
    list_temperatura.append(float(input(f"{i+1}º Temp.: ")))

    if list_temperatura[i] > 50:
        print('❌ Temperatura Muito Alta')
        temp_acima_50 += 1

print(f'Maior Temperatura: {max(list_temperatura)}°C')
print(f'Menor Temperatura: {min(list_temperatura)}°C')
print(f'Média Temperatura: {sum(list_temperatura)/len(list_temperatura):.1f}°C')
print(f'Acima de 50°C: {temp_acima_50} registros!')

#Demais Funções para Lista
#insert(index, element) - inseri um novo elemento(element) na posição de índice(index) informada

lista_aluno = ['Ana', 'João', 'Maria']

lista_aluno.insert(1, 'Mateus')

print(lista_aluno)

#pop(index) - remove um elemento da lista por índice(index), caso não seja passado nenhum valor, removerá o último

item_removido = lista_aluno.pop() 

print(lista_aluno)
print(f'Aluno Removido: {item_removido}')

#remove(element) - remove o primeiro elemento(element) correspondente

lista_aluno.remove('Mateus')
print(lista_aluno)

#count('element') - contar quantas ocorrências existem referente ao elemento(element) na lista
lista_aluno.append('Mateus')
lista_aluno.append('Mateus')

print(lista_aluno.count('Mateus'))

