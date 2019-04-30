# Faça um programa leia o arquivo numimpar.txt encontre os
# números múltiplos de 3 e gere um novo arquivo multipl3.txt.


arquivom = open("imparMult3.txt", "w")
arquivoi = open("numerosimpar.txt", "r")

for linha in arquivoi.readlines():
    if int(linha) % 3 == 0:
        # print(linha)
        arquivom.write("%d\n" % int(linha))
arquivoi.close()
arquivom.close()

