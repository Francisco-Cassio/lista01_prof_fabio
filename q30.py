from funcao_linha import linhas

def conversao(minutos):
    dias = minutos // 1440
    horas = (minutos % 1440) // 60
    min = minutos % 60

    print(f'{minutos} min equivale a\n>>>>> {dias} dia(s), {horas} hora(s) e {min} minuto(s) <<<<<')


minutos = int(input('Minutos: '))
linhas()

conversao(minutos)