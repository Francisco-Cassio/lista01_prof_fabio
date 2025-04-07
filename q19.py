from funcao_linha import linhas

def volume_esfera(raio):
    pi = 3.14
    volume = (4 * pi * (raio ** 3))/3

    print(f'Volume: {volume:.2f}m³')


raio = float(input('Raio: '))

linhas()

volume_esfera(raio)