# Faça um programa que leia o arquivo lista.txt
# e mostre todos os alunos que iniciem com a letra “G

arquivo = open("lista.txt", "r")

for linha in arquivo.readlines():
    if "g" in linha.split("da")[0]:
        print('tem: ', linha.split("da")[0])
    else:
        print("naotem")
    # print(linha)
arquivo.close()
