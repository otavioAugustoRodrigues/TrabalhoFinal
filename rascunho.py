from typing import Type 

class Item:
    def __init__(self, nome : str, quantidade : int, categoria : str, valor : float) -> None:
        self.nome_item = nome
        self.quantidade_item = quantidade
        self.categoria_item = categoria
        self.valor_item = valor
        self.item_id_item = 0

#
# -> implementar um getter para o nome do item (ex.: se é string etc...)
#
    @property
    def nome(self) -> str:
            return self.nome_item
        
#
# -> implementar um setter para o nome do item (ex.: se é string etc...)
#
    @nome.setter
    def nome(self, nome) -> None:
        self.nome_item = nome

#
# -> implementar um getter para o valor do item (ex.: se é string etc...)
#
    @property
    def valor(self) -> float:
            return self.valor_item

#
# -> implementar um setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
#
    @valor.setter
    def valor(self, valor) -> None:
        self.valor_item = valor

#
# -> implementar um getter para o valor do item (ex.: se é string etc...)
#
    @property
    def categoria(self) -> str:
            return self.categoria_item
    
#
# -> implementar um setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso
#   banco de dados).
#
    @categoria.setter
    def categoria(self, categoria) -> None:
        self.categoria_item = categoria 

class ControleEstoque:
#
# constructor do nosso controle de estoque.
#
    def __init__(self) -> None:
        self.itens_cadastrados = []
        self.itens__controle = []
        self.item_id_controle = 0
        pass
    
#
# a ideia aqui é implementar uma função que vai verificar se um item
# está cadastrado em nosso banco de itens cadastrados.
#
    def verifica_item_cadastrado(self, item : Type[Item]) -> bool:
        for i in self.itens_cadastrados:
            if i.nome == item.nome:
                return True

#
# a ideia aqui é implementar uma função que vai cadastrar um item
# no nosso banco de itens cadastrados.
#
    def cadastra_item(self, item : Type[Item]) -> None:
        if (not self.verifica_item_cadastrado(item)):
            self.itens_cadastrados.append(item)
            
#
# a ideia aqui é implementar uma função que vai remover um item
# do nosso banco de itens cadastrados.
#
    def remove_item(self, item : Type[Item]) -> None:
        if self.verifica_item_cadastrado(item):
            del self.itens_cadastrados[localiza_item(item)]

#
# a ideia aqui é implementar uma função que vai retornar o índice
# do membro da lista que estamos procurando (e utilizar em outras
# funções futuramente);
#
    def localiza_item(self, item : Type[Item]) -> int:
        for i in self.itens_cadastrados:
            if i.nome == item.nome:
                return self.itens_cadastrados.index(i)

def main():
    item1 = Item("varistor", "1", "componente eletrônico", 0.35)
    controle_estoque = ControleEstoque()
    print(controle_estoque.verifica_item_cadastrado(item1))

main()
