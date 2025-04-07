from funcao_linha import linhas

def distancia(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

    print(f'Distância entre os pontos: ({x1}, {y1}) e ({x2}, {y2}):\n>>>> {d:.2f} <<<<')


linhas()
x1 = int(input('Ponto x1: '))
y1 = int(input('Ponto y1: '))
linhas()
x2 = int(input('Ponto x2: '))
y2 = int(input('Ponto y2: '))
linhas()

distancia(x1, y1, x2, y2)