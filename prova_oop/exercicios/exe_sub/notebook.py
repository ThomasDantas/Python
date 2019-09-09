from computador import Computador


class Notebook(Computador):
  def __init__(self, fabricante, quantidade_ram, tamanho_ssd, modelo, tela):
    super().__init__(fabricante, quantidade_ram, tamanho_ssd)
    self.modelo = modelo
    self.tela = tela

  def setFabricante(self, fabricante):
    self.fabricante = fabricante

  def setQuantidade_ram(self, quantidade_ram):
    self.quantidade_ram = quantidade_ram

  def setTamanho_ssd(self, tamanho_ssd):
    self.tamanho_ssd = tamanho_ssd

  def setModelo(self, modelo):
    self.modelo = modelo

  def setTela(self, tela):
    self.tela = tela

  def getFabricante(self):
    return self.fabricante

  def getQuantidade_ram(self):
    return self.quantidade_ram

  def getTamanho_ssd(self):
    return self.tamanho_ssd

  def getModelo(self):
    return self.modelo

  def getTela(self):
    return self.tela