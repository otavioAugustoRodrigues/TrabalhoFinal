from tkinter import *
from tkinter import ttk
from controle_estoque import ControleEstoque
from planilha_csv import *
from typing import Type
from item import Item
import tkinter as tk

'''
from bancoDeDados import BancoDados
bd = BancoDados()
'''

class Estoque( ):
  def __init__(self, home: tk.Tk)-> None:
   self.estoque = PlanilhaCSV.adiciona_itens_fornecedor_planilha_csv("teste.csv")
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
   self.lis = ttk.Treeview(self.frame1,columns=('id','nome','quantidade','categoria','valor', 'nome do fornecedor'), show='headings')

   self.lis.column('ID', width = 5 , anchor = "center")
   self.lis.heading('ID', text='ID',anchor="center")

   self.lis.column('nome', width = 30, anchor = "center")
   self.lis.heading('nome', text='NOME',anchor="center")

   self.lis.column('quantidade', width = 10 , anchor = "center")
   self.lis.heading('quantidade', text='QUANTIDADE',anchor="center")

   self.lis.column('categoria', width = 30)
   self.lis.heading('categoria', text='CATEGORIA',anchor="center")

   self.lis.column('valor', width = 10)
   self.lis.heading('valor', text='VALOR',anchor="center")

   self.lis.column('nome do fornecedor', width = 30)
   self.lis.heading('nome do fornecedor', text='NOME DO FORNECEDOR',anchor="center")
   
   self.lis.pack()

   self.lis.place(relx="0.05", rely="0.05", relwidth="0.9", relheight="0.9")
   self.estoque.padrao_imprime_estoque()
   for item in self.estoque.get_itens_cadastrados:
    self.lis.insert("","end", values=(item.get_id_item, item.get_nome_item, item.get_quantidade_item, item.get_categoria_item, item.get_valor_item, item.fornecedor.get_nome_fornecedor))