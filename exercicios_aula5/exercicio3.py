print("feirao de carros")

marca = input("Marca: ")
modelo = input("Modelo: ")
desconto = int(input("Desconto: "))
dia = input("Dia limite da promoção: ")

frase = "Feirão de automóveis: Toda linha {0} com desconto de {1} % nos modelos {2}! Promoção valida até {3}!"
print(frase.format(marca, modelo, desconto, dia))




