import sqlite3
conexao = sqlite3.connect("brasil.db")
cursor = conexao.cursor()
total = 0
#

#----

cursor.execute("""update estados
                  set uf = 'RS'
                  where nome ='Rio Grande do Sul'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'SC'
                  where nome ='Santa Catarina'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'PR'
                  where nome ='Parana'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'RJ'
                  where nome ='Rio de Janeiro'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'SP'
                  where nome ='Sao Paulo'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'MG'
                  where nome ='Minas Gerais'""")

total = total + cursor.rowcount
cursor.execute("""update estados
                  set uf = 'BA'
                  where nome ='Bahia'""")

total = total + cursor.rowcount
cursor.execute("""update estados
                  set uf = 'ES'
                  where nome ='Espirito Santo'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'CE'
                  where nome ='Ceara'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'PB'
                  where nome ='Paraiba'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'RN'
                  where nome ='Rio Grande do Norte'""")
total = total + cursor.rowcount

cursor.execute("""update estados
                  set uf = 'PE'
                  where nome ='Pernambuco'""")
total = total + cursor.rowcount

print("Registros alterados: ", total)

conexao.commit()
cursor.close()
conexao.close()
