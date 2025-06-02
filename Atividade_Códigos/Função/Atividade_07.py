def calcular_notas(valor):
    notas = {100: 0, 50: 0, 20: 0, 10: 0, 2: 0} 

    for nota in notas.keys():
        notas[nota] = valor // nota 
        valor %= nota 

    return notas

while True:
    try:
        valor = int(input("Digite o valor para sacar: R$ "))
        
        if valor <= 0:
            print("\nErro: O valor deve ser maior que zero. Tente novamente.")
            continue

        notas = calcular_notas(valor)

        print("\nNotas necessárias para compor o valor:")
        for nota, quantidade in notas.items():
            if quantidade > 0:
                print(f"R${nota}: {quantidade} notas")

        break 

    except ValueError:
        print("\nErro: Por favor, digite um valor numérico válido.")