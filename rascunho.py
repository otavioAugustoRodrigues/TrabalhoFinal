import csv
from typing import Type 

class Item:
    def __init__(self, nome : str, quantidade : int, categoria : str, valor : float) -> None:
        self._nome_item = nome
        self._quantidade = quantidade
        self._categoria_item = categoria
        self._valor_item = valor
        self._item_id = 0

# -> implementa um getter para o nome do item (ex.: se é string etc...)
    @property
    def nome(self) -> str:
            return self._nome_item
        
# -> implementa um setter para o nome do item (ex.: se é string etc...)
    @nome.setter
    def nome(self, nome) -> None:
        self._nome_item = nome

    # -> implementa um getter para o nome do item (ex.: se é string etc...)
    @property
    def quantidade(self) -> int:
            return self._quantidade
        
# -> implementa um setter para o nome do item (ex.: se é string etc...)
    @nome.setter
    def quantidade(self, quantidade) -> None:
        self._quantidade = quantidade

# -> implementa um getter para o valor do item (ex.: se é string etc...)
    @property
    def valor(self) -> float:
            return self._valor_item

# -> implementa um setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
    @valor.setter
    def valor(self, valor) -> None:
        self._valor_item = valor

# -> implementa um getter para o valor do item (ex.: se é string etc...)
    @property
    def categoria(self) -> str:
            return self._categoria_item
    
# -> implementar um setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso
#   banco de dados).
    @categoria.setter
    def categoria(self, categoria) -> None:
        self._categoria_item = categoria

# -> implementa um getter para o item_id do item 
    @property
    def item_id(self) -> int:
            return self._item_id
    
# -> implementar um setter para a categoria do item 
    @item_id.setter
    def item_id(self, item_id) -> None:
        self._item_id = item_id
        

class ControleEstoque:
# constructor do nosso controle de estoque.
    def __init__(self) -> None:
        self._itens_cadastrados = []
        self._itens__controle = []
        self._item_id_controle = 0
        pass

# -> implementa um getter para a lista de itens cadastrados.
    @property
    def itens_cadastrados(self) -> Type[Item]:
            return self._itens_cadastrados

# -> implementa um getter para a lista de itens cadastrados.
    @property
    def item_id_controle(self) -> int:
            return self._item_id_controle
    
# a ideia aqui é implementar uma função que vai verificar se um item
# está cadastrado em nosso banco de itens cadastrados.
    def verifica_item_cadastrado(self, item : Type[Item]) -> bool:
        for i in self._itens_cadastrados:
            if i.nome == item.nome:
                return True

# a ideia aqui é implementar uma função que vai cadastrar um item
# no nosso banco de itens cadastrados.
    def cadastra_item(self, item : Type[Item]) -> None:
        if (not self.verifica_item_cadastrado(item)):
            self._item_id_controle += 1
            item.item_id = self._item_id_controle
            self._itens_cadastrados.append(item)
            print(f'{item.nome} {item.item_id} cadastrado com sucesso!')
            
# a ideia aqui é implementar uma função que vai remover um item
# do nosso banco de itens cadastrados.
    def remove_item(self, item : Type[Item]) -> None:
        if self.verifica_item_cadastrado(item):
            del self.itens_cadastrados[localiza_item(item)]

# a ideia aqui é implementar uma função que vai retornar o índice
# do membro da lista que estamos procurando (e utilizar em outras
# funções futuramente);
    def localiza_item(self, item : Type[Item]) -> int:
        for i in self.itens_cadastrados:
            if i.nome == item.nome:
                return self.itens_cadastrados.index(i)


# a ideia aqui é implementar uma classe que vai ser responsável
# por imprimir o controle
class GerenciadorPlanilha:
    def le_csv(self, nomearquivo):
        with open(nomearquivo, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                for element in row:
                    element_tab = element + '\t'
                    print(element_tab)

    # -> implementa uma função que vai gerar na saída um arquivo com o estado atual de todos os itens
         que foram cadastrados.
    def escreve_csv_colunas_diferentes(self, nomearquivo, controle_estoque : Type[ControleEstoque]):
        with open(nomearquivo, 'w', newline='') as csvfile:
            fieldnames = ['nome', 'quantidade', 'categoria', 'valor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for element in controle_estoque.itens_cadastrados:
                writer.writerow({'nome': element.nome, 'quantidade': element.quantidade, 'categoria': element.categoria, 'valor': element.valor})


def main():
    item1 = Item("varistor", 1, "componente eletrônico", 0.35)
    controle_estoque = ControleEstoque()
    controle_estoque.cadastra_item(item1)
    gerenciador_planilha = GerenciadorPlanilha()
    gerenciador_planilha.escreve_csv_colunas_diferentes('teste.csv', controle_estoque)


main()
