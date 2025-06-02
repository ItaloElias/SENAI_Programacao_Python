import re

def validar_senha(senha):
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    if not re.search(r'[A-Z]', senha):
        return "A senha deve conter pelo menos uma letra maiúscula."
    
    if not re.search(r'[0-9]', senha):
        return "A senha deve conter pelo menos um número."
    
    return "Senha válida!"

while True:
    senha = input("Digite uma senha: ")
    resultado = validar_senha(senha)
    
    if resultado == "Senha válida!":
        print(resultado)
        break  
    else:
        print(resultado)
        print("Tente novamente.\n")
