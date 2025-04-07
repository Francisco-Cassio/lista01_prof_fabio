from funcao_linha import linhas

def conversao(celsius):
    fahrenheit = (9 * celsius + 160) / 5

    print(f'{celsius:.0f}°C equivale a\n>>>> {fahrenheit:.0f}°F <<<<')


celsius = int(input('Temperatura em Celsius: '))

linhas()

conversao(celsius)