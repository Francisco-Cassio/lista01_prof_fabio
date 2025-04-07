from funcao_linha import linhas

def aumento(salario):
    aumento = salario * 0.25
    novo_salario = salario + aumento

    print(f'Valor do aumento: R${aumento:.2f}')
    linhas()
    print(f'Novo Salário: {novo_salario:.2f}')
    linhas()

linhas()
salario = float(input('Salário: R$'))
linhas()

aumento(salario)
