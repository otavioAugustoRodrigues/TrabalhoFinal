from typing import Type
from item import *
from fornecedor import *

class ControleEstoque:
    # Constructor do controle de estoque.
    def __init__(self) -> None:
        self._itens_cadastrados = []
        self._fornecedores_cadastrados = []
        self._id_item_controle = 0
        self._id_fornecedor_controle = 0
        pass

    # Getter para a lista de itens cadastrados.
    @property
    def get_itens_cadastrados(self) -> Type[Item]:
            return self._itens_cadastrados
    
    # Getter para a lista de fornecedores cadastrados.
    @property
    def get_fornecedores_cadastrados(self) -> Type[Fornecedor]:
            return self._fornecedores_cadastrados

    # Getter para o último ID do item cadastrado no banco de dados.
    @property
    def get_item_id_controle(self) -> int:
            return self._id_item_controle
    
    # Método que aumenta o ID, conforme os itens são cadastrados no controle estoque.
    def aumenta_item_id_controle(self) -> None:
        self._id_item_controle += 1     

    # Getter para o último ID do fornecedor cadastrado no banco de dados.
    @property
    def get_fornecedor_id_controle(self) -> int:
            return self._id_fornecedor_controle
    
    # Método que aumenta o ID, conforme os itens são cadastrados no controle estoque.
    def aumenta_fornecedor_id_controle(self) -> None:
        self._id_fornecedor_controle += 1     
    
    # Método que implementa uma função que verifica se um item está cadastrado no banco de itens cadastrados.
    def verifica_item_cadastrado(self, item : Type[Item]) -> bool:
        for i in self.get_itens_cadastrados:
            if (i.get_nome_item == item.get_nome_item and 
                i.get_categoria_item == item.get_categoria_item and
                i.get_id_item == item.get_id_item and
                i.get_nome_fornecedor_item == item.set_nome_fornecedor_item
                ):
                return True
        else:
             return False 
        
    # Método que verifica se um fornecedor está cadastrado no banco de fornecedores cadastrados.
    def verifica_fornecedor_cadastrado(self, fornecedor : Type[Fornecedor]) -> None:
        for i in self.get_fornecedores_cadastrados:
            if i.get_nome_fornecedor == fornecedor.get_nome_fornecedor:
                return True
        else:
             return False    

    # Método que cadastra um item no banco de itens cadastrados.
    def cadastra_item(self, item : Type[Item]) -> None:
        if not self.verifica_item_cadastrado(item):
            self.aumenta_item_id_controle()
            item.set_id_item = self.get_item_id_controle
            self._itens_cadastrados.append(item)
            print(f'{item.get_nome_item} {item.get_id_item} cadastrado com sucesso!')

    # Método que cadastra um fornecedor no banco de fornecedores cadastrados.
    def cadastra_fornecedor(self, fornecedor : Type[Fornecedor]) -> None:
        if (not self.verifica_fornecedor_cadastrado(fornecedor)):
            self.aumenta_fornecedor_id_controle()
            fornecedor.set_id_fornecedor = self.get_fornecedor_id_controle
            self._fornecedores_cadastrados.append(fornecedor)
            print(f'{fornecedor.get_nome_fornecedor} {fornecedor.get_id_fornecedor} cadastrado com sucesso!')

    # Método que imprime na tela todos os itens cadastrados no controle de estoque.
    def printa_terminal_itens_cadastrados(self):
        for item in self.get_itens_cadastrados:
            print(f"ID do item: {item.get_id_item}, Item cadastrado: {item.get_nome_item}, Quantidade: {item.get_quantidade_item}, Categoria: {item.categoria_item}, Valor: {item.get_valor_item}, Fornecedor: {item.get_nome_fornecedor_item}")

    # Método que imprime na tela todos os fornecedores cadastrados no controle de estoque.
    def printa_terminal_fornecedores_cadastrados(self):
        for i in self.get_fornecedores_cadastrados:
            print(f"ID do fornecedor: {i.get_id_fornecedor}, Nome do fornecedor cadastrado: {i.get_nome_fornecedor}, país: {i.get_pais_fornecedor}, termo de pagamento: {i.get_termo_pagamento_fornecedor}")

    # Método que checa se um item cadastrado já foi cadastrado anteriormente para este mesmo fornecedor.
    def checa_item_cadastrado_fornecedor(self, item: Type[Item], fornecedor : Type[Fornecedor]) -> bool:
        for i in self.get_itens_cadastrados:
            if i.get_nome_item == item.get_nome_item and i.get_nome_fornecedor_item == fornecedor.get_nome_fornecedor:
                return True
        else:
            return False

    # Método que cadastra itens para um determinado fornecedor aqui, passaremos um item como argumento e, ao cadastrarmos 
    # ele como vendido pelo fornecedor, este ficará encarregado de passar as demais informações, como o valor da venda e 
    # o próprio nome do fornecedor que vende este item.
    def cadastra_item_fornecedor(self, fornecedor : Type[Fornecedor], item : Type[Item], valor_item_fornecedor : float) -> None:
        if self.verifica_fornecedor_cadastrado(fornecedor):
            if self.checa_item_cadastrado_fornecedor(item, fornecedor):
                print(f"item {item.get_nome_item} já cadastrado para o fornecedor {fornecedor.get_nome_fornecedor}. Atualizando valor do item...")
                item.set_valor_item = valor_item_fornecedor
            else:
                novo_item_cadastrado = Item(item.get_nome_item, item.get_categoria_item)
                novo_item_cadastrado.set_valor_item = valor_item_fornecedor
                novo_item_cadastrado.set_nome_fornecedor_item = fornecedor.get_nome_fornecedor
                self.cadastra_item(novo_item_cadastrado)
        else:
            self.cadastra_fornecedor(fornecedor)
            self.cadastra_item_fornecedor(fornecedor, item, valor_item_fornecedor)