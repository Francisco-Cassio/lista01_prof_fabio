from funcao_linha import linhas

def soma(num):
    cent = num // 100
    dez = (num % 100) // 10
    uni = num % 10
    
    total = cent + dez + uni

    print(f'Soma dos elementos:\n{cent} + {dez} + {uni} = {total}')


num = int(input('Número: '))

linhas()

soma(num)