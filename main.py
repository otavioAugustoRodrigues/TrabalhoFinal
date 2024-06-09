from controle_estoque import *
from filtra_estoque import *
from fornecedor import *
from planilha_csv import *
from item import *
from ordena_estoque import *
from comprador import *
from vendedor import *

if __name__ == "__main__":
    controle_estoque = ControleEstoque()
    gerenciador_planilha = PlanilhaCSV()
    Item.adiciona_categoria_valida("componente eletrônico")
    Item.adiciona_categoria_valida("item de escola")
    item1 = Item("varistor", 2, "componente eletrônico", 0.35)
    print(item1._categorias_validas)
    controle_estoque.cadastra_item(item1)

    item2 = Item("lapis", 10, "item de escola", 2.00)
    controle_estoque.cadastra_item(item2)

    item3 = Item("cola", 50, "item de escola", 2.00)
    controle_estoque.cadastra_item(item3)
    
    item4 = Item("lapis", 10, "item de escola", 2.50)
    controle_estoque.cadastra_item(item4)
    
    gerenciador_planilha.escreve_csv_colunas_diferentes('teste.csv', controle_estoque)

    gerenciador_planilha.le_csv('teste.csv')
    gerenciador_planilha.escreve_tela_GUI(controle_estoque)

    fornecedorA = Fornecedor("fornA", "BR", "Faturado")
    controle_estoque.cadastra_fornecedor(fornecedorA)
    fornecedorA.adicionar_item_fornecedor(item1,0.35)
    fornecedorA.adicionar_item_fornecedor(item2,5.00)
    fornecedorA.adicionar_item_fornecedor(item3,7.50)

    fornecedorB = Fornecedor("fornB", "US", "Boleto")
    controle_estoque.cadastra_fornecedor(fornecedorB)
    fornecedorB.adicionar_item_fornecedor(item1,0.50)
    fornecedorB.adicionar_item_fornecedor(item2,4.80)
    fornecedorB.adicionar_item_fornecedor(item3,8.60)

    print(controle_estoque._fornecedores_cadastrados[0].printar_item("cola"))
    
    ordena_estoque = OrdenaEstoque()
    ordena_estoque.ordena_estoque_nome(controle_estoque)
    ordena_estoque.ordena_estoque_categoria(controle_estoque)
    
    filtra_estoque  = FiltraEstoque()
    filtra_estoque.filtra_controle_estoque_nome(controle_estoque, "lapis")