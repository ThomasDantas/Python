# Faça um programa que leia o arquivo lista.txt
# e mostre todos os alunos que iniciem com a letra “G

arquivo = open("lista.txt", "r")

for linha in arquivo.readlines():
    linha.split("nome")[0]
    if "g" in linha:
        print('tem')
    else:
        print("naotem")
    # print(linha)
arquivo.close()
