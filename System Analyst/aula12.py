"""21/09/2026

Tarefa

1. Calcular a participação percentual de cada produto no total.

2. Calcular a variação percentual entre os períodos informados.

3. Identificar o produto com maior variação.

vendas = [
{"produto": "A", "atual": 4200, "anterior": 3900 },
{"produto": "B", "atual": 2800, "anterior": 3100},
{"produto": "C", "atual": 5100, "anterior": 4600}
]

Critério de conclusão: cada dupla apresenta os percentuais
calculados e o produto de maior variação.
"""

vendas = [
{"produto": "A", "atual": 4200, "anterior": 3900 },
{"produto": "B", "atual": 2800, "anterior": 3100},
{"produto": "C", "atual": 5100, "anterior": 4600}
]

#1. Calcular a participação percentual de cada produto no total.


#Produto "A"

print(vendas[0]["atual"] + vendas[1]["atual"] + vendas[2]["atual"])

def var_percentual(atual: int, anterior: int) -> str:
    return str(f'{((atual - anterior) / anterior) * 100:.2f} %')

#Testes
print(part_percentual(dataset_vendas))

for i in dataset_vendas:
    print(f'Produto: {i['produto']}' | 
          Variação %: {var_percentual(i['atual'], i['anterior']):.2f})
var_perc_dict = {}
#var_perc_list = []
for i in dataset_vendas:
    var_perc_dict[i['produto']] = round(var_percentual(i['atual'], i['anterior']), 2)
    #var_perc_list.append(tupla(i['produto'], var_percentual(i['atual'], i['anterior'])))

    print(var_perc_dict)