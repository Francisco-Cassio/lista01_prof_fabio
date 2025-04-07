from funcao_linha import linhas

def conversao(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg = segundos % 60

    print(f'{segundos} segundos equivale a\n>>>>> {horas} hora(s), {minutos} minuto(s) e {seg} segundo(s) <<<<<')


segundos = int(input('Segundos: '))
linhas()

conversao(segundos)