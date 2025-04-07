from funcao_linha import linhas

def calculo(a, b, c, d, e, f):
    x = ((c * e) - (b * f)) / ((a * e) - (b * d))
    y = ((a * f) - (c * d)) / ((a * e) - (b * d))

    print(f'X = (({c} * {e}) - ({b} * {f})) / (({a} * {e}) - ({b} * {d})) = {x:.1f}\nY = (({a} * {f}) - ({c} * {d})) / (({a} * {e}) - ({b} * {d})) = {y:.1f}')


a = int(input('Valor de A: '))
b = int(input('Valor de B: '))
c = int(input('Valor de C: '))
d = int(input('Valor de D: '))
e = int(input('Valor de E: '))
f = int(input('Valor de F: '))
linhas()

calculo(a, b, c, d, e, f)