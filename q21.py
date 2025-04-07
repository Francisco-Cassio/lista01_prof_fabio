from funcao_linha import linhas

def conversao(celsius):
    celsius = (5 * fahrenheit - 160) / 9

    print(f'{fahrenheit:.0f}°F equivale a\n>>>>> {celsius:.0f}°C <<<<<')


fahrenheit = float(input('Temperatura em Fahrenheit: '))

linhas()

conversao(fahrenheit)