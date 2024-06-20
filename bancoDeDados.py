import pandas as pd
from controle_estoque import *
from item import *

class BancoDados:
  def salva_controle(self,controle : ControleEstoque) -> None:
    nomes = []
    quantidades = []
    categorias = []
    for i in range(len(controle.itens_cadastrados)):
      nomes.append(controle.itens_cadastrados[i].nome)
      quantidades.append(controle.itens_cadastrados[i].quantidade)
      categorias.append(controle.itens_cadastrados[i].categoria)

    d = {'Nome': nomes, 'Quantidade': quantidades, 'Categoria': categorias}
    dados = pd.DataFrame(data= d)
    dados.to_excel("tabelaExcel.xlsx")
    
  
  def le_controle(self) -> Type[ControleEstoque]:
    controle = ControleEstoque()
    lerItens = pd.read_excel("tabelaExcel.xlsx")
    for i in lerItens.itertuples(index=False):
      nome = i.Nome
      quantidade = int(i.Quantidade) 
      categoria = i.Categoria

      item = Item(nome, quantidade, categoria, True)
      controle.cadastra_item(item)
    return controle
 
    


