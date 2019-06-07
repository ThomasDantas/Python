import sqlite3

conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()
print("Região População Total  ")
print("====== ================= ")

banco.execute('select regiao , sum(populacao) as  tot_pop from estados '
              'group by regiao order by tot_pop ')
resultado = banco.fetchall()
for registro in resultado:
    print("{0:6} {1:5} ".format(*registro))

banco.close()
conexao.close()
