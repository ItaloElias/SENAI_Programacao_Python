def calcular_frete(peso):
    if peso <= 1:
        return 10
    elif peso <= 5:
        return 20
    else:
        return 30

peso = float(input("\nDigite o peso da encomenda em kg: "))
valor = calcular_frete(peso)
print(f"\nO valor do frete é: R$ {valor}\n")