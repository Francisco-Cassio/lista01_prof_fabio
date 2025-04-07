from funcao_linha import linhas

def soma_inverso(num):
    cent = num // 100
    dez = ((num % 100) // 10) * 10
    uni = (num % 10) * 100

    valor = uni + dez + cent
    soma = num + valor

    print(f'{num} + {valor} = {soma}')


num = int(input('Número: '))
linhas()

soma_inverso(num)