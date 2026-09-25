'''
Laços de Repetição
- while
- do..while
- for
'''
#Imprimir do número 1 até 10
x = 1 #contador
while(x <= 10):
    print(x)
    x = x + 1 #incremento 
    #x += 1

#Imprimir do número 10 até o 1
cont = 10
while cont >= 1:
    print(cont)
    cont = cont - 1 #decremento
    #cont -= 1

#----------------------------------------------------
print('#----------------------------------------------------#')
#break: destinado a encerrar um laço de repetição (loop)
cont_1 = 0
while cont_1 <= 10:
    cont_1 += 1

    if cont_1 == 11:
        break

    if(cont_1 % 2 == 0):
        print(f'{cont_1} --> PAR!')
    else:
        print(f'{cont_1} --> ÍMPAR!')
    

MENU = '''
#--- Menu Principal ---#
[1] - Opção 1
[2] - Opção 2
[3] - Sair
'''

while True:
    print(MENU)
    opcao = int(input('-> '))

    if opcao == 1:
        print('Opção 1 escolhida!')
    elif opcao == 2:
        print('Opção 2 escolhida!')
    elif opcao == 3:
        print('Bye :)')
        break
    else:
        print('Opção inválida!')

# versão com match case
while True:
    print(MENU)
    opcao = int(input('-> '))

    match opcao:
        case 1:
            print('Opção 1 escolhida!')
        case 2:
            print('Opção 2 escolhida!')
        case 3:
            print('Bye :)!')
            break
        case _:
            print('Opção Inválida!')
    