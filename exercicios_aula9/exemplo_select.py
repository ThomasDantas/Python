import sqlite3

conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute("select * from agenda")

resultado = cursor.fetchall()
print("Nome: %s\nTelefone: %s" % (resultado[0]))

cursor.close()
conexao.close()
