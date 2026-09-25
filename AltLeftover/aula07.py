import os
'''
Dicionários
'''
#declarando um dicionário
produtos = {
    "mouse": 199.9,
    "teclado": 295.95
}

#avaliar se uma chave está presente no dicionário (in)
print("monitor" in produtos)

#acessar um valor de uma chave
print(produtos['mouse'])

#modificando valor de uma chave
produtos['mouse'] = produtos['mouse'] * 0.85

print('Mouse com 15% de desconto: R$', produtos['mouse'])

#print(produtos['monitor']) - KeyError: 'monitor'

#adicionando produto 'monitor' no dicionário
produtos['monitor'] = 795.45
print(produtos)

#Métodos de Dicionário
print(produtos.items())

for key, value in produtos.items():
    print(f'{key}: {value:.2f}')

print(produtos.keys())
print(produtos.values())

# Média do preço dos produtos
print('Média preço dos produtos: R$', sum(produtos.values())/len(produtos.values()))

print(produtos.get('monitor')) #retorna o valor da chave - produtos['monitor']

#produtos.clear() - remove todos os itens da lista
os.system('cls')
#-------------------------------------------------------------------------------------
import os
import time
opcao = -1

produtos.clear()


MENU = '''
########################
### MERCADINHO SENAC ###
########################
----------------
--- PRODUTOS ---
----------------
[1] - ADICIONAR 
[2] - VISUALIZAR
[3] - APLICAR DESCONTO
[4] - APLICAR ACRÉSCIMO
[5] - REMOVER 
[0] - SAIR

'''

while opcao != 0:
    print(MENU)
    opcao = int(input('Opção: '))
    match opcao:
        case 1:
            nome_prod = input('Nome Produto: ').upper()
            valor_prod = float(input('Preço R$ '))
            produtos[nome_prod] = valor_prod
            print('Produto Cadastrado! ✅')
            time.sleep(2)
            os.system('cls')
        case 2:
            print('--- PRODUTOS CADASTRADOS ---')
            for k, v in produtos.items():
                print(f'{k.title()}: R$ {v:.2f}')
            input('Pressione ENTER para continuar...')
            os.system('cls')
        case 3:
            pct_desconto = float(input('Desconto %: ')) / 100
            nome_prod = input('Produto: ').upper()

            produtos[nome_prod] = produtos[nome_prod] * (1 - pct_desconto) 
            print('Desconto Aplicado!✅')
            time.sleep(2)
            os.system('cls')
        case 4:
            pct_acrescimo = float(input('Acréscimo %: ')) / 100
            nome_prod = input('Produto: ').upper()

            produtos[nome_prod] = produtos[nome_prod] * (1 + pct_acrescimo) 
            print('Acréscimo Aplicado!✅')
            time.sleep(2)
            os.system('cls')
        case 5:
            nome_prod = input('Produto: ').upper()
            produtos.pop(nome_prod)
            print('Produto Removido!✅')
            time.sleep(2)
            os.system('cls')
        case 0:
            print('Bye :) Volte Sempre!')
        case _:
            print('Opção Inválida!')