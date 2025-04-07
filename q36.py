from funcao_linha import linhas

def conversao(anos, meses, dias):
    total = (anos * 365) + (meses * 30) + dias

    print(f'{anos} ano(s), {meses} mes(es) e {dias} dia(s) equivale a\n>>> {total} dia(s) <<<')


anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))
linhas()

conversao(anos, meses, dias)