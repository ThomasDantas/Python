print("Gere uma lista contendo os múltiplos de 3 entre 1 e 100")

lista=[]

for x in range(1, 100):
    if (x % 3 == 0):
        lista.append(x)
print(lista)