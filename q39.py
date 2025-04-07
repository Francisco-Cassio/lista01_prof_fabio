from funcao_linha import linhas

def calculo(a, b, c):
    r = (a + b) ** 2
    s = (b + c) ** 2

    d = (r + s) / 2

    print(f'R = ({a} + {b})² = {r}\nS = ({b} = {c})² = {s}')
    linhas()
    print(f'D = ({r} + {s}) / 2 = {d}')


a = int(input('Primeiro Número: '))
b = int(input('Segundo Número: '))
c = int(input('Terceiro Número: '))

linhas()

calculo(a, b, c)