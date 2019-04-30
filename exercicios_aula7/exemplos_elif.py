categoria = int(input("Informe categoria: "))

if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 18
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 26
else:
    print("categoria invalida")
    preco = 0

print("O preço do produto é: R$%6.2f" % preco)
