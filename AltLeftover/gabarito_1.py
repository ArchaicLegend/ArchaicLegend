'''
Questão 01
'''

def calcular_total(*vendas):
    return sum(vendas)

def calcular_media(*valores):
    return sum(valores)/len(valores)

def classificar_venda(venda, limite=100):
    '''
    Retorna a classificação de uma venda.

    return:
        - acima do limite
        - acima de 75% do limite
        - acima de 50% do limite
        - acima de 25% do limite
    '''

    if venda > limite:
        return 'Acima do limite!'
    elif venda > limite*0.75:
        return 'Acima de 75% do limite'
    elif venda > limite*0.50:
        return 'Acima de 50% do limite'
    elif venda > limite*0.25:
        return 'Acima de 25% do limite'
    else:
        return 'Abaixo de 25% do limite'

print(calcular_total(500, 450, 350, 100))

print(calcular_media(500, 450, 350, 100))

print(classificar_venda(505, 1000))
print(classificar_venda(100, 1000))
print(classificar_venda(990, 1000))
print(classificar_venda(251, 1000))

'''
Questão 02
'''
def gerar_relatorio(**dados):
    if dados:
        relatorio = '=' * 25
        for k, v in dados.items():
            relatorio += f'\n{k.upper()}: {v}'

        relatorio += '\n'
        relatorio += '=' * 25

        return relatorio

    return 'Nenhum parâmetro informado!'

print(gerar_relatorio(titulo='Acompanhamento de Vedas',
                      periodo='Jan - Fev | 2026',
                      responsavel='Dalton',
                      quantidade_registros=2000))

print(gerar_relatorio(titulo='Alunos Aprovados',
                      quantidade=50,
                      ano_letivo=2026,
                      diretor='Ana Cristina'))

print(gerar_relatorio())

