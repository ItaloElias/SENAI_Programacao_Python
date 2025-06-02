import random

print("Vamos jogar contra o Froid! \n")
def par_ou_impar(numero):
    return "par" if numero % 2 == 0 else "ímpar"

def jogar():
    while True:
        escolha = input("Escolha par ou ímpar: ").strip().lower()
        if escolha not in ["par", "ímpar", "impar"]:
            print("Erro: escolha deve ser 'par' ou 'ímpar'. Tente novamente.")
            continue

        if escolha == "impar":
            escolha = "ímpar"

        try:
            usuario_numero = int(input("Digite um número entre 0 e 10: "))
            if not 0 <= usuario_numero <= 10:
                print("Erro: número deve ser entre 0 e 10. Tente novamente.")
                continue
        except ValueError:
            print("Erro: digite um número válido.")
            continue

        computador_numero = random.randint(0, 10)
        soma = usuario_numero + computador_numero
        resultado = par_ou_impar(soma)

        print(f"\nVocê escolheu {usuario_numero} e o Froid escolheu {computador_numero}.\n")
        print(f"Soma = {soma}, que é {resultado}.")

        if escolha == resultado:
            print("\nVocê venceu!")
        else:
            print("\nFroid venceu e você perdeu :(")
        break

jogar()