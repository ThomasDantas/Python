import sqlite3

conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()

nome = input("Estado a Consultar:")
flag = 0
banco.execute('select nome,uf, populacao from estados where uf = "%s"' % nome)

while True:
        resultado = banco.fetchone()
        if resultado is None:
            print("Estado não existe no Banco de Dados")
            break
            flag = 9
        else:
            print("Estado: %s\nUF: %s\nPopulação: %s" % resultado)
            break
banco.close()
conexao.close()
