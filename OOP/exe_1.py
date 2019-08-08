class Person:                          #nome Classe

  def __init__(self, name, age):       #método construtor
    self.name = name                   #atributo
    self.age = age


p1 = Person("John", 36)                #instanciação do objeto P1 a partir da Classe Person


print(p1.name)
print(p1.age)
