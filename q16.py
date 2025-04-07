from funcao_linha import linhas

def area_quadrado(lado):
    area = lado ** 2

    print(f'Área: {area:.2f}m²')


lado = float(input('Medida do lado: '))

linhas()

area_quadrado(lado)