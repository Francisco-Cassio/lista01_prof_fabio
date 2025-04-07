from funcao_linha import linhas

def conversao(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    days = (dias % 365) % 30

    print(f'{dias} dia(s) equivale a\n>>> {anos} ano(s), {meses} mes(es) e {days} dia(s) <<<')


dias = int(input('Dias: '))
linhas()

conversao(dias)