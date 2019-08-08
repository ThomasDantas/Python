op = int(input("Para gravar digite 1, para mostrar os dados 2: "))


def gravar():
    contador = 0
    arquivo = open("lista.txt", "a")

    for i in range(1, 11):
        nome = input("Nome: ")
        cidade = input("Cidade: ")
        curso = int(input("Cursos Disponiveis = 1-Informática, 2-Química e 3-Biologia: "))

        if curso == 1:
            curso = 'Informatica'
            # contador = contador + 1
        elif curso == 2:
            curso = 'Quimica'
            # contador = contador + 1
        elif curso == 3:
            curso = 'Biologia'
            # contador = contador + 1
        else:
            print("Opcao Invalida!")

        frase = "Nome: {0} da Cidade de {1} e de Curso {2};".format(
            nome, cidade, curso)
        arquivo.write("\n" + str(frase))
    arquivo.close()


# gravar()


def mostrar_dados():
    arquivod = open("dados.txt", "a")
    arquivo = open("lista.txt", "r")

    for linha in arquivo.readlines():
        if "Informatica" in linha.split(";")[0]:
            tot = str(linha.split(";")[0])
            arquivod.write(str(tot) + "\n")
    inf = linha.count("Informatica")
    qui = linha.count("Quimica")
    bio = linha.count("Biologia")
    arquivod.write("%d\n" % int(inf))
    arquivod.write("%d\n" % int(qui))
    arquivod.write("%d\n" % int(bio))

    arquivo.close()
    arquivod.close()
# mostrar_dados()


if op == 1:
    gravar()
elif op == 2:
    mostrar_dados()
