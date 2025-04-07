from funcao_linha import linhas

def comprimento_circunferencia(raio):
    pi = 3.14
    circ = 2 * pi * raio

    print(f'Comprimento da circunferência:\n>>>>>>>>> {circ:.2f}m <<<<<<<<<')


raio = float(input('Raio: '))

linhas()

comprimento_circunferencia(raio)