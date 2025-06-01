# Importa as classes necessárias do arquivo produto.py
from produto import ProdutoNacional, ProdutoImportado, FuncionarioCLT, FuncionarioPJ

def main():
    # Cadastro de produtos (lista com dois produtos: um nacional e um importado)
    produtos = [
        ProdutoNacional("Teclado", 150.0, 10),
        ProdutoImportado("Celular", 2000.0, 5, 0.40)  # 40% de taxa de importação
    ]

    print("=== Detalhes dos Produtos e Notas Fiscais ===")
    for p in produtos:
        p.exibir_detalhes()                  # Mostra nome, preço e estoque
        print(f"Preço final: R${p.preco_final()}")  # Mostra o preço final (com ou sem taxa)
        p.emitir_nota()                      # Emite nota conforme o tipo de produto
        print("--------------------------------------")

    # Cadastro de funcionários (um CLT e um PJ)
    funcionarios = [
        FuncionarioCLT("Alice", 3000.0),         # Salário fixo
        FuncionarioPJ("Bob", 160, 25.0)          # 160h * R$25/hora
    ]

    print("\n=== Pagamento dos Funcionários ===")
    for f in funcionarios:
        print(f"{f.nome}: R${f.calcular_pagamento()}")  # Mostra pagamento conforme o tipo

    # Operações de estoque: venda e reposição
    print("\n=== Operações de Estoque ===")
    produtos[0].vender(3)     # Vende 3 unidades do primeiro produto (Teclado)
    produtos[1].repor(5)      # Reposição de 5 unidades do segundo produto (Celular)

# Executa o main se o arquivo for rodado diretamente
if __name__ == '__main__':
    main()
