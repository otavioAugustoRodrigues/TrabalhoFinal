class Item:
    def __init__(self, nome : str, quantidade : int, categoria : str, valor : float, item_ativo : bool, materia_prima : bool) -> None:
        self._nome_item = nome
        self._quantidade = quantidade
        self._categoria_item = categoria
        self._valor_item = valor
        self._item_ativo = item_ativo
        self._materia_prima = materia_prima
        self._item_id = 0

    # Getter para o nome do item (ex.: se é string etc...)
    @property
    def nome(self) -> str:
            return self._nome_item
        
    # Setter para o nome do item (ex.: se é string etc...)
    @nome.setter
    def nome(self, nome) -> None:
        self._nome_item = nome

    # Getter para o nome do item (ex.: se é string etc...)
    @property
    def quantidade(self) -> int:
            return self._quantidade
        
    # Setter para o nome do item (ex.: se é string etc...)
    @quantidade.setter
    def quantidade(self, quantidade) -> None:
        self._quantidade = quantidade

    # Getter para o valor do item (ex.: se é string etc...)
    @property
    def categoria(self) -> str:
            return self._categoria_item
    
    # Setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso banco de dados).
    @categoria.setter
    def categoria(self, categoria) -> None:
        self._categoria_item = categoria
    
    # Getter para o valor do item (ex.: se é string etc...)
    @property
    def valor(self) -> float:
            return self._valor_item

    # Setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
    @valor.setter
    def valor(self, valor) -> None:
        self._valor_item = valor

    # Getter para verificar se o item está obsoleto ou não.
    @property
    def item_ativo(self) -> bool:
            return self._item_ativo
    
    # Setter para alterar o estado atual do item entre obsoleto ou não.
    @item_ativo.setter
    def item_ativo(self, item_ativo) -> None:
        self._item_ativo = item_ativo

    # Getter para verificar se o item é matéria prima ou não.
    @property
    def materia_prima(self) -> bool:
            return self._materia_prima
    
    # Setter para transformar um item em matéria prima ou produto acabado.
    @materia_prima.setter
    def materia_prima(self, materia_prima) -> None:
        self._materia_prima = materia_prima

    # Getter para o item_id do item 
    @property
    def item_id(self) -> int:
            return self._item_id
    
    # Setter para a categoria do item 
    @item_id.setter
    def item_id(self, item_id) -> None:
        self._item_id = item_id