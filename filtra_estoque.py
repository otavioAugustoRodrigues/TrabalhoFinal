from controle_estoque import *
from planilha_csv import *

# Classe responsável por filtrar o que está cadastrado no estoque de acordo com algum parâmetro.
class FiltraEstoque:
    # método responsável por filtrar o que está cadastrado no estoque de acordo com o nome do item.
    def filtra_controle_estoque_nome(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome : str) -> None:
        controle_estoque_ordenado_nome = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_nome_item == parametro_filtro_nome:
                controle_estoque_ordenado_nome.append(i)
        controle_estoque.imprime_informacoes_item_cabecalho()
        for item in controle_estoque_ordenado_nome:
            controle_estoque.imprime_informacoes_item_atributos(item)

    def filtra_controle_estoque_categoria(self, controle_estoque : Type[ControleEstoque], parametro_filtro_categoria : str) -> None:
        controle_estoque_ordenado_categoria = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_categoria_item == parametro_filtro_categoria:
                controle_estoque_ordenado_categoria.append(i)
        controle_estoque.imprime_informacoes_item_cabecalho()
        for item in controle_estoque_ordenado_categoria:
            controle_estoque.imprime_informacoes_item_atributos(item)
        
    def filtra_controle_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome_fornecedor : str) -> None:
        controle_estoque_ordenado_fornecedor = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.fornecedor.get_nome_fornecedor == parametro_filtro_nome_fornecedor:
                controle_estoque_ordenado_fornecedor.append(i)
        controle_estoque.imprime_informacoes_item_cabecalho()
        for item in controle_estoque_ordenado_fornecedor:
            controle_estoque.imprime_informacoes_item_atributos(item)