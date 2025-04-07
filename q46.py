from funcao_linha import linhas

def valores(valor_mercadoria):
    parcela = valor_mercadoria // 3
    entrada = (valor_mercadoria % 3) + parcela

    print(f'Entrada: R$ {entrada:.2f}\nPrimeira Parcela: R${parcela:.2f}\nSegunda Parcela: R${parcela:.2f}\n')


valor_mercadoria = float(input('Valor da mercadoria: R$ '))
linhas()

valores(valor_mercadoria)