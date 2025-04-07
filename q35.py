from funcao_linha import linhas

def soma_elementos(num):
    mil = num // 1000
    cent = (num % 1000) // 100
    dez = ((num % 1000) % 100) // 10
    uni = ((num % 1000) % 100) % 10

    valor = mil + cent + dez + uni

    print(f'Soma dos elementos:\n{mil} + {cent} + {dez} + {uni} = {valor}')


num = int(input('Número: '))
linhas()

soma_elementos(num)