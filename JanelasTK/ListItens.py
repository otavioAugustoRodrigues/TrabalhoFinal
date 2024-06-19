from tkinter import *
from tkinter import ttk
from controle_estoque import ControleEstoque
from typing import Type
from item import Item
import tkinter as tk
from bancoDeDados import BancoDados

bd = BancoDados()

class ListItens( ):
  def __init__(self, home: tk.Tk)-> None:
   self.controle_estoque = bd.le_controle()
   self.janela = Tk()
   self.listitens()
   self.frame()
   self.botoes(home)
   self.lista()
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

  def voltar(self, home: tk.Tk):
   self.janela.destroy()
   home.janela.deiconify()
   
  def botoes(self, home: tk.Tk)->None:
    self.botaoVoltar = Button(self.frame2, text="VOLTAR", command=lambda:self.voltar(home))
    self.botaoVoltar.place(relx="0.5", rely="0.5",relwidth="0.25", relheight="0.30", anchor="center")

  def lista(self)-> None:
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

   for i in range(len(self.controle_estoque.itens_cadastrados)):
    id = self.controle_estoque.itens_cadastrados[i].item_id
    nome = self.controle_estoque.itens_cadastrados[i].nome
    quant = self.controle_estoque.itens_cadastrados[i].quantidade
    categoria = self.controle_estoque.itens_cadastrados[i].categoria
    self.lis.insert("","end", values=(id, nome, quant,categoria))