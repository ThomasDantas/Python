from notebook import Notebook
from desktop import Desktop

computador = Notebook('dy', '8GB', '4T', 'Sei la', '21º')
computador1 = Notebook('acer', '4GB', '1T', 'HUM', '17º')

desktop = Desktop('acer', '8GB', '120GB', 'DELL')
desktop1 = Desktop('acer', '8GB', '120GB', 'DELL', 29)


# print("PRIMEIRO PC")
# print(computador.getFabricante())
# print(computador.getQuantidade_ram())
# print(computador.getTamanho_ssd())
# print(computador.getModelo())
# print(computador.getTela(), "\n")
#
# print("SEGUNDO PC")
# print(computador1.getFabricante())
# print(computador1.getQuantidade_ram())
# print(computador1.getTamanho_ssd())
# print(computador1.getModelo())
# print(computador1.getTela())


print("DESKTOP 1")
print("tamanho", desktop.getMonitor())
print("marca", desktop.getMarca(), "\n")


print("DESKTOP 2")
print("tamanho", desktop1.getMonitor())
print("marca", desktop1.getMarca())


