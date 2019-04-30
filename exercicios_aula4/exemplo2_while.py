senha = "9876"
senha_dig = ""

while senha_dig != senha:
    senha_dig = input("Digite a senha: ")
    if senha == senha_dig:
        print("Acesso Liberado")
    else:
        print("Senha Invalida!")
