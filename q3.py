from funcao_linha import linhas

def calcular_hora(horas, minutos):
    horas = minutos // 60
    min = minutos % 60
    
    print(f'{minutos} min equivale a\n>>>>> {horas}h{min}min <<<<<')


minutos = int(input('Minutos: '))

linhas()

horas = minutos // 60
min = minutos % 60

calcular_hora(horas, min)