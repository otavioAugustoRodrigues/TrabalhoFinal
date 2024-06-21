from abc import ABC, abstractmethod
from typing import Type
from item import *
from controle_estoque import *

class Suprimentos(ABC):
    @abstractmethod
    def opera_material(self, controle_estoque : Type[ControleEstoque], quantidade: int, nome_item : str, nome_fornecedor : str) -> None:
        pass