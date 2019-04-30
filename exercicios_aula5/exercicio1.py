print("receber duas strings e ver se uma esta dentro da outra")

frase1 = input("Digite uma frase: ")
frase2 = input("Digite outra frase: ")

if frase2 in frase1:
    print("Existe frase 2 dentro da 1")
    print(frase1.find(frase2))
else:
    print("Nao frase 2 dentro da 1")
