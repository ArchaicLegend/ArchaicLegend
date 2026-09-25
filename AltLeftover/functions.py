'''
Exercício 01
Crie uma função chamada calcular_media que:
    - Receba uma quantidade variável de números usando *args.
    - Receba informações opcionais sobre o aluno usando **kwargs, como nome, turma e 
      disciplina.
    - Calcule a média dos números recebidos.
    - Retorne uma mensagem contendo o nome do aluno e sua média.
    - Caso nenhum número seja informado, a função deve informar que não é possível 
      calcular a média.
'''
def calcular_media(*args, **kwargs):
    if len(args) == 0:
        return 'Não é possível calcular a média!'

    try:
        media = sum(args)/len(args)
        return f'Aluno: {kwargs['nome']}\nMédia: {media:.2f}'
    except KeyError:
        return 'Erro de chave ausente! Informe o nome do aluno!'
    except:
        return 'Erro ao calcular a média'