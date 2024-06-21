from typing import Type
from item import *
from controle_estoque import *

class ProgramadorProducao:
    def transforma_item_ativo(self, controle_estoque : Type[ControleEstoque], nome_item : str) -> None:
        for i in controle_estoque.get_itens_cadastrados:
            if i.get_nome_item == nome_item:
                i.set_item_ativo = True 
                print(f"Item {i.get_nome_item} foi configurado como ativo!")
    
    def transforma_item_obsoleto(self, controle_estoque : Type[ControleEstoque], nome_item : str) -> None:
        for i in controle_estoque.get_itens_cadastrados:
            if i.get_nome_item == nome_item:
                i.set_item_ativo = False
                print(f"Item {i.get_nome_item} foi configurado como obsoleto!")
