from funcao_linha import linhas

def conversao(meses):
    anos = meses // 12
    mes = meses % 12

    print(f'{meses} meses equivale a\n>>>>> {anos} ano(s) e {mes} mes(es) <<<<<')


meses = int(input('Meses: '))
linhas()

conversao(meses)