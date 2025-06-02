import time

def contagem_regressiva(inicio):
    while inicio > -1:
        print(inicio)
        time.sleep(1) 
        inicio -= 1
    print("Tempo esgotado!")

numero_inicial = int(input("Digite o número inicial para a contagem regressiva: "))
contagem_regressiva(numero_inicial)