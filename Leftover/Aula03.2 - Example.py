"""
#Expressões Lógicas
print(10 > 20 and 20 < 1)


False and False
    False


print(True or False and not True)

True or False and False
    True or False
        True

# Estruturas Condicionais
# Condições Simples
if(10 % 2 == 0):
    print("O número 10 é PAR!")

#Condição Composta
if(10 % 2 == 0):
    print(" O número 10 é PAR!")
else:
    print("O número é IMPAR!")

#Condição Aninhada
media = float(input("Digite sua média: "))
if(media >= 7):
    print('Aprovado! 🎉')
elif(media >= 5):
    print('Recuperação! 😒')
else:
    print('Reprovado! ❌')


1. Escreva um programa que pergunta a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma 
mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h.

velocidade = int(input("Digite a velocidade: "))
if(velocidade >80):
    print("Veículo multado")
    multa = (velocidade - 80) * 5
    print(f"{multa:.2f}")
else:
    print("Dentro do limite")

2. Escreva um programa que pergunta a distância que um passageiro deseja percorrer em km. Calcule o preço 
da passagem, cobrando R$0,50 por km para viagem de até 200km, e R$0,45 para viagens mais longas.
"""
"""
distancia = int(input('Distancia: '))
if(distancia <= 200):
    print(f'Preço da Passagem: R${distancia * 0.5}:.2f')
else:
    print(f'Preço da Passagem: R${distancia * 0.45}:.2f')


3. Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar
o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode 
superar a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido 
pelo número de meses a pagar.

casa = float(input("Valor da Casa: "))
salario = float(input("Digite o salário: "))
anoPagar = float(input("Digite com quantos anos a casa é quitada: "))
prestacao = casa / (anoPagar * 12)
if((prestacao <= (salario * (30 / 100)))):
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")


#Professor's Example

valor_casa = float(input("Valor da Casa: R$ "))
salario = float(input('Salario: R$ '))
meses = int(input("Quantidade de Anos: ")) * 12
prestacao = valor_casa / meses

if(prestacao <= salario * 0.3):
    print("Empréstimo Aprovado!")
    print(f"Valor das Parcelas R${prestacao:.2f})!")
else:
    print("Empréstimo Negado!")
"""

"""

4. Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residencial, I para indústrias e
C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.

                Preço por tipo e faixa de consumo
        
    Tipo           | Faixa (kWh)           |  Preço

    Residencial    |Até 500                | R$ 0,40
                   |Acima de 500           | R$ 0,65
    
    Comercial      |Até 1000               | R$ 0,55
                   |Acima de 1000          | R$ 0,60
    
    Industrial     |Até 5000               | R$ 0,55
                   |Acima de 5000          | R$ 0,60
"""

"""
kWh = float (input("Enter the kWh consumed: "))
installation_type = input("Choose a installation type (n1/R, n2/C, n3/I)")

if installation_type == "R":
    if kWh <= 500:
        price = 0.40
        total = price * kWh
        print(f"The price you will pay is: R$ {total:.2f}")
    else:
        price = 0.65
        total = price * kWh
        print(f"The price you will pay is: R$ {total:.2f}")

elif installation_type == "C":
    if kWh <= 1000:
            price = 0.55
            total = price * kWh
            print(f"The price you will pay is: R$ {total:.2f}")
    else:
        price = 0.60
        total = price * kWh
        print(f"The price you will pay is: R$ {total:.2f}")

else:
    installation_type == "I"
    if kWh <= 5000:
            price = 0.55
            total = price * kWh
            print(f"The price you will pay is: R$ {total:.2f}")
    else:
        price = 0.60
        total = price * kWh
        print(f"The price you will pay is: R$ {total:.2f}") 
"""

#Professor's Example

"""
quant_kwh = float(input("Quantidade de kwh: "))
tipo_instalacao = input("Tipo de Instalação: [R] Residencial, [I] Industrial, [C] Comercial\n-> ")

if(tipo_instalacao.upper() == "R"):
    if(quant_kwh <= 500):
        print(f"Total: R$ {(quant_kwh * 0.40)}:.2f")
    else:
        print(f"Total: R$ {(quant_kwh * 0.65)}:.2f")
elif(tipo_instalacao.upper() == "C"):
    if(quant_kwh <= 1000):
        print(f"Total: R$ {quant_kwh * 0.55}:.2f")
    else:
        print(f"Total: R$ {(quant_kwh * 0.60)}:.2f")
elif(tipo_instalacao.upper() == "I"):
    if(quant_kwh <= 5000):
        print(f"Total: R$ {(quant_kwh * 0.55)}:.2f")
    else:
        print(f"Total: R$ {(quant_kwh * 0.60)}:.2f")
else:
    print("Tipo de instalação inválida!")
"""

while
    x <= 10
    print("OK")