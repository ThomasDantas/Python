# classe soma, dois atributos v1 e v2, declarar dois objetos da classe soma, cada objeto recebe dois valores
# soma dos dois valores


class Soma:
    def __init__(self, v1, v2):
        self.valor1 = v1
        self.valor2 = v2

    def somar(self):
        print("soma dos valores, v1 e v2: ", self.valor1 + self.valor2)


valor1 = int(input("valor1: "))
valor2 = int(input("valor1: "))


res1 = Soma(valor1, valor2)
res1.somar()

