from typing import Type, List
from item import *
from fornecedor import *
import csv 

class ControleEstoque:
    # Constructor do controle de estoque.
    def __init__(self) -> None:
        self._itens_cadastrados = []
        self._fornecedores_cadastrados = []
        self._id_item_controle = 0
        self._id_fornecedor_controle = 0

    # Getter para a lista de itens cadastrados.
    @property
    def get_itens_cadastrados(self) -> Type[Item]:
            return self._itens_cadastrados
    
    # Setter para o array de itens cadastrados implementado a partir de uma slice.
    @get_itens_cadastrados.setter
    def set_itens_cadastados(self, itens : List[Item]) -> None:
        self._itens_cadastrados = itens[:]
    
    # Getter para a lista de fornecedores cadastrados.
    @property
    def get_fornecedores_cadastrados(self) -> Type[Fornecedor]:
            return self._fornecedores_cadastrados

    # Getter para o último ID do item cadastrado no banco de dados.
    @property
    def get_item_id_controle(self) -> int:
        return self._id_item_controle
    
    @get_item_id_controle.setter
    def set_item_id_controle(self, id : int) -> None:
        self._id_item_controle = id
    
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
            if i.fornecedor is not None:
                if (i.get_nome_item == item.get_nome_item and 
                    i.get_categoria_item == item.get_categoria_item and
                    i.get_id_item == item.get_id_item and
                    i.fornecedor.get_nome_fornecedor == item.fornecedor.get_nome_fornecedor
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
            if item.fornecedor is not None:
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

    # Método responsável por imprimir o cabeçalho da lista de itens.
    def padrao_imprime_cabecalho(self) -> None:
        print(f"{'ID' :<5}\t{'Nome' :<15}\t{'Qtd.' :<5}\t{'Categoria' :<25}\t{'Valor' :<10}\t{'Valor total em estoque':<25}\t{'Nome do fornecedor' :<20}\t")

    # Método responsável por imprimir as informações de cada item da lista de itens.
    def padrao_imprime_estoque(self) -> None:
        self.padrao_imprime_cabecalho()
        for i_item_cadastrado in self.get_itens_cadastrados:
            if i_item_cadastrado.fornecedor is None:
                print(f"{i_item_cadastrado.get_id_item :< 5}\t{i_item_cadastrado.get_nome_item :<15}\t{i_item_cadastrado.get_quantidade_item :<5}\t{i_item_cadastrado.get_categoria_item :<25}\t{i_item_cadastrado.get_valor_item :<10}\t{i_item_cadastrado.get_valor_total_estoque():<10}\t{'0':<30}")   
            else:
                print(f"{i_item_cadastrado.get_id_item :< 5}\t{i_item_cadastrado.get_nome_item :<15}\t{i_item_cadastrado.get_quantidade_item :<5}\t{i_item_cadastrado.get_categoria_item :<25}\t{i_item_cadastrado.get_valor_item :<10}\t{i_item_cadastrado.get_valor_total_estoque():<10}\t{i_item_cadastrado.fornecedor.get_nome_fornecedor:<30}")   

    # Método que imprime na tela todos os fornecedores cadastrados no controle de estoque.
    def printa_terminal_fornecedores_cadastrados(self):
        for i in self.get_fornecedores_cadastrados:
            print(f"ID do fornecedor: {i.get_id_fornecedor}, Nome do fornecedor cadastrado: {i.get_nome_fornecedor}, país: {i.get_pais_fornecedor}, termo de pagamento: {i.get_termo_pagamento_fornecedor}")

    # Método que cadastra itens para um determinado fornecedor aqui, passaremos um item como argumento e, ao cadastrarmos 
    # ele como vendido pelo fornecedor, este ficará encarregado de passar as demais informações, como o valor da venda e 
    # o próprio nome do fornecedor que vende este item.
    def cadastra_item_fornecedor(self, fornecedor : Type[Fornecedor], item : Type[Item], valor_item_fornecedor : float) -> None:
        if self.verifica_fornecedor_cadastrado(fornecedor):
            for itens in self.get_itens_cadastrados:
                if itens.checa_item_cadastrado_fornecedor(item.get_nome_item, fornecedor):
                    print(f"item {itens.get_nome_item} já cadastrado para o fornecedor {fornecedor.get_nome_fornecedor}. Atualizando valor do item...")
                    itens.set_valor_item = valor_item_fornecedor
                    break
            else:
                novo_item_cadastrado = Item(item.get_nome_item, item.get_categoria_item)
                novo_item_cadastrado.set_valor_item = valor_item_fornecedor
                novo_item_cadastrado.set_fornecedor(fornecedor)
                self.cadastra_item(novo_item_cadastrado)

        else:
            print("fornecedor não cadastrado!")

    def retorna_item_nome_fornecedor(self, item_nome : str, fornecedor_nome : str) -> Type[Item]:
        for item in self.get_itens_cadastrados:
            if item.fornecedor is not None:
                if item.nome == item_nome and item.fornecedor.get_nome_fornecedor == fornecedor_nome:
                    return item
                
    def inicializa_controle_estoque(self, nomearquivo : str) -> None:
        with open(nomearquivo, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                print(row['nome'])  # Debugging: Print each row
                item = Item(row['nome'], row['categoria'])
                item.set_quantidade_item = row['quantidade']
                item.set_id_item = row['ID']
                fornecedor = Fornecedor(row['fornecedor'],row['pais fornecedor'], row['termo pgto fornecedor'])
                fornecedor.set_id_fornecedor = row['ID do fornecedor']
                self.cadastra_item_fornecedor(row['fornecedor'], item, float(row['valor']))
                
                current_id = int(row['ID'])
                if not hasattr(self, 'max_id_controle'):
                    self.max_id_controle = current_id
                else:
                    self.max_id_controle = max(self.max_id_controle, current_id)

                # Optional: set the max_id_controle attribute directly
                self.set_item_id_controle = self.max_id_controle