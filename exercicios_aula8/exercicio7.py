# pegar nome


arquivo = open("lista.txt", "r")

for linha in arquivo.readlines():
    print(str(linha.split("da")[0]))
arquivo.close()
