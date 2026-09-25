'''
Uma loja precisa de um pequeno programa para calcular o valor total de uma compra. 
O código abaixo foi entregue por um colega, mas não está executando.

Encontre e corrija todos os erros de sintaxe para fazer o programa funcionar.
'''

print("=== SISTEMA DE COMPRAS ===")

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: ")
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade

if quantidade > 0
    print("Produto:", produto)
    print("Quantidade:", quantidade)
    print("Total da compra: R$", total)
else:
    print("A quantidade deve ser maior que zero.")

print("Compra finalizada!")

'''
| Bug | Linha | O que está errado? | Como corrigir? |
| --- | ----: | ------------------ | -------------- |
| 1   |     ? | ?                  | ?              |
| 2   |     ? | ?                  | ?              |

'''

'''
Uma escola precisa de um programa simples para calcular a média de um aluno. 
O código foi escrito corretamente do ponto de vista da sintaxe, mas apresenta problemas quando é executado.

Execute o programa, observe o erro apresentado pelo Python e descubra o que está causando o problema.
'''

print("=== SISTEMA DE MÉDIA ===")

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = nota1 + nota2 + nota3 / 3

print("\nAluno:", nome)
print("Média:", media)

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno em recuperação.")

'''
| Bug | Linha | O que está errado? | Como corrigir? |
| --- | ----: | ------------------ | -------------- |
| 1   |     ? | ?                  | ?              |
| 2   |     ? | ?                  | ?              |

'''