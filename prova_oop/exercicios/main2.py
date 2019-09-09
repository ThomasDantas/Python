# bota
class Pai():
  def __init__(self, sobrenome):
    self.sobrenome = sobrenome


class Filha(Pai):
  def __init__(self, nome, sobrenome):
    super().__init__(sobrenome)  # foi passado o atributo para o construtor da classe mãe
    self.nome = nome  # aqui é setado o atributo específico da classe filha


  def getNome(self):
    return self.nome


filho1 = Filha("Maria", "Cardoso")
print(filho1.getNome())
