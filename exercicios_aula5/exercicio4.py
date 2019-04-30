print("senha")

senha = input("Digita a senha: ")

if senha.isupper() or senha.isdigit():
    print("valid")
else:
    print("invalid")
