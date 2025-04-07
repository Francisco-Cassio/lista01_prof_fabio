from funcao_linha import linhas

def inverso(num):
    centena = num // 100
    dezena = (num % 100) // 10
    unidade = num % 10

    print(f'Inverso: {unidade}{dezena}{centena}')

num = int(input('Número: '))

linhas()

inverso(num)