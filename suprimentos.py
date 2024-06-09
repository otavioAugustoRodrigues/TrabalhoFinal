from abc import ABC, abstractmethod
from typing import Type
from item import *
from item import Item

class Suprimentos(ABC):
    @abstractmethod
    def varia_material(self, item : Type[Item], quantidade : int) -> None:
        pass

    def transforma_item_ativo(item : Item) -> None:
        item.item_ativo = True
    
    def transforma_item_obsoleto(item : Item) -> None:
        item.item_ativo = False