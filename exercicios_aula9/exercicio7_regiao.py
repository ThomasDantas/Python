import sqlite3
conexao = sqlite3.connect("brasil.db")
cursor = conexao.cursor()
total = 0
cursor.execute("""update estados
                  set regiao = 'Sul'
                  where uf ='RS'""")
total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Sul'
                  where nome ='Santa Catarina'""")
total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Sul'
                  where nome ='Parana'""")
total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Sudeste'
                  where nome ='Rio de Janeiro'""")
total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Sudeste'
                  where nome ='Sao Paulo'""")
total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Sudeste'
                  where nome ='Espirito Santo'""")

total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Sudeste'
                  where nome ='Minas Gerais'""")

total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Nordeste'
                  where nome ='Bahia'""")

total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Nordeste'
                  where nome ='Paraiba'""")

total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Nordeste'
                  where nome ='Pernambuco'""")

total = total + cursor.rowcount
cursor.execute("""update estados
                  set regiao = 'Nordeste'
                  where nome ='Cear�'""")

total = total + cursor.rowcount

cursor.execute("""update estados
                  set regiao = 'Nordeste'
                  where nome ='Rio Grande do Norte'""")
total = total + cursor.rowcount

print("Registros alterados: ", total)
conexao.commit()
cursor.close()
conexao.close()
