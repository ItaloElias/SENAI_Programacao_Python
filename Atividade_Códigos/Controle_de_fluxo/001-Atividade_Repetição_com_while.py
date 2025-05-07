senha_correta = 3143
while True:
    senha = int(input("\nDigite a senha para acessar: "))

    if senha == senha_correta:
        print("\nacesso permitido!\n")
        break
    elif senha < senha_correta:
        print("\nA senha é maior.")
    else:
        print("\nA senha é menor.")