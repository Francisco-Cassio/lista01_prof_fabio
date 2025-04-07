from funcao_linha import linhas

def conversao(m):
    cm = m * 100

    print(f'{m:.1f} m equivale a\n>>>> {cm:.0f} cm <<<<')


m = float(input('Metros: '))
linhas()

conversao(m)