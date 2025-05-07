def menu():
    while True:
        print("\n-----------------MENU-----------------")
        print("1 - Coca-Cola")
        print("2 - Pepsi")
        print("3 - Guaraná Antartica")

        opcao = input("\nEscolha seu refrigerante 350ML: ")

        if opcao == "1":
            print("\nCoca-Cola escolhida! ")
            print("Entregando refrigerante... ")
            print("Obrigado pela aquisição! ")
            break
        elif opcao == "2":
            print("\nPepsi escolhida! ")
            print("Entregando refrigerante... ")
            print("Obrigado pela aquisição! ")  
            break
        elif opcao == "3":
            print("\nGuaraná Antartica escolhido! ")
            print("Entregando refrigerante... ")
            print("Obrigado pela aquisição! ")
            break
        else:
            print("\nOpção inválida, por favor escolha 1, 2 ou 3.")

menu()