import time
'''
1. Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total de ganho com juros 
no período.

dep_inicial = float(input('Deposito Inicial R$: '))
tx_juros = float(input('Taxa de Juros %: '))
mes = 1
var_aux = dep_inicial
while mes <= 24:
    print(f'#--- Rendimento do {mes}º mês ---#')
    dep_inicial = dep_inicial + (dep_inicial * (tx_juros / 100)) # dep_inicial = dep_inicial * (1 + (tx_juros / 100))
    print(f'Valor Inicial R$ {var_aux}\nTotal Rendimento R$ {dep_inicial:.2f}')

    mes += 1 #incremento

    #time.sleep(1) #pausa a execução por um tempo x determinado

print(f'Rendimento Total de 24 meses: R$ {dep_inicial:.2f}! Liberado!')
'''

'''
2. Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
Esse valor será depositado no ínicio de cada mês, e você deve considerá-lo para o cálculo
de juros do mês seguinte.

dep_inicial = float(input('Deposito Inicial R$: '))
tx_juros = float(input('Taxa de Juros %: '))
mes = 1
var_aux = dep_inicial
while mes <= 24:
    print(f'#--- Rendimento do {mes}º mês ---#')
    dep_inicial = dep_inicial + (dep_inicial * (tx_juros / 100)) # dep_inicial = dep_inicial * (1 + (tx_juros / 100))
    print(f'Valor Inicial R$ {var_aux}\nTotal Rendimento R$ {dep_inicial:.2f}')

    if mes == 24:
        break

    dep_mes = float(input(f'Depósito do {mes+1}º mês R$:'))

    dep_inicial += dep_mes # dep_inicial = dep_inicial + dep_mes

    mes += 1 #incremento

    time.sleep(1) #pausa a execução por um tempo x determinado

print(f'Rendimento Total de 24 meses: R$ {dep_inicial:.2f}! Liberado!')


3. Escreva um programa que pergunte o valor inicial de uma dívida e juros mensal. Pergunte
também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
'''
vlr_inicial = float(input('Valor da Dívida R$: '))
juros = float(input('Juros Mensal %: '))
vlr_mensal = float(input('Valor Mensal R$: '))
vlr_total_juros = 0
vlr_aux = vlr_inicial
total_meses = 0

while vlr_inicial >= 0:

    vlr_total_juros += (vlr_inicial * (1 + (juros/100))) - vlr_inicial
    vlr_inicial = vlr_inicial * (1 + (juros/100)) - vlr_mensal 

    print(f'Dívida R$: {vlr_inicial:.2f}')

    time.sleep(2)
    total_meses += 1
    #Desafio: resolver problema do exibir valor negativo

print(f'Total Pago: R${vlr_aux + vlr_total_juros:.2f}')
print(f'Juros Total: R${vlr_total_juros:.2f}')
print(f'Total de Meses pago: {total_meses} meses')   

