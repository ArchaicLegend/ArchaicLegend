'''
Continuidade Funções
'''

#parâmetros default
def exibir_nome(nome='Usuário'):
    print(f'Olá, {nome}!')

exibir_nome('Davi')

#ordem do parâmetros
def exibir_relatorio(indices, valores):
    print(f'{indices}: {valores}')

exibir_relatorio('Média Mensal', 75.6)
exibir_relatorio(valores=75.6, indices='Média Mensal')

#parâmetro *args
def somar(*valores):
    print(f'Soma: {sum(valores)}')
    

somar(12, 5, 4)
somar(15, 5, 4, 5)
somar(14, 5, 2, 5, 80, 4)

#parâmetro **kwargs
def criar_opcoes(**opcoes):
    config = {}
    for key, value in opcoes.items():
        config[key] = value

    return config
        
print(criar_opcoes(limite=10, tema='Dark', contraste=0.15))
'''
{
    'limite': 10,
    'tema': 'Dark',
    'constraste': 0.15
}
'''
print(criar_opcoes(tema='Dark', 
             idioma='PT-BR', 
             notificacoes=True, 
             volume=80, 
             qualidade='FullHD'))
'''
{
    'tema': 'Dark',
    'idioma': 'PT-BR',
    'notificacoes': True,
    'volume': 80,
    'qualidade': 'FullHD'
}
'''

def registrar_evento(evento, *detalhes, **metadata):
    print(f'Evento: {evento}')
    print(f'Detalhes: {detalhes}')
    print(f'Metadata: {metadata}')

registrar_evento(
    'Workshop Senac',
    'WS1095',
    20260915001,
    local='Senac Centro',
    horario='18:00',
    turno='Noite'
)