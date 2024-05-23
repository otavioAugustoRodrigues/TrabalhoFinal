from Categorias import Categoria
from Controles import aumentarIdItem

class Item:
  def __init__(self, nome : str, quantidade : int, categoria : Categoria, valor : float) -> None:
    self.nome = nome,
    self.quantidade = quantidade,
    self.categoria = categoria,
    self.valor = valor,
    self.itemId = 0

def criarItem(nome : str, quantidade : int, categoria : Categoria, valor : float) -> Item:
  ItemCriado = Item(nome, quantidade, categoria, valor)
  ItemCriado.itemId = 1
  aumentarIdItem()
  return ItemCriado

escola = Categoria("Itens de escola",0)

lapis = criarItem("lapis", 4, escola, 4.7)
print(lapis.itemId)
cola = criarItem("cola", 7, escola, 2.5)
print(cola.itemId)
