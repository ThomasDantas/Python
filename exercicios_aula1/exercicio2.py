print('calculadora')

val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
res = val1+val2
traco = '-'

print('A soma entre {} e {} é igual a {}'.format(val1, val2, res))
print(traco*50)
print('A subtracao entre {} e {} é igual a {}'.format(val1, val2, val1-val2))
print(traco*50)
print('A divisao inteira entre {} e {} é igual a {}'.format(val1, val2, val1//val2))
print(traco*50)
print('A multiplicacao entre {} e {} é igual a {}'.format(val1, val2, val1*val2))
print(traco*50)
print('A potencia entre {} e {} é igual a {}'.format(val1, val2,val1**val2))
print(traco*50)
print('O resto da divisao entre {} e {} é igual a {}'.format(val1, val2,val1 % val2))
print(traco*50)
