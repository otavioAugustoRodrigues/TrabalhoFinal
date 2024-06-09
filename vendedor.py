from suprimentos import *

# Classe encarregada de vender material -> diminui qtd. de itens.
class Vendedor(Suprimentos):
    def varia_material(self, item: Item, quantidade: int) -> None:
        item.quantidade_item -= quantidade