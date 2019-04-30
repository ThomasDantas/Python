print('Pagar Imposto')

nome = input('Nome do Cliente: ')
i = int(input('Idade: '))
cidade = input('Cidade: ')
curso = input('Qual curso Deseja: ')
s = float(input('Digite seu salario: '))

if s < 2300:
    print('Voce nao Deve pagar impostos')
else:
    print('Voce deve pagar impostos')


print( "\n", nome, "\n", i, "\n", cidade, "\n", curso)