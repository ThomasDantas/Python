from pessoa import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        super().__init__(nome, idade)
        self.cpf = cpf

    def getCPF(self):
        return self.cpf

    def setCPF(self, cpf):
        self.cpf = cpf
