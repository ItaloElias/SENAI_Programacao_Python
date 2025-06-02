import statistics

def encontrar_maior(lista):
    return max(lista)

def encontrar_menor(lista):
    return min(lista)

while True:
    try:
        entrada = input("\nDigite uma lista de números separados por espaço: ")
        numeros = [float(num) for num in entrada.split()]

        if len(numeros) == 0:
            print("\nErro: A lista não pode estar vazia. Tente novamente.")
            continue

        media = statistics.mean(numeros)
        maior = encontrar_maior(numeros)
        menor = encontrar_menor(numeros)

        print(f"\nMédia: {media:.2f}")
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}\n")
        break 

    except ValueError:
        print("\nErro: Certifique-se de digitar apenas números válidos separados por espaço.")