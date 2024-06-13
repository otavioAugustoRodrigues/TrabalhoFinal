from controle_estoque import *

# Classe responsável por filtrar o que está cadastrado no estoque de acordo com algum parâmetro.
class FiltraEstoque:
    # método responsável por filtrar o que está cadastrado no estoque de acordo com o nome do item.
    def filtra_controle_estoque_nome(self, controle_estoque : Type[ControleEstoque], nome_filtro : str) -> None:
        self.controle_estoque_ordenado_nome = []
        for i in controle_estoque.itens_cadastrados :
            if i.nome_item == nome_filtro:
                self.controle_estoque_ordenado_nome.append(i)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for j in self.controle_estoque_ordenado_nome:
            print(f"{j.nome_item :<15}\t{j.quantidade_item :<5}\t{j.categoria_item :<25}\t{j.valor_item :<10}")      

    def filtra_controle_estoque_categoria(self, controle_estoque : Type[ControleEstoque], nome_filtro : str) -> None:
        self.controle_estoque_ordenado_categoria = []
        for i in controle_estoque.itens_cadastrados :
            if i.categoria_item == nome_filtro:
                self.controle_estoque_ordenado_categoria.append(i)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for j in self.controle_estoque_ordenado_categoria:
            print(f"{j.nome_item :<15}\t{j.quantidade_item :<5}\t{j.categoria_item :<25}\t{j.valor_item :<10}")   
        
    def filtra_controle_estoque_fornecedor(self, controle_estoque : Type[ControleEstoque], nome_filtro : str) -> None:
        self.controle_estoque_ordenado_fornecedor = []
        for i in controle_estoque.itens_cadastrados :
            if i.fornecedor_item == nome_filtro:
                self.controle_estoque_ordenado_fornecedor.append(i)
        print(f"{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}")
        for j in self.controle_estoque_ordenado_fornecedor:
            print(f"{j.nome_item :<15}\t{j.quantidade_item :<5}\t{j.categoria_item :<25}\t{j.valor_item :<10}")   