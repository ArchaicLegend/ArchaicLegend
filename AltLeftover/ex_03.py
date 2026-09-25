'''
Questão 1 – Cadastro de produtos
Situação-problema: Uma loja deseja armazenar informações básicas de seus produtos. 
Cada produto possui nome, preço e quantidade disponível em estoque.

Tarefas:
    - Crie um dicionário para representar um produto, utilizando as chaves nome, preco e estoque.
    - Cadastre pelo menos 5 produtos em uma estrutura de dados adequada.
    - Percorra os produtos com um laço de repetição.
    - Exiba o nome e o preço de cada produto.
    - Identifique os produtos com estoque inferior a 10 unidades utilizando uma estrutura condicional.

Desafio extra: calcule o valor total em estoque de cada produto (preço × quantidade).

produtos = []

for i in range(5):
    n_prod = input('Nome: ')
    p_prod = float(input('Preço R$: '))
    e_prod = int(input('Estoque: '))

    produtos.append({
        "nome": n_prod,
        "preco": p_prod,
        "estoque": e_prod
    })

for i, p in enumerate(produtos):
   print(f"""
PRODUTO {i + 1}
Nome: {p['nome']}
Preço: R$ {p['preco']}
""")
   if p.get('estoque') < 10:
      print(f'Estoque abaixo do limite! Quant.: {p.get('estoque')}')

   print(f'Valor Total em Estoque: R$ {p.get('preco') * p.get('estoque')}')



Questão 2 – Indicadores de desempenho
Situação-problema: Uma equipe de análise possui indicadores mensais de desempenho. Cada indicador será armazenado 
como uma tupla contendo o nome do indicador e seu valor.

Tarefas:
   - Crie pelo menos 6 tuplas no formato (nome_do_indicador, valor).
   - Armazene as tuplas em uma lista.
   - Percorra a lista utilizando um laço de repetição.
   - Exiba o nome e o valor de cada indicador.
   - Considere satisfatório um indicador com valor maior ou igual a 70 e classifique cada registro.

Desafio extra: calcule a média dos valores e informe quantos indicadores atingiram o resultado satisfatório.
'''

indicadores = [
   ('ATX', 45),
   ('DER', 25),
   ('ZOD', 70),
   ('JOI', 99),
   ('OSI', 64),
   ('TCP', 78)
]

result = {
   'media': 0,
   'quant_satisfatorio': 0
}

for i, ind in enumerate(indicadores):
   print(f'INDICADOR {i + 1}\nNome: {ind[0]}\nValor: {ind[1]}')
   result['media'] += ind[1]

   if ind[1] >= 70:
      print('Resultado: Atendido!')
      result['quant_satisfatorio'] += 1
   else:
      print('Resultado: Não Atendido!')

result['media'] = result['media']/len(indicadores)

print(f'Média Indicadores: {result['media']}\nQuantidade >= 70: {result['quant_satisfatorio']}')
   

