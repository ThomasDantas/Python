import sqlite3

conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()

banco.execute('select nome, uf, regiao , max (populacao) as tot_pop from estados ')
resultado = banco.fetchall()
for registro in resultado:
    print("Estado mais Populoso")
    print("Estado: %s - UF: %s - Regiao: %s - Populacao: %s" % registro)

banco.execute('select nome, uf, regiao , min (populacao) as tot_pop from estados ')
resultado = banco.fetchall()
for registro in resultado:
    print("Estado menos Populoso")
    print("Estado: %s - Regiao: %s - Regiao: %s - Populacao: %s" % registro)

banco.close()
conexao.close()
