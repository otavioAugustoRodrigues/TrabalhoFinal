import csv
from typing import Type 

class Item:
    def __init__(self, nome : str, quantidade : int, categoria : str, valor : float, item_ativo : bool) -> None:
        self._nome_item = nome
        self._quantidade = quantidade
        self._categoria_item = categoria
        self._valor_item = valor
        self._item_ativo = item_ativo
        self._item_id = 0


# -> a ideia aqui será implementar herança para os diferentes tipos de cadastros entre itens vendidos pelo fornnecedor e aqueles em controle no estoque.
#class ItemEstoque(Item):
#    def __init__(self, nome : str, quantidade : int, categoria : str, valor : float, item_ativo : bool) -> None:
#        super().__init__(nome, categoria, item_ativo)
#    pass

#class ItemFornecedor(Item):
#    pass

# -> implementa um getter para o nome do item (ex.: se é string etc...)
    @property
    def nome(self) -> str:
            return self._nome_item
        
# -> implementa um setter para o nome do item (ex.: se é string etc...)
    @nome.setter
    def nome(self, nome) -> None:
        self._nome_item = nome

    # -> implementa um getter para o nome do item (ex.: se é string etc...)
    @property
    def quantidade(self) -> int:
            return self._quantidade
        
# -> implementa um setter para o nome do item (ex.: se é string etc...)
    @quantidade.setter
    def quantidade(self, quantidade) -> None:
        self._quantidade = quantidade

# -> implementa um getter para o valor do item (ex.: se é string etc...)
    @property
    def valor(self) -> float:
            return self._valor_item

# -> implementa um setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
    @valor.setter
    def valor(self, valor) -> None:
        self._valor_item = valor

# -> implementa um getter para o valor do item (ex.: se é string etc...)
    @property
    def categoria(self) -> str:
            return self._categoria_item
    
# -> implementar um setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso
#   banco de dados).
    @categoria.setter
    def categoria(self, categoria) -> None:
        self._categoria_item = categoria

# -> implementa um getter para verificar se o item está obsoleto ou não.
    @property
    def item_ativo(self) -> int:
            return self._item_ativo
    
# -> implementar um setter para alterar o estado atual do item entre obsoleto ou não.
    @item_ativo.setter
    def item_ativo(self, item_ativo) -> None:
        self._item_ativo = item_ativo

# -> implementa um getter para o item_id do item 
    @property
    def item_id(self) -> int:
            return self._item_id
    
# -> implementar um setter para a categoria do item 
    @item_id.setter
    def item_id(self, item_id) -> None:
        self._item_id = item_id
        

class ControleEstoque:
# constructor do nosso controle de estoque.
    def __init__(self) -> None:
        self._itens_cadastrados = []
        self._itens__controle = []
        self._item_id_controle = 0
        pass

# -> implementa um getter para a lista de itens cadastrados.
    @property
    def itens_cadastrados(self) -> Type[Item]:
            return self._itens_cadastrados

# -> implementa um getter para a lista de itens cadastrados.
    @property
    def item_id_controle(self) -> int:
            return self._item_id_controle
    
# a ideia aqui é implementar uma função que vai verificar se um item
# está cadastrado em nosso banco de itens cadastrados.
    def verifica_item_cadastrado(self, item : Type[Item]) -> bool:
        for i in self._itens_cadastrados:
            if i.nome == item.nome:
                return True

# a ideia aqui é implementar uma função que vai cadastrar um item
# no nosso banco de itens cadastrados.
    def cadastra_item(self, item : Type[Item]) -> None:
        if (not self.verifica_item_cadastrado(item)):
            self._item_id_controle += 1
            item.item_id = self._item_id_controle
            self._itens_cadastrados.append(item)
            print(f'{item.nome} {item.item_id} cadastrado com sucesso!')
            
# a ideia aqui é implementar uma função que vai remover um item
# do nosso banco de itens cadastrados.
    def remove_item(self, item : Type[Item]) -> None:
        if self.verifica_item_cadastrado(item):
            item._item_ativo = False

# a ideia aqui é implementar uma função que vai retornar o índice
# do membro da lista que estamos procurando (e utilizar em outras
# funções futuramente);
    def localiza_item(self, item : Type[Item]) -> int:
        for i in self.itens_cadastrados:
            if i.nome == item.nome:
                return self.itens_cadastrados.index(i)


# a ideia aqui é implementar uma classe que vai ser responsável
# por imprimir o controle
class GerenciadorPlanilha:
    def le_csv(self, nomearquivo):
        with open(nomearquivo, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            #spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                print(row['nome'],"\t", row['quantidade'],"\t",row['categoria'],"\t",row['valor'])

    def escreve_csv_colunas_diferentes(self, nomearquivo, controle_estoque : Type[ControleEstoque]):
        with open(nomearquivo, 'w', newline='') as csvfile:
            fieldnames = ['nome', 'quantidade', 'categoria', 'valor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for element in controle_estoque.itens_cadastrados:
                writer.writerow({'nome': element.nome, 'quantidade': element.quantidade, 'categoria': element.categoria, 'valor': element.valor})


class Fornecedor:
    def __init__(self, nome : str, pais : str, termo_pagamento : str) -> None:
        self._nome_fornecedor = nome
        self._pais = pais
        self._termo_pagamento = termo_pagamento
        self._lista_itens = []
        self._valores_itens = []

# -> implementa um getter para o nome do fornecedor (ex.: se é string etc...)
    @property
    def nome_fornecedor(self) -> str:
        return self._nome_fornecedor
        
# -> implementa um setter para o nome do fornecedor (ex.: se é string etc...)
    @nome_fornecedor.setter
    def nome_fornecedor(self, nome) -> None:
        self._nome_fornecedor = nome
    
# -> implementa um getter para o país do fornecedor (ex.: se é string etc...)
    @property
    def pais(self) -> str:
        return self._pais
        
# -> implementa um setter para o país do fornecedor (ex.: se é string etc...)
    @pais.setter
    def pais(self, pais) -> None:
        self.pais = pais
    
# -> implementa um getter para o país do fornecedor (ex.: se é string etc...)
    @property
    def termo_pagamento(self) -> str:
        return self._termo_pagamento
        
# -> implementa um setter para o país do fornecedor (ex.: se é string etc...)
    @termo_pagamento.setter
    def termo_pagamento(self, termo_pagamento) -> None:
        self._termo_pagamento = termo_pagamento

    def adicionar_iten_fornecedor(self, item : Type[Item], valor: float)->None:
         self._lista_itens.append(item)
         self._valores_itens.append(valor)

    def printar_item(self, item :str)-> str:
        for i in range(len(self._lista_itens)):
            if self._lista_itens[i].nome == item:
                return f'{self._lista_itens[i].nome} , {self._valores_itens[i]}'
        else:
             return f'item não encontrado'
            
def main():


    controle_estoque = ControleEstoque()
    gerenciador_planilha = GerenciadorPlanilha()

    item1 = Item("varistor", 2, "componente eletrônico", 0.35, False)
    controle_estoque.cadastra_item(item1)

    item2 = Item("lapis", 10, "item de escola", 2.00, True)
    controle_estoque.cadastra_item(item2)

    item3 = Item("cola", 50, "item de escola", 2.00, True)
    controle_estoque.cadastra_item(item3)
    gerenciador_planilha.escreve_csv_colunas_diferentes('teste.csv', controle_estoque)

    gerenciador_planilha.le_csv('teste.csv')

    fornecedorA = Fornecedor("fornA", "BR", "Faturado")
    fornecedorA.adicionar_iten_fornecedor(item1,0.35)
    fornecedorA.adicionar_iten_fornecedor(item2,5.00)
    fornecedorA.adicionar_iten_fornecedor(item3,7.50)

    print(fornecedorA.printar_item("cola"))
    

main()
