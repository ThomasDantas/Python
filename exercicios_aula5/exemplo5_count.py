print("contar quantas palavras existem dentro da string")

frase="Um tigre, dois tigres, três tigres, vários tigres"
print(frase)

print("numero de palavras tigre: ", frase.count("tigre"))

print("--------------------------------------------------------")

print("Exemplinho xd")

frase = "Um tigre, dois tigres, tres tigres, varios tigres"
print("Total palavra tigre=", frase.count("tigre"))
print("Total palavra tigres=",frase.count("tigres"))

p = 0
while p > -1:
    p = frase.find("tigre", p)
    if p >= 0:
        print("Posicao: %d" % p)
        p += 1
