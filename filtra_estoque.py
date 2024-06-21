from controle_estoque import *

# Classe responsável por filtrar o que está cadastrado no estoque de acordo com algum parâmetro.
class FiltraEstoque:

    @classmethod
    def filtra_controle_estoque_nome(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome : str) -> None:
        controle_estoque_ordenado_nome = ControleEstoque()
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_nome_item == parametro_filtro_nome:
                controle_estoque_ordenado_nome._itens_cadastrados.append(i)
        controle_estoque_ordenado_nome.padrao_imprime_estoque()

    @classmethod
    def filtra_controle_estoque_categoria(self, controle_estoque : Type[ControleEstoque], parametro_filtro_categoria : str) -> None:
        controle_estoque_ordenado_categoria = ControleEstoque()
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_categoria_item == parametro_filtro_categoria:
                controle_estoque_ordenado_categoria._itens_cadastrados.append(i)
        controle_estoque_ordenado_categoria.padrao_imprime_estoque()
        
    @classmethod
    def filtra_controle_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome_fornecedor : str) -> None:
        controle_estoque_ordenado_fornecedor = ControleEstoque()
        for i in controle_estoque.get_itens_cadastrados :
            if i.fornecedor is not None:
                if i.fornecedor.get_nome_fornecedor == parametro_filtro_nome_fornecedor:
                    controle_estoque_ordenado_fornecedor._itens_cadastrados.append(i)
        controle_estoque_ordenado_fornecedor.padrao_imprime_estoque()