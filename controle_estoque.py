from typing import Type
from item import *
from fornecedor import *

class ControleEstoque:
    # Constructor do controle de estoque.
    def __init__(self) -> None:
        self._itens_cadastrados = []
        self._fornecedores_cadastrados = []
        self._item_id_controle = len(self._itens_cadastrados)
        self._fornecedor_id_controle = len(self._fornecedores_cadastrados)
        pass

    # Getter para a lista de itens cadastrados.
    @property
    def itens_cadastrados(self) -> Type[Item]:
            return self._itens_cadastrados

    # Getter para o último ID do item cadastrado no banco de dados.
    @property
    def item_id_controle(self) -> int:
            return self._item_id_controle
    
    # Método que implementa uma função que verifica se um item está cadastrado no banco de itens cadastrados.
    def verifica_item_cadastrado(self, item : Type[Item]) -> bool:
        for i in self._itens_cadastrados:
            if i.nome_item == item.nome_item and i.valor_item == item.valor_item:
                return True
        else:
             return False 
        
    # Método que verifica se um fornecedor está cadastrado no banco de fornecedores cadastrados.
    def verifica_fornecedor_cadastrado(self, fornecedor : Fornecedor) -> None:
        for i in self._itens_cadastrados:
            if i.nome_item == fornecedor.nome_fornecedor:
                return True
        else:
             return False    
    
    def cria_item_fornecedor(self, nome : str, quantidade : int, categoria : str, valor : float, nome_fornecedor : Type[Fornecedor]) -> None:
        item = Item(nome, quantidade, categoria, valor, False)
        item.nome_fornecedor = nome_fornecedor
        self.cadastra_item(item)

    # Método que cadastra um item no banco de itens cadastrados.
    def cadastra_item(self, item : Type[Item]) -> None:
        if (not self.verifica_item_cadastrado(item)):
            self._item_id_controle += 1
            item.item_id = self._item_id_controle
            self._itens_cadastrados.append(item)
            print(f'{item.nome_item} {item.item_id} cadastrado com sucesso!')

    # Método que cadastra um fornecedor no banco de fornecedores cadastrados.
    def cadastra_fornecedor(self, fornecedor : Type[Fornecedor]) -> None:
        if (not self.verifica_fornecedor_cadastrado(fornecedor)):
            self._fornecedor_id_controle += 1
            fornecedor._id_fornecedor = self._fornecedor_id_controle
            self._fornecedores_cadastrados.append(fornecedor)
            print(f'{fornecedor.nome_fornecedor} {fornecedor._id_fornecedor} cadastrado com sucesso!')

    # Retorna o índice do membro da lista.
    def localiza_item(self, item : Type[Item]) -> int:
        for i in self.itens_cadastrados:
            if i.nome_item == item.nome_item:
                return self.itens_cadastrados.index(i)
            
    def printa_terminal_itens_cadastrados(self):
         for item in self.itens_cadastrados:
              print(f"Item cadastrado: {item.nome_item}, Quantidade: {item.quantidade_item}, Categoria: {item.categoria_item}, Valor: {item.valor_item}, Fornecedor: {item.nome_fornecedor_item}")