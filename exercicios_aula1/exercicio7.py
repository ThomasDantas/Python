print('Aumento de salario trabalhador')

nome = input('Nome do funcionario: ')
salario = float(input('Salario: '))
por_aum = float(input('Porcentagem aumento de salario: '))

aum = por_aum / 100
new_salario = (salario * aum) + salario

print("Nome: ", nome)
print('Salario Antigo: ', salario)
print('Novo salario: ', new_salario)