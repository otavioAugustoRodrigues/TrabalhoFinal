from typing import Type

class Item:
    _categorias_validas = []

    def __init__(self, nome : str, quantidade : int, categoria : str, valor : float) -> None:
        self.nome_item = nome
        self.quantidade_item = quantidade
        self.categoria_item = categoria
        self.valor_item = valor
        self.item_ativo = False
        self.item_id = 0
        self.nome_fornecedor_item = None

    @classmethod
    def adiciona_categoria_valida(self, nova_categoria_valida : str) -> None:
        if type(nova_categoria_valida) == str:
            self._categorias_validas.append(nova_categoria_valida)
        else:
            print("categoria inválida!")
    
    # Getter para o nome do item (ex.: se é string etc...)
    @property
    def nome_item(self) -> str:
            return self._nome_item
        
    # Setter para o nome do item (ex.: se é string etc...)
    @nome_item.setter
    def nome_item(self, nome) -> None:
        self._nome_item = nome

    # Getter para o nome do item (ex.: se é string etc...)
    @property
    def quantidade_item(self) -> int:
            return self._quantidade
        
    # Setter para o nome do item (ex.: se é string etc...)
    @quantidade_item.setter
    def quantidade_item(self, quantidade) -> None:
        self._quantidade = quantidade

    # Getter para a categoria do item.
    @property
    def categoria_item(self) -> str:
            return self._categoria_item
    
    # Setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso banco de dados).
    @categoria_item.setter
    def categoria_item(self, categoria) -> None:
        if categoria in self._categorias_validas:
            self._categoria_item = categoria
        else:
            print("categoria não é válida!")
    
    # Getter para o valor do item (ex.: se é string etc...)
    @property
    def valor_item(self) -> float:
            return self._valor_item

    # Setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
    @valor_item.setter
    def valor_item(self, valor) -> None:
        self._valor_item = valor

    # Getter para verificar se o item está obsoleto ou não.
    @property
    def item_ativo(self) -> int:
            return self._item_ativo
    
    # Setter para alterar o estado atual do item entre obsoleto ou não.
    @item_ativo.setter
    def item_ativo(self, item_ativo) -> None:
        self._item_ativo = item_ativo

    # Getter para o item_id do item 
    @property
    def item_id(self) -> int:
            return self._item_id
    
    # Setter para a categoria do item 
    @item_id.setter
    def item_id(self, item_id) -> None:
        self._item_id = item_id

    # Getter para o nome do fornecedor (ex.: se é string etc...)
    @property
    def nome_fornecedor_item(self) -> str:
            return self._nome_fornecedor
        
    # Setter para o nome do item (ex.: se é string etc...)
    @nome_fornecedor_item.setter
    def nome_fornecedor_item(self, nome_fornecedor) -> None:
        self._nome_fornecedor = nome_fornecedor