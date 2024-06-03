from abc import ABC, abstractmethod
from typing import Type
from item import *
from item import Item

class Suprimentos(ABC):
    @abstractmethod
    def varia_material(self, item : Type[Item], quantidade : int) -> None:
        pass

# Classe encarregada de comprar material -> aumenta qtd. de itens. 
class Comprador(Suprimentos):
    def varia_material(self, item: type[Item], quantidade: int) -> None:
        item.quantidade += quantidade

# Classe encarregada de vender material -> diminui qtd. de itens.
class Vendedor(Suprimentos):
    def varia_material(self, item: Item, quantidade: int) -> None:
        item.quantidade -= quantidade