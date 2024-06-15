from controle_estoque import *
from filtra_estoque import *
from fornecedor import *
from gerenciador_planilha import *
from item import *
from ordena_estoque import *
from comprador_vendedor import *
from testePanda import *
from JanelasTK.home import Home
from JanelasTK.ListItens import ListItens

import pandas as pd


if __name__ == "__main__":
    controle_estoque = ControleEstoque()
    gerenciador_planilha = GerenciadorPlanilha()

    #le o arquivo com os Itens salvo
    lerItens = pd.read_excel("tabelaExcel.xlsx")

    for i in lerItens.itertuples(index=False):
      nome = i.Nome
      quantidade = int(i.Quantidade) 
      categoria = i.Categoria
      valor = float(i.Valor)

      item = Item(nome, quantidade, categoria, valor, True)
      controle_estoque.cadastra_item(item)


    item1 = Item("varistor", 2, "componente eletrônico", 0.35, False)
    controle_estoque.cadastra_item(item1)

    item2 = Item("lapis", 10, "item de escola", 2.00, True)
    controle_estoque.cadastra_item(item2)

    item3 = Item("cola", 50, "item de escola", 2.00, True)
    controle_estoque.cadastra_item(item3)
    
    item4 = Item("lapis", 10, "item de escola", 2.50, True)
    controle_estoque.cadastra_item(item4)

    item5 = Item("caneta", 80, "item de escola", 3.90, True)
    controle_estoque.cadastra_item(item5)
    
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
    nomes = []
    quantidades = []
    categorias = []
    valor = []
    
    for i in range(len(controle_estoque.itens_cadastrados)):
      nomes.append(controle_estoque.itens_cadastrados[i].nome)
      quantidades.append(controle_estoque.itens_cadastrados[i].quantidade)
      categorias.append(controle_estoque.itens_cadastrados[i].categoria)
      valor.append(controle_estoque.itens_cadastrados[i].valor)

    d = {'Nome': nomes, 'Quantidade': quantidades, 'Categoria': categorias, 'Valor': valor}
    dados = pd.DataFrame(data= d)

    lista = ListItens(controle_estoque)
    lista()
   
    dados.to_excel("tabelaExcel.xlsx", index=False)
    print(dados)
    
   