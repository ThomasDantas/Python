print('loja de venda')

nome = input('Nome do produto: ')
codigo = int(input('Codigo: '))
valor_produto = float(input('Valor produto: '))
desconto = int(input('% de Desconto: '))

dec = desconto / 100
calculo = valor_produto - (valor_produto * dec)

print('Codigo: ', '%03d' % codigo)
print('Nome: ', nome)
print('Preco: ', '%03.1f' % valor_produto)
print('Desconto: ', '%02d' % desconto)
print('Preco de venda: ', calculo)

