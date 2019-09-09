from computador import Computador


class Desktop(Computador):
  def __init__(self, fabricante, quantidade_ram, tamanho_ssd, marca_monitor, tamanho_monitor=21):
    super().__init__(fabricante, quantidade_ram, tamanho_ssd)
    self.tamanho_monitor = tamanho_monitor
    self.marca = marca_monitor


  def setTamanhoMonitor(self, tamanho_monitor):
    self.tamanho_monitor = tamanho_monitor

  def setMarca(self, marca):
    self.marca = marca

  def getMonitor(self):
    return self.tamanho_monitor

  def getMarca(self):
    return self.marca
