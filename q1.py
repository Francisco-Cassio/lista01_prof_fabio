from funcao_linha import linhas

def calcular_velocidade(vel_ms):
    vel_kh = vel_ms * 3.6
    
    print(f'{vel_ms:.1f} m/s equivale a\n>>>> {vel_kh:.1f} km/h <<<<')


vel_ms = float(input('Velocidade (m/s): '))

linhas()

calcular_velocidade(vel_ms)