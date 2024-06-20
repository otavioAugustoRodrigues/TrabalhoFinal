from typing import Type
from fornecedor import *

class Item:
    _categorias_validas = []

    def __init__(self, nome : str, categoria : str) -> None:
        self.nome_item = nome
        self._quantidade_item = 0
        self.categoria_item = categoria
        self._valor_item = 0
        self._item_ativo = False
        self._id_item = 0
        self.fornecedor = None

    @classmethod
    def adiciona_categoria_valida(self, nova_categoria_valida : str) -> None:
        if type(nova_categoria_valida) == str:
            self._categorias_validas.append(nova_categoria_valida)
        else:
            print("categoria inválida!")
    
    # Getter para o nome do item (ex.: se é string etc...)
    @property
    def get_nome_item(self) -> str:
            return self.nome_item
        
    # Setter para o nome do item (ex.: se é string etc...)
    @get_nome_item.setter
    def set_nome_item(self, nome : str) -> None:
        self.nome_item = nome

    # Getter para o nome do item (ex.: se é string etc...)
    @property
    def get_quantidade_item(self) -> int:
            return self._quantidade_item
        
    # Setter para o nome do item (ex.: se é string etc...)
    @get_quantidade_item.setter
    def set_quantidade_item(self, quantidade : int) -> None:
        self._quantidade_item = quantidade

    # Getter para a categoria do item.
    @property
    def get_categoria_item(self) -> str:
            return self.categoria_item
    
    # Setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso banco de dados).
    @get_categoria_item.setter
    def set_categoria_item(self, categoria : str) -> None:
        if categoria in self._categorias_validas:
            self.categoria_item = categoria
        else:
            print("categoria não é válida!")
    
    # Getter para o valor do item (ex.: se é string etc...)
    @property
    def get_valor_item(self) -> float:
            return self._valor_item

    # Setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
    @get_valor_item.setter
    def set_valor_item(self, valor : float) -> None:
        self._valor_item = valor

    # Getter para verificar se o item está obsoleto ou não.
    @property
    def get_item_ativo(self) -> int:
            return self._item_ativo
    
    # Setter para alterar o estado atual do item entre obsoleto ou não.
    @get_item_ativo.setter
    def set_item_ativo(self, item_ativo : bool) -> None:
        self._item_ativo = item_ativo

    # Getter para o item_id do item 
    @property
    def get_id_item(self) -> int:
            return self._id_item
    
    # Setter para a categoria do item 
    @get_id_item.setter
    def set_id_item(self, item_id : int) -> None:
        self._id_item = item_id

    def set_fornecedor(self, fornecedor : Type[Fornecedor]) -> None:
        if self.fornecedor is None:
            self.fornecedor = Fornecedor(fornecedor.get_nome_fornecedor, fornecedor.get_pais_fornecedor, fornecedor.get_termo_pagamento_fornecedor)
            self.fornecedor.set_id_fornecedor = fornecedor.get_id_fornecedor
        else:
            self.fornecedor.set_nome_fornecedor = fornecedor.get_nome_fornecedor
            self.fornecedor.set_pais_fornecedor = fornecedor.get_pais_fornecedor
            self.fornecedor.set_termo_pagamento_fornecedor = fornecedor.get_termo_pagamento_fornecedor
            self.fornecedor.set_id_fornecedor = fornecedor.get_id_fornecedor
        
    def get_valor_total_estoque(self) -> float:
         return self.get_valor_item * self.get_quantidade_item         
    
    # Método que checa se um item cadastrado já foi cadastrado anteriormente para este mesmo fornecedor.
    def checa_item_cadastrado_fornecedor(self, nome_item_avaliado : str, fornecedor : Type[Fornecedor]) -> bool:
        if self.fornecedor is not None:
            print(f"if {self.get_nome_item} == {nome_item_avaliado} and {self.fornecedor.get_nome_fornecedor} == {fornecedor.get_nome_fornecedor}:")
            if self.get_nome_item == nome_item_avaliado and self.fornecedor.get_nome_fornecedor == fornecedor.get_nome_fornecedor:
                return True
        else:
            return False