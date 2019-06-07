import sqlite3
conexao = sqlite3.connect("brasil.db")
cursor = conexao.cursor()


cursor.execute("\n"
              "       create table estados(\n"
              "           id integer primary key autoincrement,\n"
              "           nome text,\n"
              "           populacao integer);\n"
              "       ")


dados = [("Rio Grande do Sul", "3550340"),
("Santa Catarina", "1230450"),
("Parana", "2500600"),
("Rio de Janeiro", "1500600"),
("Sao Paulo", "7600400"),
("Bahia", "2888600"),
("Pernambuco", "2300890"),
("Espirito Santo", "1350090"),
("Ceará", "1500000"),
("Paraiba", "900890"),
("Rio Grande do Norte", "890000"),
("Minas Gerais", "3500600")
          ]
cursor.executemany('''
insert into estados (nome, populacao)
values(?, ?) ''', dados)

conexao.commit()
cursor.close()
conexao.close()
print("Tabela estados foi criada com sucesso !")
