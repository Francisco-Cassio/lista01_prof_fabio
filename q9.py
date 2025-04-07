from funcao_linha import linhas

def inverter (num1, num2):
    print(f'Valor: {num1}{num2}\nInverso: {num2}{num1}')


num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))

linhas()

inverter(num1, num2)