"""
Laços de Repetição
 - while
 - do..while
 - for
 
#Imprimir do número 1 até 10
x = 1
while(x <= 10):
    print(x)
    x = x + 1 #Incremento
    #x += 1

x = 10
while(x >= 1):
    print(x)
    x = x - 1 #Incremento
    #x += 1

#Colocar aqui o resto da aula
"""





















"""
while True:
else:
    print("Opção inválida!")

# versão com match case
while True:
    print(MENU)
    opcao : int(input("->"))

    match opcao:
        case 1:
            print("Opção 1 escolhida!")
        case 2:
            print("Opção 2 escolhida!")
        case 3:
            print("Bye :)!")
"""
#Continuar

"""
1. Escreva um programa que pergunta o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o tal ganho com os juros no período.
"""
dep_ini = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite o valor dos juros: "))
if(dep_ini <= 1000):
    print("Crédito Aprovado!")
    print(f"Total: R$ {dep_ini * taxa_juros:.2f}!")
else:
    print("Crédito Negado!")

"""
2. Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no início de cada mês, e você deve considera-lo para o cálculo de juros
do mês seguinte.

3. Escreva um programa que pergunte o valor inicial de uma dívida e juros mensal. Pergunte também 
o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago 
e o total de juros pago.
"""

