print("Lancheria")

L = {
    "Cachorro Quente": 15.50,
    "Refrigerante": 8.00,
    "X Salada": 18.00,
    "Torrada": 9.50,
    "Batata Frita": 12.00
}

for i in L:
    print("Produto", " ------------------ ", "Valor\n", i, '--------------', L[i], '\n')

L["Agua mineral"] = 5.00
print(L)
print("Torrada esta na lista?", "Torrada" in L)
print('Valor X Salada: ', L['X Salada'])
print('Todas Chaves: ', L.keys())
del L["Refrigerante"]
print(L)