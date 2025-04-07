from funcao_linha import linhas

def conversao(dias):
    semana = dias // 7
    resto = dias % 7

    print(f'{dias} dias equivale a\n>>> {semana} semana(s) e {resto} dia(s) <<<')


dias = int(input('Dias: '))
linhas()

conversao(dias)