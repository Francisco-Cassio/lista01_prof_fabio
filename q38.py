from funcao_linha import linhas

def calculo(num1, den1, num2, den2):
    denominador = den1 * den2
    numerador = (denominador / den1) * num1 + (denominador / den2) * num2

    print(f'Resultado da Soma:\n{num1} / {den1} + {num2} / {den2} = {numerador:.0f} / {denominador:.0f}')



num1 = int(input('Numerador: '))
den1 = int(input('Denominador: '))
linhas()
num2 = int(input('Numerador: '))
den2 = int(input('Denominador: '))
linhas()

calculo(num1, den1, num2, den2)