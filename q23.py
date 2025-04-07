from funcao_linha import linhas

def conversao(kg):
    g = kg * 1000

    print(f'{kg:.2f} kg equivale a\n>>>> {g:.0f} g <<<<')


kg = float(input('Quilos: '))
linhas()

conversao(kg)