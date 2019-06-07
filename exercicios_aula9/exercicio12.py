import sqlite3
conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()
print("Região  Num UF      População      Minina     Maxima     Media      Total ")
print("======  =========               =========  ==========  =========  ========== ")

banco.execute('select regiao , count(*), min(populacao), max(populacao), '
              'avg (populacao), sum(populacao) as  tot_pop from estados '
              'group by regiao order by tot_pop')
resultado = banco.fetchall()
for registro in resultado:
    print("{0:6} {1:4} {2:30,} {3:10,} {4:10,.0f} {5:13,}".format(*registro))

banco.close()
conexao.close()
