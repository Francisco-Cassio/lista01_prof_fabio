from funcao_linha import linhas

def porcentagem(valor):
    parte = valor * 0.7

    print(f'70% de R${valor:.2f} é\n>>>> R${parte:.2f} <<<<')


valor = float(input('Valor: R$ '))

linhas()

porcentagem(valor)