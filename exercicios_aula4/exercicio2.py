print("notas dos alunos em uma lista")

EREGES = {
    "Mateus": 7,
    "Rambo": 10,
    "Thomas": 6,
    "Gustavo": 5,
    "Lucas": 8}

media = 0
nota = 0
print(EREGES)

for x in EREGES:
    media += EREGES[x]
    if int(EREGES[x]) > nota:
        nota = int(EREGES[x])

print("Nota mais alta: ", nota)
print("Média: ", media/5)
