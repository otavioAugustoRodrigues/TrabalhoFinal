from controle_estoque import *
from filtra_estoque import *
from fornecedor import *
from item import *
from ordena_estoque import *
from bancoDeDados import *
from JanelasTK.home import Home
from JanelasTK.ListItens import ListItens
#from bancoDeDados import BancoDados
from planilha_csv import *
from comprador import *
from vendedor import *

import pandas as pd

if __name__ == "__main__":
    '''
    bd = BancoDados()
    controle = bd.le_controle()
    '''
    controle_estoque = ControleEstoque()

    fornecedor1 = Fornecedor("Leitura", "Brasil", "30D NET")
    controle_estoque.cadastra_fornecedor(fornecedor1)

    fornecedor2 = Fornecedor("Renner", "Brasil", "30D NET")
    controle_estoque.cadastra_fornecedor(fornecedor2)

    fornecedor3 = Fornecedor("Arkom", "Brasil", "30D NET")
    controle_estoque.cadastra_fornecedor(fornecedor3)

    #controle_estoque.printa_terminal_fornecedores_cadastrados()

    item1 = Item("lapis", "material escolar")
    controle_estoque.cadastra_item(item1)

    item2 = Item("tesoura", "material escolar")
    controle_estoque.cadastra_item(item2)

    item3 = Item("calça", "roupa")
    controle_estoque.cadastra_item(item3)

    item4 = Item("blusa", "roupa")
    controle_estoque.cadastra_item(item4)

    item5 = Item("varistor", "componente eletrônico")
    controle_estoque.cadastra_item(item5)

    item6 = Item("LED", "componente eletrônico")
    controle_estoque.cadastra_item(item6)

    #controle_estoque.printa_terminal_itens_cadastrados()

    controle_estoque.cadastra_item_fornecedor(fornecedor1, item1, 1)
    controle_estoque.cadastra_item_fornecedor(fornecedor1, item2, 1.50)

    controle_estoque.cadastra_item_fornecedor(fornecedor2, item1, 3)
    controle_estoque.cadastra_item_fornecedor(fornecedor2, item3, 299.90)
    controle_estoque.cadastra_item_fornecedor(fornecedor2, item4, 99.90)

    controle_estoque.cadastra_item_fornecedor(fornecedor3, item5, 0.0005)
    controle_estoque.cadastra_item_fornecedor(fornecedor3, item5, 0.001)

    controle_estoque.cadastra_item_fornecedor(fornecedor1, item1, 2)
    controle_estoque.cadastra_item_fornecedor(fornecedor1, item1, 2.50)

    #controle_estoque.printa_terminal_itens_cadastrados()
    #controle_estoque.printa_terminal_fornecedores_cadastrados()

    filtra_estoque = FiltraEstoque()
    filtra_estoque.filtra_controle_estoque_nome(controle_estoque, "lapis")
    #filtra_estoque.filtra_controle_estoque_fornecedor(controle_estoque, "Arkom")

    ordena_estoque = OrdenaEstoque()
    #ordena_estoque.ordena_estoque_nome(controle_estoque)
    #ordena_estoque.ordena_estoque_categoria(controle_estoque)
    #ordena_estoque.ordena_estoque_fornecedor(controle_estoque)

    controle_estoque.printa_terminal_itens_cadastrados()

    #cria lista de atributos dos itens e passa como parametro para criação do DataFrame e depois passa para excel

    # item = Item("Açucar","Comida",5.40, True)
    #controle.cadastra_item(item)

    #Home()

    #bd.salva_controle(controle)

    planilha_csv = PlanilhaCSV()
    # planilha_csv.escreve_tela_GUI(controle_estoque)
    planilha_csv.escreve_csv_colunas_diferentes("teste.csv", controle_estoque)
    '''
    controle_estoque = ControleEstoque()

    planilha_csv = PlanilhaCSV()
    planilha_csv.adiciona_itens_fornecedor_planilha_csv("teste.csv", controle_estoque)
    '''