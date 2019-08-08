num1 = int(input("Informe um numero: "))
num2 = int(input("Informe outro numero: "))


def calc(num1, num2):
    if num1 > 0:
        op = int(input("Escolha uma das opcoes: 1- adicao, 2-subtracao, 3-multiplicacao e 4-divisao: "))
        if op == 1:
            soma = num1 + num2
            print("o resultado da soma é igual a: ", soma)
        elif op == 2:
            soma = num1 - num2
            print("o resultado da subtracao é igual a: ", soma)
        elif op == 3:
            soma = num1 * num2
            print("o resultado da multiplicacao é igual a: ", soma)
        elif op == 4:
            soma = num1 / num2
            print("o resultado da divisao é igual a: ", soma)
    else:
        print("Informar o primeiro numero maior que zero!")


calc(num1, num2)
