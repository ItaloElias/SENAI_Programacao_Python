def converter_celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F.")

def calcular_idade():
   
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = 2025 
    idade = ano_atual - ano_nascimento
    print(f"Você tem {idade} anos.")

def menu():
    while True:
        print("\n-----------------MENU-----------------")
        print("1 - Converter Celsius para Fahrenheit")
        print("2 - Calcular idade (ano nascimento)")
        print("3 - Sair\n")

        opcao = input("Digite o numero que melhor te atende: ")

        if opcao == "1":
            converter_celsius_para_fahrenheit()
            break
        elif opcao == "2":
            calcular_idade()
            break
        elif opcao == "3":
            print("\nAté logo!\n")
            break
        else:
            print("Opção inválida, por favor escolha 1, 2 ou 3.")

menu()