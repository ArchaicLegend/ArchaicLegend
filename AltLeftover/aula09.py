"""Tratamento de Erro/Exceções"""

try:
    print('Iniciando...')

    ex = float('Davi')

except:
    print('[ERROR]: Problema na Estrutura')


print('Quase lá...')

#Capturar um erro
try:
    print('Iniciando...')

    #ex = float('Davi')

    lista = [1, 2, 3]
    lista[10]

except ValueError:
    print('[ERROR]: Erro no valor do tipo de dado')
except IndexError:
    print('[ERROR]: Erro no index de acesso ao objeto(lista)')
except:
    print('[ERROR]: Erro inesperado')

print('Quase lá...')
