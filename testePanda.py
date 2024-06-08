import pandas as pd
from controle_estoque import *
from item import *

class BancoDados:
  def ler_controle(self,controle : ControleEstoque) -> pd.DataFrame:
    nomes = []
    quantidades = []
    categorias = []
    valor = []
    for i in range(len(controle.itens_cadastrados)):
      nomes.append(controle.itens_cadastrados[i].nome)
      quantidades.append(controle.itens_cadastrados[i].quantidade)
      categorias.append(controle.itens_cadastrados[i].categoria)
      valor.append(controle.itens_cadastrados[i].valor)

    d = {'Nome': nomes, 'Quantidade': quantidades, 'Categoria': categorias, 'Valor': valor}

    dados = pd.DataFrame(data= d)
    return dados

 
    


