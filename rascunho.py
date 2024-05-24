'''
coloquei todas as classes/métodos no mesmo arquivo apenas porque fui fazendo, depois vamos organizando tudo...
'''

class Item:
'''
constructor do nosso item.
'''
    def __init__(self, nome : str, quantidade : int, categoria : Categoria, valor : float) -> None:
        self.nome = nome,
        self.quantidade = quantidade,
        self.categoria = categoria,
        self.valor = valor,
        self.item_id = 0

'''
-> implementar um setter para o nome do item (ex.: se é string etc...)
'''
    @nome.setter
    def nome(self, nome_item) -> None:
        pass

'''
-> implementar um setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
'''
    @valor.setter
    def valor(self, valor_item) -> None:
        pass

'''
-> implementar um setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso
   banco de dados).
'''
    @categoria.setter
    def categoria(self, categoria_item) -> None:
        pass

class ControleEstoque:
'''
constructor do nosso controle de estoque.
'''
    def __init__(self) -> None:
        self.itens_cadastrados = []
        self.itens_estoque = []
        self.item_id = 0
        pass
    
'''
a ideia aqui é implementar uma função que vai verificar se um item
está cadastrado em nosso banco de itens cadastrados.
'''
    def verifica_item_cadastrado(self, item : Type[Item]) -> bool:
        for i in self.itens_cadastrados:
            if i.nome == item.nome:
                return True

'''
a ideia aqui é implementar uma função que vai cadastrar um item
no nosso banco de itens cadastrados.
'''                                                
    def cadastra_item(self, item : Type[Item]) -> None:
        if (not self.verifica_item_cadastrado(item):
            self.itens_cadastrados.append(item)
            
'''
a ideia aqui é implementar uma função que vai remover um item
do nosso banco de itens cadastrados.
'''                    
    def remove_item(self, item : Type[Item] -> None:
        if self.verifica_item_cadastrado(item):

'''
a ideia aqui é implementar uma função que vai retornar o índice
do membro da lista que estamos procurando (e utilizar em outras
funções futuramente);
'''                    
    def localiza_item(self, item : Type[Item] -> int:
        for i in self.itens_cadastrados:
            if i.nome == item.nome:
                return self.itens_cadastrados.index(i)
