class Person:
  def __init__(self, rg, nome, idade, endereco):
    self.rg = rg
    self.name = nome
    self.age = idade
    self.address = endereco

  def listar(self):
    print("rg: ", self.rg)
    print("nome: ", self.name)
    print("idade: ", self.age)
    print("endereco: ", self.address)

  def alterar(self, rg, name, age, address):
    self.rg = rg
    self.name = name
    if age < self.age:
      print("idade menor que a outra")
    else:
      self.age = age
    self.address = address
    self.listar()


print("cadastrar primeira pessoa")
rg = input("digite o seu rg: ")
name = input("digite seu nome: ")
age = int(input("digite sua idade: "))
address = input("seu endereco: ")

l1 = Person(rg, name, age, address)
l1.listar()

print("cadastrar segunda pessoa")
rg2 = input("digite o seu rg: ")
name2 = input("digite seu nome: ")
age2 = int(input("digite sua idade: "))
address2 = input("seu endereco: ")

l2 = Person(rg2, name2, age2, address2)
l2.listar()

print("alterar dados pesoa 1: ")
rg = input("digite o seu rg: ")
name = input("digite seu nome: ")
age = int(input("digite sua idade: "))
address = input("seu endereco: ")

l1.alterar(rg, name, age, address)
