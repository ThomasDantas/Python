# classe soma, dois atributos v1 e v2, declarar dois objetos da classe soma, cada objeto recebe dois valores
# soma dos dois valores

class Soma:
    def __init__(self, v1, v2):
        self.valor1 = v1
        self.valor2 = v2

    def somar(self):
        print("soma dos valores, v1 e v2: ", self.valor1 + self.valor2)


res1 = Soma(10, 10)
res1.somar()

res2 = Soma(15, 56)
res2.somar()
