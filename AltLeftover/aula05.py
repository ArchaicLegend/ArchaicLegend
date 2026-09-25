'''
Laços de Repetição - FOR
'''
#imprimir de 1 até 10
for i in range(1, 11):
    print(i)

#imprimir de 10 até 1
for i in range(10, 0, -1):
   print(i)

# listar todos os números múltiplos de 3 de 1 até 20
for i in range(1, 20):
    if i % 3 == 0:
        print(i)

# listar todos os números ímpares de 105 até 200
for i in range(105, 200, 2):
    print(i)

# Acumuladores
cont = 0
soma = 0

while cont < 5:
    nota = float(input(f'Digite a sua {cont+1}º nota:'))
    soma += nota
    cont += 1

print(f'Média Final: {soma/5:.1f}')
