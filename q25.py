from funcao_linha import linhas

def conversao(metros):
    km = metros // 1000
    m = metros % 1000

    print(f'{metros:.2f} m equivale a\n>>>> {km:.0f} km e {m:.0f} m <<<<')


metros = float(input('Metros: '))
linhas()

conversao(metros)