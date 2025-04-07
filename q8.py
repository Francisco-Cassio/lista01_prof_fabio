from funcao_linha import linhas

def calcular(num1, num2):
    soma = num1 + num2
    sub = num1 - num2
    div = soma / sub

    print(f'Soma: {num1} + {num2} = {soma}\nSubtração: {num1} - {num2} = {sub}\n--------------------------\nDivisão da soma pela subtração:\n>>>>>> {soma} / {sub} = {div:.2f} <<<<<<')


num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))

linhas()

calcular(num1, num2)