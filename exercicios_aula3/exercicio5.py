print("materiais")

M = {
    "Caderno": 8.50,
    "Mochila": 36.50,
    "Caneta": 3.00,
    "Folha A4": 9.50,
    "Lapiseira": 12.00
}

print("1", M)

M["Régua"]=5.00
print("2", M)

print("3", "Mochila" in M)

print("4", M["Caneta"])

print("5", M.keys())

del M["Caneta"]
print("6", M)
