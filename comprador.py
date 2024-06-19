from suprimentos import *

# Classe encarregada de comprar material -> aumenta qtd. de itens. 
class Comprador(Suprimentos):
    def opera_material(self, item: 'Item', quantidade: int) -> None:
        if item.get_item_ativo == True:
            item.set_quantidade_item = item.get_quantidade_item + quantidade