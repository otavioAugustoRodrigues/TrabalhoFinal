from controle_estoque import *

# Classe responsável por filtrar o que está cadastrado no estoque de acordo com algum parâmetro.
class FiltraEstoque:


    def filtra_controle_estoque_nome(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome : str) -> None:
        controle_estoque_ordenado_nome = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_nome_item == parametro_filtro_nome:
                controle_estoque_ordenado_nome.append(i)
        controle_estoque.padrao_imprime_cabecalho()
        for j in controle_estoque_ordenado_nome:
            controle_estoque.padrao_imprime_estoque(j)

    def filtra_controle_estoque_categoria(self, controle_estoque : Type[ControleEstoque], parametro_filtro_categoria : str) -> None:
        controle_estoque_ordenado_categoria = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_categoria_item == parametro_filtro_categoria:
                controle_estoque_ordenado_categoria.append(i)
        controle_estoque.padrao_imprime_cabecalho()
        for j in controle_estoque_ordenado_categoria:
            controle_estoque.padrao_imprime_estoque(j)
        
    def filtra_controle_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome_fornecedor : str) -> None:
        controle_estoque_ordenado_fornecedor = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.fornecedor is not None:
                if i.fornecedor.get_nome_fornecedor == parametro_filtro_nome_fornecedor:
                    controle_estoque_ordenado_fornecedor.append(i)
        controle_estoque.padrao_imprime_cabecalho()
        for j in controle_estoque_ordenado_fornecedor:
            controle_estoque.padrao_imprime_estoque(j)