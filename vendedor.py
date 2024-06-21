from suprimentos import *
# Classe encarregada de vender material -> diminui qtd. de itens.
class Vendedor(Suprimentos):
    def opera_material(self, controle_estoque : Type[ControleEstoque], quantidade: int, nome_item : str, nome_fornecedor : str) -> None:
        item = controle_estoque.retorna_item_nome_fornecedor(nome_item, nome_fornecedor)
        if item.get_item_ativo == True:
                item.set_quantidade_item = item.get_quantidade_item - quantidade
        else:
            print("Item não cadastrado!")