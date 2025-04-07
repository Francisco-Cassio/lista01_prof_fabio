from funcao_linha import linhas

def media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3

    print(f'Média: ({num1} + {num2} + {num3}) / 3 = {media}')


num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))
num3 = int(input('Terceiro Número: '))
linhas()

media(num1, num2, num3)