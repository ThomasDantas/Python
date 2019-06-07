import sqlite3

conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()
opc = int(input("1- Consulta Ordem Alfabetica 2-Consulta Ordem população: "))

if opc == 1:

    banco.execute("select nome , populacao  from estados order by nome")
else:
    banco.execute("select nome , populacao  from estados order by populacao")

resultado = banco.fetchall()
for registro in resultado:
    print(" Estado: {0} -  População: {1}".format(registro[0], registro[1]))

banco.close()
conexao.close()
