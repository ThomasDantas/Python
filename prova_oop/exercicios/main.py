from lacteo import Lacteo
from bebida import Bebida

caloriasA = input("calorias: ")
nome = input("nome: ")
quantidade_lactose = input("lactose: ")
quantidade_gordura = input("gordura: ")

lacteo = Lacteo(caloriasA, nome, quantidade_gordura, quantidade_lactose)
lacteo.setCalorias(caloriasA)
lacteo.setQuantidadeGordura(quantidade_gordura)

print(lacteo.getCalorias())
print(lacteo.getNome())

nome = input("nome: ")
caloriasB = input("calorias: ")
quantidade_acucar = input("quantidade acucar: ")
quantidade_ml = input("ml: ")

bebida = Bebida(nome, caloriasB, quantidade_acucar, quantidade_ml)
bebida.setCalorias(caloriasB)

bebida.setQuantidadeAcucar(quantidade_acucar)
bebida.setCalorias(caloriasB)
print(bebida.getCalorias())
print(bebida.getQuantidadeAcucar())


