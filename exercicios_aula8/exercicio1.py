# Faça um programa que gere os números de 1 a 500 e grava no
# arquivo numeros.txt e imprima o mesmo.


arquivo = open("exercicio1.txt", "w")
for linha in range(1, 501):
    arquivo.write("%d\n" % linha)
arquivo.close()


arquivo = open('exercicio1.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
