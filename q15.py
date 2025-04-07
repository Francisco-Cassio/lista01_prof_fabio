from funcao_linha import linhas

def area_triangulo(base, altura):
    area = (base * altura)/2

    print(f'Área: {area:.2f}m²')
    linhas()


linhas()
base = float(input('Base: '))
linhas()
altura = float(input('Altura: '))
linhas()

area_triangulo(base, altura)