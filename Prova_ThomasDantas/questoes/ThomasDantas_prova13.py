nome = input("Informe o nome do Produto: ")
codigo = int(input('Informe o código: '))
valor = float(input('Valor do Produto: '))
desc = float(input('Percentagem do desconto %: '))

soma = valor - ((valor*desc) /100)

print("Produto:", nome, "Código: %03d Valor: %3.2f Desconto: %02d Novo Valor: %3.2f" % (codigo, valor, desc, soma))

