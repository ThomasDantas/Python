import sqlite3
conexao = sqlite3.connect("brasil.db")
banco = conexao.cursor()
banco.execute("alter table estados ADD uf text ")
banco.execute("alter table estados ADD regiao text ")
print("Tabela estados foi alterada com sucesso")
conexao.commit()
conexao.close()
