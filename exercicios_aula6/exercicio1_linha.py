# Crie uma função para desenhar uma linha, usando o
# caractere '_'.
# O tamanho da linha será definido na chamada da função.


def linha():
    tam_linha = int(input("Informe o tamanho da linha: "))
    l = '_'
    calc = 0

    calc = l * tam_linha
    print(calc)


linha()
