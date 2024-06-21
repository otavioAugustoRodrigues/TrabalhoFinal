from suprimentos import *

# Classe encarregada de comprar material -> aumenta qtd. de itens. 
class Comprador(Suprimentos):
    def opera_material(self, controle_estoque : Type[ControleEstoque], quantidade: int, nome_item : str, nome_fornecedor : str) -> None:
        if controle_estoque.retorna_item_nome_fornecedor(nome_item, nome_fornecedor) is not None:
            item = controle_estoque.retorna_item_nome_fornecedor(nome_item, nome_fornecedor) is not None
            item.set_quantidade_item = item.get_quantidade_item + quantidade
        else:
            print("Item não existe/é obsoleto. Sem permissão para compra!")     