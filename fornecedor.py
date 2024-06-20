from typing import Type
from item import *

class Fornecedor:
    def __init__(self, nome : str, pais : str, termo_pagamento : str) -> None:
        self._nome_fornecedor = nome
        self._pais_fornecedor = pais
        self._termo_pagamento_fornecedor = termo_pagamento
        self._id_fornecedor = 0
        # self._lista_itens = []
        # self._valores_itens = []

    # Getter para o nome do fornecedor (ex.: se é string etc...)
    @property
    def get_nome_fornecedor(self) -> str:
        return self._nome_fornecedor
        
    # Setter para o nome do fornecedor (ex.: se é string etc...)
    @get_nome_fornecedor.setter
    def set_nome_fornecedor(self, nome : str) -> None:
        self._nome_fornecedor = nome
    
    # Getter para o país do fornecedor (ex.: se é string etc...)
    @property
    def get_pais_fornecedor(self) -> str:
        return self._pais_fornecedor
        
    # Setter para o país do fornecedor (ex.: se é string etc...)
    @get_pais_fornecedor.setter
    def set_pais_fornecedor(self, pais : str) -> None:
        self._pais_fornecedor = pais
    
    # Getter para o país do fornecedor (ex.: se é string etc...)
    @property
    def get_termo_pagamento_fornecedor(self) -> str:
        return self._termo_pagamento_fornecedor
        
    # Setter para o país do fornecedor (ex.: se é string etc...)
    @get_termo_pagamento_fornecedor.setter
    def set_termo_pagamento_fornecedor(self, termo_pagamento : str) -> None:
        if type(termo_pagamento) == str:
            self._termo_pagamento = termo_pagamento
        else:
            print("Nome inválido!")
            input_user = input("Informe o nome do fornecedor:")
            self.set_nome_fornecedor(input_user)
    
    # Getter para o ID do fornecedor 
    @property
    def get_id_fornecedor(self) -> int:
        return self._id_fornecedor
        
    @get_id_fornecedor.setter
    def set_id_fornecedor(self, id : int) -> None:
        self._id_fornecedor = id
