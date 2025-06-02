def converter_conceito(nota):
    if 90 <= nota <= 100:
        return 'A'
    elif 80 <= nota <= 89:
        return 'B'
    elif 70 <= nota <= 79:
        return 'C'
    elif 60 <= nota <= 69:
        return 'D'
    elif 0 <= nota <= 59:
        return 'F'
    else:
        return 'Nota inválida'

while True:
    try:
        nota = float(input("\nDigite a nota (0 a 100): "))
        if 0 <= nota <= 100:
            conceito = converter_conceito(nota)
            print(f"\nO conceito correspondente é: {conceito}\n")
            break 
        else:
            print("\nPor favor, digite um valor entre 0 e 100.")
    except ValueError:
        print("\nEntrada inválida! Por favor, digite apenas números.")
