from funcao_linha import linhas

def calcular_hora(horas, minutos):
    total = (horas * 60) + minutos
    
    print(f'{horas}h{minutos}min equivale a\n>>> {total} minutos <<<')


horas = int(input('Horas: '))
minutos = int(input('Minutos: '))

linhas()

calcular_hora(horas, minutos)