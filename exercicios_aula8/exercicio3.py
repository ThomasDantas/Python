# Faça um programa leia o arquivo numpar.txt encontre e liste os
# números múltiplos de 4.


arquivop = open('numerospar.txt', 'r')

for linha in arquivop.readlines():
    if int(linha) % 4 == 0:
        print(linha)

arquivop.close()
