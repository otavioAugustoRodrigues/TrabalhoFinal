from typing import Type

class Item:
    _categorias_validas = []

    def __init__(self, nome : str, categoria : str) -> None:
        self.nome_item = nome
        self._quantidade_item = 0
        self.categoria_item = categoria
        self._valor_item = 0
        self._item_ativo = False
        self._id_item = 0
        self._nome_fornecedor_item = 0

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

    # Getter para o nome do fornecedor (ex.: se é string etc...)
    @property
    def get_nome_fornecedor_item(self) -> str:
            return str(self._nome_fornecedor_item)
        
    # Setter para o nome do item (ex.: se é string etc...)
    @get_nome_fornecedor_item.setter
    def set_nome_fornecedor_item(self, nome_fornecedor : str) -> None:
        self._nome_fornecedor_item = nome_fornecedor