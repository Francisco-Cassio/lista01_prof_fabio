from funcao_linha import linhas

def gasto_cigarro(anos_fumante, quantidade_cigarros, preco_carteira):
    carteira = 20
    gasto = (((anos_fumante * 365) * quantidade_cigarros) / carteira) * preco_carteira

    print(f'A quantidade de dinheiro gasto foi\n>>>> R${gasto:.2f} <<<<')


anos_fumante = int(input('Fuma há quantos anos? '))
quantidade_cigarros = int(input('Cigarros fumados por dia: '))
preco_carteira = float(input('Preco da carteira: R$ '))
linhas()

gasto_cigarro(anos_fumante, quantidade_cigarros, preco_carteira)