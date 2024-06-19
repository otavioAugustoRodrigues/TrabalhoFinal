from controle_estoque import *

# Classe responsável por filtrar o que está cadastrado no estoque de acordo com algum parâmetro.
class FiltraEstoque:
    # método responsável por filtrar o que está cadastrado no estoque de acordo com o nome do item.
    def filtra_controle_estoque_nome(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome : str) -> None:
        controle_estoque_ordenado_nome = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_nome_item == parametro_filtro_nome:
                controle_estoque_ordenado_nome.append(i)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for j in controle_estoque_ordenado_nome:
            print(f"{j.get_nome_item :<15}\t{j.get_quantidade_item :<5}\t{j.get_categoria_item :<25}\t{j.get_valor_item :<10}")      

    def filtra_controle_estoque_categoria(self, controle_estoque : Type[ControleEstoque], parametro_filtro_categoria : str) -> None:
        controle_estoque_ordenado_categoria = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_categoria_item == parametro_filtro_categoria:
                controle_estoque_ordenado_categoria.append(i)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for j in controle_estoque_ordenado_categoria:
            print(f"{j.get_nome_item :<15}\t{j.get_quantidade_item :<5}\t{j.get_categoria_item :<25}\t{j.get_valor_item :<10}")   
        
    def filtra_controle_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque], parametro_filtro_nome_fornecedor : str) -> None:
        controle_estoque_ordenado_fornecedor = []
        for i in controle_estoque.get_itens_cadastrados :
            if i.get_nome_fornecedor_item == parametro_filtro_nome_fornecedor:
                controle_estoque_ordenado_fornecedor.append(i)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for j in controle_estoque_ordenado_fornecedor:
            print(f"{j.get_nome_item :<15}\t{j.get_quantidade_item :<5}\t{j.get_categoria_item :<25}\t{j.get_valor_item :<10}\t{j.get_nome_fornecedor_item:<30}")   