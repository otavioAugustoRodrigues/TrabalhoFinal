from suprimentos import *

# Classe encarregada de comprar material -> aumenta qtd. de itens. 
class Comprador(Suprimentos):
    def varia_material(self, item: type[Item], quantidade: int) -> None:
        item.quantidade_item += quantidade