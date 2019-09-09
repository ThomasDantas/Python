from alimento import Alimento

class Lacteo(Alimento):
  def __init__(self, calorias, nome, quantidade_lactose, quantidade_gordura):
    super().__init__(calorias, nome)
    self.quantidade_lactose = quantidade_lactose
    self.quantidade_gordura = quantidade_gordura

  def setCalorias(self, calorias):
    self.calorias = calorias

  def setQuantidadeGordura(self, quantidade_gordura):
    self.quantidade_gordura = quantidade_gordura

  def getCalorias(self):
    return self.calorias

  def getNome(self):
    return self.nome