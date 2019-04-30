print("tabuada dos numeros, 0 fecha o programa")

num = int(input("Digite um numero menor que 11, e veja a TABUADA: "))
t = 1

while num != 0:
    for i in range(1, 11):
        print(i, "x", num, '=', num*i)
        i = i+1

    num = int(input("Digite um numero menor que 11, e veja a TABUADA: "))

print("INFERNO DEU ERRO")
