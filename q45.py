from funcao_linha import linhas

def divisao(valor):
    cem = valor // 100
    cinquenta = (valor % 100) // 50
    dez = ((valor % 100) % 50) // 10
    cinco = (((valor % 100) % 50) % 10) // 5
    um = (((valor % 100) % 50) % 10) % 5

    print(f'R${valor:.2f} pode ser pago com:\n{cem} notas de 100\n{cinquenta} notas de 50\n{dez} notas de 10\n{cinco} notas de 5\n{um} notas de 1')


valor = int(input('Valor: R$ '))
linhas()

divisao(valor)