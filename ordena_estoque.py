from typing import Type
from controle_estoque import *
from planilha_csv import *

# Classe responsável por ordenar o que está cadastrado no estoque de acordo com algum parâmetro.
class OrdenaEstoque:
    # Classe responsável por ordenar o que está cadastrado no estoque de acordo com o nome dos itens.
    @classmethod
    def ordena_estoque_nome(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_nome = ControleEstoque()
        array_filtrado = []
        for i in controle_estoque.get_itens_cadastrados:
            if i.fornecedor is not None:
                array_filtrado.append(i)

        controle_estoque_ordenado_nome.set_itens_cadastados = sorted(array_filtrado, key=lambda x: x.get_nome_item)
        controle_estoque_ordenado_nome.padrao_imprime_cabecalho()
        for item in controle_estoque_ordenado_nome.get_itens_cadastrados:
            controle_estoque_ordenado_nome.padrao_imprime_estoque(item)

    # Classe responsável por ordenar o que está cadastrado no estoque de acordo com a categoria dos itens.
    @classmethod
    def ordena_estoque_categoria(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_categoria = ControleEstoque()
        array_filtrado = []
        for i in controle_estoque.get_itens_cadastrados:
            if i.fornecedor is not None:
                array_filtrado.append(i)

        controle_estoque_ordenado_categoria.set_itens_cadastados = sorted(array_filtrado, key=lambda x: x.get_categoria_item)
        controle_estoque_ordenado_categoria.padrao_imprime_cabecalho()
        for item in controle_estoque_ordenado_categoria.get_itens_cadastrados:
            controle_estoque_ordenado_categoria.padrao_imprime_estoque(item)
    
    # Classe responsável por ordenar o que está cadastrado no estoque de acordo com o nome do fornecedor dos itens.
    @classmethod
    def ordena_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_fornecedor = ControleEstoque()
        array_filtrado = []
        for i in controle_estoque.get_itens_cadastrados:
            if i.fornecedor is not None:
                array_filtrado.append(i)
        else:
            controle_estoque_ordenado_fornecedor.set_itens_cadastados = sorted(array_filtrado, key=lambda x: x.fornecedor.get_nome_fornecedor)
            controle_estoque_ordenado_fornecedor.padrao_imprime_cabecalho()
            for item in controle_estoque_ordenado_fornecedor.get_itens_cadastrados:
                controle_estoque_ordenado_fornecedor.padrao_imprime_estoque(item)