from typing import Type
from controle_estoque import *

# Classe responsável por ordenar o que está cadastrado no estoque de acordo com algum parâmetro.
class OrdenaEstoque:
    # Método responsável por imprimir o cabeçalho
    def padrao_imprime_cabecalho(self) -> None:
        print(f"{'ID' :<5}\t{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}\t{'Nome do fornecedor' :<25}")

    # Método responsável por imprimir 
    def padrao_imprime_estoque(self, i_item_cadastrado : Type[Item]) -> None:
        print(f"{i_item_cadastrado.get_id_item :< 5}\t{i_item_cadastrado.get_nome_item :<15}\t{i_item_cadastrado.get_quantidade_item :<5}\t{i_item_cadastrado.get_categoria_item :<25}\t{i_item_cadastrado.get_valor_item :<10}\t{i_item_cadastrado.get_nome_fornecedor_item:<30}")   

    # Método responsável por ordenar o que está cadastrado no estoque de acordo com o nome dos itens.
    def ordena_estoque_nome(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_nome = sorted(controle_estoque.get_itens_cadastrados, key=lambda x: x.get_nome_item)
        self.padrao_imprime_cabecalho()
        for i in controle_estoque_ordenado_nome:
            self.padrao_imprime_estoque(i)

    # Método responsável por ordenar o que está cadastrado no estoque de acordo com a categoria dos itens.
    def ordena_estoque_categoria(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_categoria = sorted(controle_estoque.get_itens_cadastrados, key=lambda x: x.get_categoria_item)
        self.padrao_imprime_cabecalho()
        for i in controle_estoque_ordenado_categoria:
            self.padrao_imprime_estoque(i)

    # Método responsável por ordenar o que está cadastrado no estoque de acordo com o nome do fornecedor.
    def ordena_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_fornecedor = sorted(controle_estoque.get_itens_cadastrados, key=lambda x: x.get_nome_fornecedor_item)
        self.padrao_imprime_cabecalho()
        for i in controle_estoque_ordenado_fornecedor:
            self.padrao_imprime_estoque(i)