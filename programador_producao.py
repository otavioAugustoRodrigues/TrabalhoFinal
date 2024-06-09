from typing import Type
from item import *

class ProgramadorProducao:
    def transforma_item_ativo(item : Item) -> None:
        item.item_ativo = True
    
    def transforma_item_obsoleto(item : Item) -> None:
        item.item_ativo = False