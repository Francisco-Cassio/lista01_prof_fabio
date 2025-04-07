from funcao_linha import linhas

def venda(custo_fab, percentual_distribuidor, imposto):
    val_distribuidor = (custo_fab/100) * percentual_distribuidor
    val_imposto = (custo_fab/100) * imposto
    custo_cons = custo_fab + val_distribuidor + val_imposto

    print(f'Preço de venda: R${custo_cons:.2f}')


custo_fab = float(input('Custo de fábrica: '))
percentual_distribuidor = float(input('Percentual do distribuidor: '))
imposto = float(input('Percentual de impostos: '))
linhas()

venda(custo_fab, percentual_distribuidor, imposto)