from funcao_linha import linhas

def quantidade(quant_latao):
    cobre = quant_latao * 0.7
    zinco = quant_latao - cobre

    print(f'Quantidade de cobre: {cobre:.1f} kg\nQuantidade de zinco: {zinco:.1f} kg')


quant_latao = int(input('Quantidade de latão(kg): '))
linhas()

quantidade(quant_latao)