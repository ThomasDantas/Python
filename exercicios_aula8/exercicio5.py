# Faça um programa que receba o nome, cidade e o curso de
# 10 alunos. Salve esses dados no arquivo lista.txt.
# Todas as informações referentes a um aluno devem estar na mesma
# linha separadas por ponto e virgula “;”


arquivo = open("lista.txt", "a")

for i in range(1, 3):
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    curso = input("Curso: ")

    frase = "Lista de alunos: nome {0} da cidade {1} e de curso {2};".format(
        nome, cidade, curso)
    arquivo.write("\n" + str(frase))
arquivo.close()
