

def fras():
    frase = "O pinto pia, pipa pinga. Pinga a pipa e o pinto pia. Quanto mais o pinto pia mais a pipa pinga"

    print("Total palavra pinto=", frase.count("pinto"))

    p = 0
    while p > -1:
        p = frase.find("pinto", p)
        if p >= 0:
            print("Posicao da palavra pinto: %d" % p)
            p += 1

    print(frase.replace('pinto', 'galo'))

    maius = []
    p = ['da', 'de', 'di', 'do', 'du', 'para']  # preposição
    for palavras in frase.split():
        if not palavras in p:
            palavras = palavras.capitalize()
            maius.append(palavras)
    print(' '.join(maius))

    # print("Maiusculo: ", frase.upper())


fras()
