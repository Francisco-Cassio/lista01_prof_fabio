from funcao_linha import linhas

def conversao(decimal):
    mil = binario // 1000
    cem = (binario % 1000) // 100
    dez = ((binario % 1000) % 100) // 10
    um = ((binario % 1000) % 100) % 10

    p1 = mil * 8
    p2 = cem * 4
    p3 = dez * 2
    p4 = um

    decimal = p1 + p2 + p3 + p4

    print(f'Decimal: {decimal}')


binario = int(input('Binário: '))
linhas()

conversao(binario)