from funcao_linha import linhas

def conversao(valor_dol, cotacao):
    valor_real = valor_dol * cotacao
    
    print(f'US$ {valor_dol:.2f} equivale a\n>>>> R$ {valor_real:.2f} <<<<')

valor_dol = float(input('Valor em dólares: US$ '))
cotacao = 5.70

linhas()

conversao(valor_dol, cotacao)