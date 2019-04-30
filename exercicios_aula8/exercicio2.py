# Faça um programa que gere os números de 1 a 500 e grave no
# arquivo numpar.txt os números pares e numimpar.txt os números
# impares.

arquivop = open("numerospar.txt", "w")
arquivoi = open("numerosimpar.txt", "w")

for linha in range(1, 501):
    if linha % 2 == 0:
        arquivop.write("%d\n" % linha)
    elif linha % 3 == 0:
        arquivoi.write("%d\n" % linha)


arquivop.close()
arquivoi.close()
