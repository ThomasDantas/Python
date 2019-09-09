from alimento import Alimento

class Bebida(Alimento):
  def __init__(self, nome, quantidade_ml, quantidade_acucar, calorias):
    super().__init__(calorias, nome)
    self.quantidade_ml = quantidade_ml
    self.quantidade_acucar = quantidade_acucar

  def setCalorias(self, calorias):
    self.calorias = calorias

  def setQuantidadeAcucar(self, quantidade_acucar):
    self.quantidade_acucar = quantidade_acucar

  def getCalorias(self):
    return self.calorias

  def getQuantidadeAcucar(self):
    return self.quantidade_acucar

