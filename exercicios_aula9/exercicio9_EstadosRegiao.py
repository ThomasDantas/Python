import sqlite3

conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()

banco.execute('select regiao , count (uf) as tot_estado from estados group by regiao')
resultado = banco.fetchall()
for registro in resultado:
    print("Região: %s - Total de Estados: %s" % registro)

banco.close()
conexao.close()
