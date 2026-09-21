#Expressões Lógicas
print(10 > 20 and 20 < 1)
'''
False and False
    False
'''

print(True or False and not True)
'''
True or False and False
    True or False
        True
'''
# Estruturas Condicionais
# Condição Simples
if(10 % 2 == 0):
    print('O número 10 é PAR!')

#Condição Composta
if(11 % 2 == 0):
    print('O número é PAR!')
else:
    print('O número é IMPAR!')

#Condição Aninhada
media = float(input('Digite sua média: '))
if(media >= 7):
    print('Aprovado! 🎉')
elif(media >= 5):
    print('Recuperação!😒')
else:
    print('Reprovado! ❌')

'''
1. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem
dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.
'''
velocidade = int(input('Velocidade: '))
if(velocidade > 80):
    print('Veículo Multado!')
    multa = (velocidade - 80) * 5
    print(f'Multa R${multa:.2f}')

'''
2. Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem,
cobrando R$0,50 por km para viagem de até 200km, e R$0,45 para viagens mais longas.
'''
distancia = int(input('Distância: '))
if(distancia <= 200):
    print(f'Preço da Passagem: R${(distancia * 0.5):.2f}')
else:
    print(f'Preço da Passagem: R${(distancia * 0.45):.2f}')
'''
3. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor 
da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode superar a 30% do 
salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
'''
valor_casa = float(input('Valor da Casa: R$ '))
salario = float(input('Salário: R$ '))
meses = int(input('Quantidade de Anos: ')) * 12
prestacao = valor_casa / meses

if(prestacao <= salario * 0.3):
    print('Empréstimo Aprovado!')
    print(f'Valor das Parcelas R${prestacao:.2f}!')
else:
    print('Empréstimo Reprovado!')

'''
Solução exercício 4.
'''
quant_kwh = float(input('Quantidade em kWh: '))
tipo_instalação = input('Tipo de Instalação: [R] Residencial, [I] Industrial, [C] Comercial\n-> ')

if(tipo_instalação.upper() == 'R'):
    if(quant_kwh <= 500):
        print(f'Total: R$ {(quant_kwh * 0.40):.2f}')
    else:
        print(f'Total: R$ {(quant_kwh * 0.65):.2f}')
elif(tipo_instalação.upper() == 'C'):
    if(quant_kwh <= 1000):
        print(f'Total: R$ {(quant_kwh * 0.55):.2f}')
    else:
        print(f'Total: R$ {(quant_kwh * 0.60):.2f}')
elif(tipo_instalação.upper() == 'I'):
    if(quant_kwh <= 5000):
        print(f'Total: R$ {(quant_kwh * 0.55):.2f}')
    else:
        print(f'Total: R$ {(quant_kwh * 0.60):.2f}')
else:
    print('Tipo de Instalação Inválida!')
    
