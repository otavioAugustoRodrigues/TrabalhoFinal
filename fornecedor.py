from typing import Type
from item import *

class Fornecedor:
    def __init__(self, nome : str, pais : str, termo_pagamento : str) -> None:
        self._nome_fornecedor = nome
        self._pais = pais
        self._termo_pagamento = termo_pagamento
        self._id_fornecedor = 0
        self._lista_itens = []
        self._valores_itens = []

    # Getter para o nome do fornecedor (ex.: se é string etc...)
    @property
    def nome_fornecedor(self) -> str:
        return self._nome_fornecedor
        
    # Setter para o nome do fornecedor (ex.: se é string etc...)
    @nome_fornecedor.setter
    def nome_fornecedor(self, nome) -> None:
        self._nome_fornecedor = nome
    
    # Getter para o país do fornecedor (ex.: se é string etc...)
    @property
    def pais(self) -> str:
        return self._pais
        
    # Setter para o país do fornecedor (ex.: se é string etc...)
    @pais.setter
    def pais(self, pais) -> None:
        self.pais = pais
    
    # Getter para o país do fornecedor (ex.: se é string etc...)
    @property
    def termo_pagamento(self) -> str:
        return self._termo_pagamento
        
    # Setter para o país do fornecedor (ex.: se é string etc...)
    @termo_pagamento.setter
    def termo_pagamento(self, termo_pagamento) -> None:
        self._termo_pagamento = termo_pagamento

    def adicionar_item_fornecedor(self, item : Type[Item], valor: float)->None:
         self._lista_itens.append(item)
         self._valores_itens.append(valor)

    def printar_item(self, item :str)-> str:
        for i in range(len(self._lista_itens)):
            if self._lista_itens[i].nome == item:
                return f'{self._lista_itens[i].nome} , {self._valores_itens[i]}'
        else:
             return f'item não encontrado'