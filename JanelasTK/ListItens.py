from tkinter import *
from tkinter import ttk
from controle_estoque import ControleEstoque
from typing import Type
from item import Item


class ListItens( ):
  def __init__(self, controle: Type[ControleEstoque])-> None:
   self.janela = Tk()
   self.listitens()
   self.frame()
   self.botoes()
   self.lista(controle)
   self.janela.mainloop()

  def listitens(self)-> None:
   self.janela.title("LISTA DE ITENS")
   self.janela.configure(background = '#e1ede0')
   self.janela.geometry("700x500")
   self.janela.resizable(True,True)
   self.janela.maxsize(width=900,height=700)
   self.janela.minsize(width=500,height=400)

  def frame(self)-> None:
   self.frame1 = Frame(self.janela, bg='#e1ede0')
   self.frame1.place(relx="0", rely="0", relwidth="1", relheight="0.75")

   self.frame2 = Frame(self.janela, bg='#e1ede0')
   self.frame2.place(relx="0", rely="0.75", relwidth="1", relheight="0.25")

  def botoes(self)->None:
    self.botaoVoltar = Button(self.frame2, text="VOLTAR", command=self.janela.destroy)
    self.botaoVoltar.place(relx="0.5", rely="0.5",relwidth="0.25", relheight="0.30", anchor="center")

  def lista(self, cont: Type[ControleEstoque])-> None:
   self.lis = ttk.Treeview(self.frame1,columns=('id','nome','quant','cate'), show='headings')
   
   self.lis.column('id',width=50,anchor="center")
   self.lis.column('nome',width=200)
   self.lis.column('quant',width=50,anchor="center")
   self.lis.column('cate',width=200)
   self.lis.heading('id', text='ID',anchor="center")
   self.lis.heading('nome', text='NOME',anchor="center")
   self.lis.heading('quant', text='QUANTIDADE',anchor="center")
   self.lis.heading('cate', text='CATEGORIA',anchor="center")
   self.lis.pack()

   self.lis.place(relx="0.05", rely="0.05", relwidth="0.9", relheight="0.9")

   for i in range(len(cont.itens_cadastrados)):
    id = cont.itens_cadastrados[i].item_id
    nome = cont.itens_cadastrados[i].nome
    quant = cont.itens_cadastrados[i].quantidade
    categoria = cont.itens_cadastrados[i].categoria
    self.lis.insert("","end", values=(id, nome, quant,categoria))
   
  
      


   