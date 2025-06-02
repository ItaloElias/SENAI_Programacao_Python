import re

def gerar_email(nome_completo):
    nome_parts = nome_completo.strip().split()
    if len(nome_parts) < 2:
        raise ValueError("Nome completo deve ter pelo menos um primeiro nome e um sobrenome.")
    
    primeiro_nome = nome_parts[0].lower()
    sobrenome = nome_parts[-1].lower()

    email = f"{primeiro_nome}.{sobrenome}@escola.com"
    return email

while True:
    try:
        nome_completo = input("Digite o nome completo do aluno: ")

        if len(nome_completo.strip().split()) < 2:
            print("\nErro: Nome completo deve ter pelo menos um primeiro nome e um sobrenome.")
            continue

        email = gerar_email(nome_completo)
        print(f"\nE-mail gerado: {email}")
        break 

    except ValueError as e:
        print(f"\nErro: {e}")