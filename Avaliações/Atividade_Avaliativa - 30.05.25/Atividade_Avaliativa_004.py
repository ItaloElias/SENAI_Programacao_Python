while True:
    numero = int(input("\nDigite um número: "))


    if numero % 2 == 0:
        print(f"\nO número {numero} é PAR!")
    else:
        print(f"\nO número {numero} é ÍMPAR!")
    
    while True:
        continuar = input("\nDeseja testar outro número? (S/N): ").strip().upper()
       
        if continuar == 'S' or continuar == 'N':
            break  
        else:
            print("Resposta inválida! Por favor, digite 'S' para sim ou 'N' para não.")
    
    if continuar == 'N':
        print("\nObrigado por utilizar esta aplicação!\n")
        break