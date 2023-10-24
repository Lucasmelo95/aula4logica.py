while True:
    nome = str(input("Digite seu nome: "))
    senha = str(input("Digite sua senha: "))

    if nome != senha:
        break
    else:
        print("Nome e senha nao pode ser iguais! ")