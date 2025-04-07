from funcao_linha import linhas

def conversao(horas):
    semanas = horas // 168
    dias = (horas % 168) // 24
    hours = horas % 24

    print(f'{horas} horas equivale a\n>>>>> {semanas} semana(s), {dias} dia(s) e {hours} hora(s) <<<<<')


horas = int(input('Horas: '))
linhas()

conversao(horas)