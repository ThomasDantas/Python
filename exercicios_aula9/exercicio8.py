import sqlite3

conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()

nome = input("Região a Consultar:")
flag = 0
banco.execute('select nome,uf, populacao, regiao from estados where regiao = "%s"' % nome)

while True:
    registro = banco.fetchone()
    if registro is None:
        break
        # flag = 9
        print("Região não existe no Banco de Dados")
    else:

        print(" Estado: {0} -  UF: {1} - Populaçao: {2} - Regiao: {3}".format(registro[0], registro[1], registro[2],
                                                                              registro[3]))

banco.close()
conexao.close()
