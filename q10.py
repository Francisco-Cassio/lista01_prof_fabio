from funcao_linha import linhas

def elementos_divisao(num1, num2):
    quociente = num1 // num2
    resto = num1 % num2

    print(f'Quociente: {quociente}\nResto: {resto}')  

num1 = int(input('Primeiro Número: '))
num2 = int(input('Segundo Número: '))

linhas()

elementos_divisao(num1, num2)