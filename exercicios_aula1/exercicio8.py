print('aluguel')

km = float(input('Quilometragem percorrida, R$ 0,15 o KM rodado: '))
dias = int(input('Dias de viagem, R$ 60 o dia: '))

al_km = km * 0.15
al_dias = dias * 60

print('Total Aluguel: ', al_dias + al_km)