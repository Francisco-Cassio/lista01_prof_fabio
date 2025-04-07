from funcao_linha import linhas

def conversao(km):
    m = km * 1000

    print(f'{km:.1f} km equivale a\n>>>> {m:.0f} m <<<<')


km = float(input('Quilometros: '))
linhas()

conversao(km)