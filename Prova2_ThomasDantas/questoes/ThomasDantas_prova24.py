

def senha():
    usuario = input("Digite o usuario: ")
    senha = input("Digita a senha: ")

    if len(senha) >= 8:
        if senha.isupper() or senha.isalnum():
            if not "@#$%&*":
                print("Senha aceita")
        else:
            print("Deve ter somente letras minusculas e numeros")
    elif senha == "fim":
        print("Fim")
    else:
        print("mais de 8 caracteres")


senha()

