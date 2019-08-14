from pessoaf import PessoaFisica
from pessoaj import PessoaJuridica


print("PessoaFisicca")
nome = input("nome: ")
idade = input("idade: ")
cpf = input("cpf: ")
a = PessoaFisica(cpf, nome, idade)
print("\nnome: ", a.getNome())
print("idade: ", a.getIdade())
print("cpf", a.getCPF())


print("\nPessoaJuridica")
nome = input("nome: ")
idade = input("idade: ")
cnpj = input("cnpj: ")
b = PessoaJuridica(cnpj, nome, idade)
print("\nnome: ", b.getNome())
print("idade: ", b.getIdade())
print("cnpj: ", b.getCNPJ())


idade = input("\nMudar idade PessoaFisica: ")
a.setIdade(idade)
print(a.getIdade())

cnpj = input("\nMudar cnpj PessoaJuridica: ")
b.setCNPJ(cnpj)
print(b.getCNPJ())
