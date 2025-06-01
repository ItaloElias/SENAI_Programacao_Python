import abc  # Módulo para criar classes abstratas

# Classe base Produto
class Produto:
    # Construtor da classe Produto
    def __init__(self, nome, preco, estoque):
        self.nome = nome                  # Nome do produto
        self.preco = preco                # Preço base do produto
        self.estoque = estoque            # Quantidade em estoque

    # Exibe os detalhes do produto formatados
    def exibir_detalhes(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco} | Estoque: {self.estoque} unidades")

    # Retorna o preço final (sem alterações)
    def preco_final(self):
        return self.preco

    # Emite nota genérica
    def emitir_nota(self):
        print(f"Nota gerada para {self.nome}.")

    # Reposição de estoque
    def repor(self, quantidade):
        self.estoque += quantidade
        print(f"Reposto {quantidade} unidades de {self.nome}. Novo estoque: {self.estoque}")

    # Venda de produtos com verificação de estoque
    def vender(self, quantidade):
        if quantidade > self.estoque:
            print(f"Não é possível vender {quantidade} unidades de {self.nome}. Estoque atual: {self.estoque}")
        else:
            self.estoque -= quantidade
            print(f"Vendido {quantidade} unidades de {self.nome}. Estoque restante: {self.estoque}")

# Subclasse ProdutoNacional (sem alteração nos atributos)
class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)  # Chama o construtor da classe pai

    # Mesmo comportamento de preço
    def preco_final(self):
        return self.preco

    # Nota fiscal nacional
    def emitir_nota(self):
        print(f"Nota fiscal nacional para {self.nome}.")

# Subclasse ProdutoImportado (tem taxa de importação)
class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)       # Construtor da classe pai
        self.taxa_importacao = taxa_importacao       # Taxa adicional (%)

    # Preço com taxa de importação aplicada
    def preco_final(self):
        return self.preco + (self.preco * self.taxa_importacao)

    # Nota específica de produto importado
    def emitir_nota(self):
        print(f"Nota de importação para {self.nome} com taxa aplicada.")

# Classe abstrata Funcionario (não pode ser instanciada diretamente)
class Funcionario(abc.ABC):
    def __init__(self, nome):
        self.nome = nome

    @abc.abstractmethod
    def calcular_pagamento(self):
        pass  # Método obrigatório para subclasses

# Funcionário CLT com salário fixo
class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

# Funcionário PJ com pagamento por hora
class FuncionarioPJ(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora

