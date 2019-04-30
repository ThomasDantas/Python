# Faça um programa que receba a distancia percorrida por um
# passageiro e calcule o valor da passagem, sendo que até 200 km é R$
# 0,50 o quilometro , de 201 km até 400 km é R$ 0,45 e acima de 400
# km é de R$ 0,40 calcule e mostre o valor da passagem conforme
# tabela acima.


dist = float(input("Informe a distancia percorrida: "))
print("ate 200km 0,50, 201km ate 400 0,45, maior de 400 0,40")

calc = 0

if dist <= 200:
    calc = dist*0.50
    print(calc)
elif dist >= 201 and dist <= 400:
    calc = dist * 0.45
    print(calc)
elif dist > 400:
    calc = dist * 0.40
    print(calc)
