from funcao_linha import linhas

def area_retangulo(base, altura):
    area = base * altura

    print(f'Área: {area:.2f}m²')
    linhas()


linhas()
base = float(input('Base: '))
linhas()
altura = float(input('Altura: '))
linhas()

area_retangulo(base, altura)