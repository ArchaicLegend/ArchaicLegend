'''
    Tipos de Dados
    - int: Números inteiros sem parte decimal (ex. 42, -7)
    - float: Números reais com ponto decimal (ex. 3.14, 1.80, -2.5)
    - complex: Números complexos com parte real e imaginária (ex. 1+2j)
    - str: Textos delimitados por aspas simples ou duplas (ex. "aula 02" ou 'Aula 02')
    - bool: Valores lógicos verdadeiro (True) ou Falso (False)
'''

nome = 'Analista de Dados'
preco = 599.90
carga_horaria = 240
ativado = True

'''
print('Nome do Curso: ' + nome +
        '\n' + 'Valor: R$ ' + preco +
        '\n' + 'CH: ' + carga_horaria + 'hrs' +
        '\n' + 'Ativado: ' + ativado)

O código acima gera o erro: [TypeError]: can only concatenate str (not "float") to str
'''
# F-String: adiciona variáveis dentro de textos 

print(f'Nome do Curso: {nome}\nValor: R$ {preco}\nCH: {carga_horaria}hrs\nAtivado: {ativado}')

resultado = f'''
Nome do Curso: {nome}
Valor: R${preco}
CH: {carga_horaria}hrs
Ativado: {ativado}
'''
print(resultado)

#Operadores Relacionais
idade = 0

print(idade >= 18) #inclusivo
print(idade <= 18) #inclusivo
print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)

#Operadores Lógicos
#not - and - or
'''
    Salário de um funcionário for > 2000 e tempo de empresa for > 5, receberá aumento!
'''
salario = 2000
tempo_empresa = 10

print('Receberá aumento?')
print(salario > 2000 and tempo_empresa > 5)

'''
    Um aluno será aprovado se media >= 7 ou presença for >= 75
'''
media = 6.75
presenca = 75
print('Aprovado?')
print(media >= 7 or presenca >= 75)

#Função entrada de dados - input
temperatura = float(input('Digite a temperatura: '))
print('O valor da temperatura é', temperatura)

print(type(temperatura)) # função type() para descobrir o tipo de dado

'''
Casting de dados
    Processo de transformar um determinado dado em um tipo diferente

    - str(x): transformar x no tipo string
    - int(x): transformar o x no tipo int
    - float(x): transformar o x no tipo float
'''

# print(type(int("a"))) gera o erro [ValueError]: invalid literal for int() with base 10: 'a'

#Entrada de dados
preco = float(input('Digite o preço do produto: '))
desconto =  float(input('Digite o valor do desconto: '))

#Processamento
preco_final = preco - (preco * (desconto / 100))

#Saída de dados
print('Preço Final: R$', preco_final)

'''
Escreva um algoritmo que receba 3 notas e retorne a média final do aluno.
'''
# Entrada de Dados
nota_1 = float(input("Digite a 1º Nota: "))
nota_2 = float(input("Digite a 2º Nota: "))
nota_3 = float(input("Digite a 3º Nota: "))

# Processamento
media = (nota_1 + nota_2 + nota_3) / 3

# Saída de Dados
print(f'Média: {media:.2f}')

#Arredondamento de números
# round(x, y) -> x: valor para arredondar, y: a quantidade de casas para arredondar
# round() é uma função que desconsidera o 0 no final 