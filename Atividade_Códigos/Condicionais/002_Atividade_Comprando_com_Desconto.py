valor_da_compra = float(input("Valor da compra: R$"))

if valor_da_compra > 100:
    print(f"Desconto aplicado! valor final: R${valor_da_compra-10}")
else:
    print(f"Sem desconto aplicado! Valor final: R${valor_da_compra}")