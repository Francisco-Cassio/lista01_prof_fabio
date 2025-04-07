from funcao_linha import linhas

def subtracao_inverso(num):
    cent = num // 100
    dez = ((num % 100) // 10) * 10
    uni = (num % 10) * 100

    valor = uni + dez + cent
    sub = num - valor

    print(f'{num} - {valor} = {sub}')


num = int(input('Número: '))
linhas()

subtracao_inverso(num)