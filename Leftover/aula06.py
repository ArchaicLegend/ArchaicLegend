'''
Estrutura de Dados
'''
'''
Index = Posição -1
Posição = Index +1
'''

#Listas (array)
#Armazenamento por referência
'''
list_a = [10,20,30] #Lista pré-definida
list_b = list_a

print(list_a.__dir__) #__dir__ comando para localizar na memória
print(list_b.__dir__)
'''
'''
#Declaração de lista
lista_vazia = [] #utilizando colchetes
lista_vazia_const = list() #utilizando construtor
'''
'''
lista_valores_number = [10, 5, 5.4]
lista_valores_string = ['a', 'b', 'João']
lista_valores_bool = {True, False, True}
lista_valores_list = (lista_valores_number, lista_valores_string, lista_valores_bool)
'''
'''
#Descobrindo o tamanho de uma lista
print(len(list_a))
print(len(lista_valores_list))

#Iterando uma lista
for i in lista_valores_string:
    print(i)

cont = 0
while cont < len(list_valores_number):
    print(list_a[cont])
    cont += 1

#------------------------------------
#append(x) -> método para adicionar elementos na lista, 
#sendo x o elemento para adicionar
lista_notas = list()

for i in range(5):
    listas_notas.append(float(input(f"{i+1}º Nota: ")))

#sum(x) -> retorna a soma dos elementos do objeto iterável x
# print(f"Média Final: {sum(lista_notas)/len(lista_notas):.2f}")
'''

'''
Desafio 01: Crie um algoritmo que pergunte ao usuário quantas temperaturas
serão lidas, posteriormente armazene essas temperaturas em uma lista e no
final retorne a média, a maior e menor temperatura registrada. Caso alguma 
temperatura ultrapasse 50° exiba um alerta '❌ Temperatura Muito Alta' e registre 
quantas vezes foi registrado temperaturas acima de 50°
'''
reg_qtd = float(input("Informe o número de registros de temperatura: "))
for i in range(reg_qtd):
    reg_temp.append(float(input(f"{i+1}º Temperatura: ")))
print(reg_temp)