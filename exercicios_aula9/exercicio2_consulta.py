import sqlite3
conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()
opc = int(input("1- Consulta Tabela 2- Consulta Individual: "))

if opc == 1:
    banco.execute("select *  from estados")
    resultado=banco.fetchall()
    for registro in resultado:
       #  print("Estado: %s\nPopula��o: %s" % (registro))
        print(" Estado: {0} -  População: {1}".format(registro[1], registro[2]))

    banco.close()
    conexao.close()
else:
    nome = input("Estado a Consultar:")
    flag = 0
    banco.execute('select nome, populacao from estados where nome = "%s"' % nome)

    while True:
        resultado = banco.fetchone()
        if resultado is None:
            break
            flag = 9
            print("Estado não existe no Banco de Dados")
        else:
            #print("Estado: %s\nPopula��o: %s" % (resultado))
            print(" Estado: {0} -  População: {1}".format(resultado[0], resultado[1]))
            break

    banco.close()
    conexao.close()
