from controleEstoque import *

# Classe responsável por filtrar o que está cadastrado no estoque de acordo com algum parâmetro.
class FiltraEstoque:

    # método responsável por filtrar o que está cadastrado no estoque de acordo com o nome do item.
    def filtra_nome(self, controle_estoque : Type[ControleEstoque], nome_filtro : str) -> None:
        controle_estoque_ordenado_nome = []
        for i in controle_estoque.itens_cadastrados :
            if i.nome == nome_filtro:
                controle_estoque_ordenado_nome.append(i)
        print(f"{'Nome':<15}\t{'Qtd.':<5}\t{'Categoria':<25}\t{'Valor':<10}")
        for j in controle_estoque_ordenado_nome:
            print(f"{j.nome:<15}\t{j.quantidade:<5}\t{j.categoria:<25}\t{j.valor:<10}")       