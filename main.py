from controle_estoque import *
from filtra_estoque import *
from fornecedor import *
from gerenciador_planilha import *
from item import *
from ordena_estoque import *
from comprador_vendedor import *
from bancoDeDados import *
from JanelasTK.home import Home
from JanelasTK.ListItens import ListItens
from bancoDeDados import BancoDados

import pandas as pd


if __name__ == "__main__":
  
    # #gerenciador_planilha.escreve_csv_colunas_diferentes("teste.csv", controle_estoque)

    # #gerenciador_planilha.le_csv('teste.csv')
    # #gerenciador_planilha.escreve_tela_GUI(controle_estoque)

    # #print(controle_estoque._fornecedores_cadastrados[0].printar_item("cola"))
    
    # # ordena_estoque = OrdenaEstoque()
    # # ordena_estoque.ordena_nome(controle_estoque)
    # # ordena_estoque.ordena_categoria(controle_estoque)
    
    # # filtra_estoque  = FiltraEstoque()
    # # filtra_estoque.filtra_nome(controle_estoque, "lapis")
    
    #cria lista de atributos dos itens e passa como parametro para criação do DataFrame e depois passa para excel

    Home()
    
   