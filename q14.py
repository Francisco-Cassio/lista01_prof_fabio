from funcao_linha import linhas

def media_ponderada(n1, peso1, n2, peso2, n3, peso3):
    media_pond = (n1*peso1 + n2*peso2 + n3*peso3) / (peso1 + peso2 + peso3)

    print(f'Média ponderada: {media_pond:.2f}') 


n1 = float(input('Primeira nota: '))
peso1 = int(input('Peso: '))

linhas()

n2 = float(input('Segunda nota: '))
peso2 = int(input('Peso: '))

linhas()

n3 = float(input('Terceira nota: '))
peso3 = int(input('Peso: '))

linhas()

media_ponderada(n1, peso1, n2, peso2, n3, peso3)