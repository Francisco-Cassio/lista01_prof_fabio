from funcao_linha import linhas

def calcular_velocidade(vel_km):
    vel_ms = vel_km / 3.6
    
    print(f'{vel_km:.1f} km/h equivale a\n>>>>> {vel_ms:.1f} m/s <<<<<')


vel_km = float(input('Velocidade (km/h): '))

linhas()

calcular_velocidade(vel_km)


