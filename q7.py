from funcao_linha import linhas

def calcular(num1, num2, num3):
    soma = num1 + num2
    sub = num2 - num3
    
    print(f'Soma dos 2 primeiros dígitos: {num1} + {num2} = {soma}\nDiferença dos 2  últimos dígitos: {num2} - {num3} = {sub}')


num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))
num3 = int(input('Terceiro Número: '))

linhas()

calcular(num1, num2, num3)

