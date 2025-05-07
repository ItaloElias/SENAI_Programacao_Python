def main():
    while True:

        print("\nMenu de Operações:")
        print("\n1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair\n")


        opcao = input("Escolha uma operação: ")

        if opcao == '5':
            print("Saindo do programa...\n")
            break  

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue  

        if opcao == '1':
            resultado = num1 + num2
            print(f"\n soma de {num1} + {num2} é {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(f"\nA subtração de {num1} - {num2} é {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(f"\nA multiplicação de {num1} * {num2} é {resultado}")
        elif opcao == '4':
            if num2 == 0:
                print("\nErro: Não é possível dividir por zero.")
            else:
                resultado = num1 / num2
                print(f"\nA divisão de {num1} / {num2} é {resultado}")
        else:
            print("\nOpção inválida, por favor escolha uma opção válida (1-5).")
            
if __name__ == "__main__":
    main()