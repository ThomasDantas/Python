L = [5, 6, 3, 7, 2, 7, 9, 35, 10, 15, 17, 7]

print(L)
if 28 in L:
    print('Sim, existe  o numero 28 na Lista')
else:
    print('Nao, existe  o numero 28 na Lista')

print('Soma da lista: ', sum(L))
print('menor valor da lista: ', min(L))
L.remove(15)
print('numero 15 removido: ', L)
print('tamanho da lista: ', len(L))
print('odem crescente: ', sorted(L))

