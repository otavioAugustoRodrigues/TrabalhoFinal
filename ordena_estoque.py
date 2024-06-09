from typing import Type
from controle_estoque import *

# Classe responsável por ordenar o que está cadastrado no estoque de acordo com algum parâmetro.
class OrdenaEstoque:

    # Classe responsável por ordenar o que está cadastrado no estoque de acordo com o nome dos itens.
    def ordena_estoque_nome(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_nome = sorted(controle_estoque.itens_cadastrados, key=lambda x: x.nome_item)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for i in controle_estoque_ordenado_nome:
            print(f"{i.nome_item :<15}\t{i.quantidade_item :<5}\t{i.categoria_item :<25}\t{i.valor_item :<10}")

    # Classe responsável por ordenar o que está cadastrado no estoque de acordo com a categoria dos itens.
    def ordena_estoque_categoria(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_categoria = sorted(controle_estoque.itens_cadastrados, key=lambda x: x.categoria_item)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for i in controle_estoque_ordenado_categoria:
            print(f"{i.nome_item :<15}\t{i.quantidade_item :<5}\t{i.categoria_item :<25}\t{i.valor_item :<10}") 

    def ordena_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_fornecedor = sorted(controle_estoque.itens_cadastrados, key=lambda x: x.categoria_item)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for i in controle_estoque_ordenado_fornecedor:
            print(f"{i.nome_item :<15}\t{i.quantidade_item :<5}\t{i.categoria_item :<25}\t{i.valor_item :<10}") 