num = int(input("Digite um numero menor que 11, e veja: "))
t = 1

op = int(input('Opcao 1 - Tabuada, 2 - Fatorial: '))

if op == 1:
    while num != 0:
        for i in range(1, 11):
            print(i, "x", num, '=', num*i)
            i = i+1

        num = int(input("Digite outro numero menor que 11, e veja a tabuada: "))

elif op == 2:
    while num != 0:
        fat = 1
        i = 2
        while i <= num:
            fat = fat * i
            i = i + 1
            print("Fatorial do Numero ", num, " = ", fat)

        num = int(input("Digite outro numero menor que 11, e veja o fatorial: "))
