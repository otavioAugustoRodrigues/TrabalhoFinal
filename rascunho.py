import csv
from typing import Type

# Módulo que implementa informações sobre dia/hora.
from datetime import datetime

# Módulo que implementa interfaces gráficas para o Python
import tkinter as tk
from tkinter import ttk


class Item:
    def __init__(self, nome : str, quantidade : int, categoria : str, valor : float, item_ativo : bool) -> None:
        self._nome_item = nome
        self._quantidade = quantidade
        self._categoria_item = categoria
        self._valor_item = valor
        self._item_ativo = item_ativo
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
    def valor(self) -> float:
            return self._valor_item

    # Setter para o valor do item (ex.: se o valor é muito grande/pequeno etc...
    @valor.setter
    def valor(self, valor) -> None:
        self._valor_item = valor

    # Getter para o valor do item (ex.: se é string etc...)
    @property
    def categoria(self) -> str:
            return self._categoria_item
    
    # Setter para a categoria do item (ex.: se a categoria é válida - ela já existe em nosso banco de dados).
    @categoria.setter
    def categoria(self, categoria) -> None:
        self._categoria_item = categoria

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
        
     
class ControleEstoque:
    # Constructor do controle de estoque.
    def __init__(self) -> None:
        self._itens_cadastrados = []
        self._fornecedores_cadastrados = []
        self._item_id_controle = 0
        self._fornecedor_id_controle = 0
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
            if i.nome == item.nome and i.nome == item.valor:
                return True
        else:
             return False 
        
    # Método que verifica se um fornecedor está cadastrado no banco de fornecedores cadastrados.
    def verifica_fornecedor_cadastrado(self, fornecedor : Type[Fornecedor]) -> None:
        for i in self._itens_cadastrados:
            if i.nome == fornecedor.nome_fornecedor:
                return True
        else:
             return False    
            
    # Método que cadastra um item no banco de itens cadastrados.
    def cadastra_item(self, item : Type[Item]) -> None:
        if (not self.verifica_item_cadastrado(item)):
            self._item_id_controle += 1
            item.item_id = self._item_id_controle
            self._itens_cadastrados.append(item)
            print(f'{item.nome} {item.item_id} cadastrado com sucesso!')

    # Método que cadastra um fornecedor no banco de fornecedores cadastrados.
    def cadastra_fornecedor(self, fornecedor : Type[Fornecedor]) -> None:
        if (not self.verifica_fornecedor_cadastrado(fornecedor)):
            self._fornecedor_id_controle += 1
            fornecedor._id_fornecedor = self._fornecedor_id_controle
            self._fornecedores_cadastrados.append(fornecedor)
            print(f'{fornecedor.nome_fornecedor} {fornecedor._id_fornecedor} cadastrado com sucesso!')


    # "Remove" um item da lista, alterando seu estado para obsoleto.
    def remove_item(self, item : Type[Item]) -> None:
        if self.verifica_item_cadastrado(item):
            item._item_ativo = False


    # Retorna o índice do membro da lista.
    def localiza_item(self, item : Type[Item]) -> int:
        for i in self.itens_cadastrados:
            if i.nome == item.nome:
                return self.itens_cadastrados.index(i)


# Classe responsável por ordenar o que está cadastrado no estoque de acordo com algum parâmetro.
class OrdenaEstoque:

    # Classe responsável por ordenar o que está cadastrado no estoque de acordo com o nome dos itens.
    def ordena_nome(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_nome = sorted(controle_estoque.itens_cadastrados, key=lambda x: x.nome)
        print(f"{'Nome':<15}\t{'Qtd.':<5}\t{'Categoria':<25}\t{'Valor':<10}")
        for i in controle_estoque_ordenado_nome:
            print(f"{i.nome:<15}\t{i.quantidade:<5}\t{i.categoria:<25}\t{i.valor:<10}")

    # Classe responsável por ordenar o que está cadastrado no estoque de acordo com a categoria dos itens.
    def ordena_categoria(self, controle_estoque : Type[ControleEstoque]) -> None:
        controle_estoque_ordenado_nome = sorted(controle_estoque.itens_cadastrados, key=lambda x: x.categoria)
        print(f"{'Nome':<15}\t{'Qtd.':<5}\t{'Categoria':<25}\t{'Valor':<10}")
        for i in controle_estoque_ordenado_nome:
            print(f"{i.nome:<15}\t{i.quantidade:<5}\t{i.categoria:<25}\t{i.valor:<10}")       


# Classe responsável por filtrar o que está cadastrado no estoque de acordo com algum parâmetro.
class FiltraEstoque:

    # método responsável por filtrar o que está cadastrado no estoque de acordo com o nome do item.
    def filtra_nome(self, controle_estoque : Type[ControleEstoque], nome_filtro : str) -> None:
        controle_estoque_ordenado_nome = []
        for i in controle_estoque.itens_cadastrados :
            if i.nome == nome_filtro:
                controle_estoque_ordenado_nome.append(i)
        print(f"{'Nome':<15}\t{'Qtd.':<5}\t{'Categoria':<25}\t{'Valor':<10}")
        for j in controle_estoque_ordenado_nome:
            print(f"{j.nome:<15}\t{j.quantidade:<5}\t{j.categoria:<25}\t{j.valor:<10}")       
            

# Class responsável por imprimir o estado atual do estoque.
class GerenciadorPlanilha:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d/%m")
    
    # método responsável por imprimir o estado atual no terminal.
    def le_csv(self, nomearquivo : csv) -> None:
        with open(nomearquivo, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            #spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            print(f"{'Nome':<15}\t{'Qtd.':<5}\t{'Categoria':<25}\t{'Valor':<10}")
            for row in reader:
                print(f"{row['nome']:15}\t{row['quantidade']:5}\t{row['categoria']:25}\t{row['valor']}")
                
    # função responsável por imprimir o estado atual do terminal em um arquivo .csv.
    def escreve_csv_colunas_diferentes(self, nomearquivo : csv, controle_estoque : Type[ControleEstoque]) -> None:
        with open(nomearquivo, 'w', newline='') as csvfile:
            fieldnames = ['nome', 'quantidade', 'categoria', 'valor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for element in controle_estoque.itens_cadastrados:
                writer.writerow({'nome': element.nome, 'quantidade': element.quantidade, 'categoria': element.categoria, 'valor': element.valor})

    # Método responsável por imprimir uma GUI com informações do controle de estoque no dia atual.
    def escreve_tela_GUI(self, controle_estoque : Type[ControleEstoque]) -> None:
        root = tk.Tk()
        root.title(f"Controle de Estoque - {self.formatted_date}")

        table = ttk.Treeview(root)
        table['columns'] = ['nome', 'qtd.', 'categoria', 'valor']

        table.heading("#0", text="Object")
        table.heading("nome", text="Nome")
        table.heading("qtd.", text="Qtd.")
        table.heading("categoria", text="Categoria")
        table.heading("valor", text="Valor")

        for i, obj in enumerate(controle_estoque.itens_cadastrados, start=1):
            table.insert("", "end", text=f"{obj.item_id}", values=(obj.nome, obj.quantidade, obj.categoria, obj.valor))

        table.pack(expand=True, fill=tk.BOTH)

        root.mainloop()

# Classe encarregada de realizar mudanças no estado do material.
class VariaMaterial:
    pass

# Classe encarregada de comprar material -> aumenta qtd. de itens. 
class CompraMaterial(VariaMaterial):
    pass


# Classe encarregada de vender material -> diminui qtd. de itens.
class VendaMaterial(VariaMaterial):
    pass


def main():  
    controle_estoque = ControleEstoque()
    gerenciador_planilha = GerenciadorPlanilha()

    item1 = Item("varistor", 2, "componente eletrônico", 0.35, False)
    controle_estoque.cadastra_item(item1)

    item2 = Item("lapis", 10, "item de escola", 2.00, True)
    controle_estoque.cadastra_item(item2)

    item3 = Item("cola", 50, "item de escola", 2.00, True)
    controle_estoque.cadastra_item(item3)
    
    item4 = Item("lapis", 10, "item de escola", 2.50, True)
    controle_estoque.cadastra_item(item4)
    
    gerenciador_planilha.escreve_csv_colunas_diferentes('teste.csv', controle_estoque)

    gerenciador_planilha.le_csv('teste.csv')
    gerenciador_planilha.escreve_tela_GUI(controle_estoque)

    fornecedorA = Fornecedor("fornA", "BR", "Faturado")
    controle_estoque.cadastra_fornecedor(fornecedorA)
    fornecedorA.adicionar_item_fornecedor(item1,0.35)
    fornecedorA.adicionar_item_fornecedor(item2,5.00)
    fornecedorA.adicionar_item_fornecedor(item3,7.50)

    fornecedorB = Fornecedor("fornB", "US", "Boleto")
    controle_estoque.cadastra_fornecedor(fornecedorB)
    fornecedorB.adicionar_item_fornecedor(item1,0.50)
    fornecedorB.adicionar_item_fornecedor(item2,4.80)
    fornecedorB.adicionar_item_fornecedor(item3,8.60)

    print(controle_estoque._fornecedores_cadastrados[0].printar_item("cola"))
    
    ordena_estoque = OrdenaEstoque()
    ordena_estoque.ordena_nome(controle_estoque)
    ordena_estoque.ordena_categoria(controle_estoque)
    
    filtra_estoque  = FiltraEstoque()
    filtra_estoque.filtra_nome(controle_estoque, "lapis")
    
main()
