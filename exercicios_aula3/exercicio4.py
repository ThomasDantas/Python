print("Escreva um programa para encontrar a soma S = 3 + 6 + 9 +…. +333, escreva a média dos numeros")

soma=0
qtd=0

for x in range(1, 334):
    if x % 3 == 0:
        soma += x
        qtd += 1
print("Soma = ", soma)
print("Quantidade = ", qtd)
print("Media = ", soma/qtd)