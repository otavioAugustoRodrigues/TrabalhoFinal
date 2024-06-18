from tkinter import *
from tkinter import ttk
from controle_estoque import ControleEstoque
from typing import Type
from item import Item
import tkinter as tk
from bancoDeDados import BancoDados

bd = BancoDados()

class CriarItem():
  def __init__(self, home: tk.Tk)-> None:
   self.controle_estoque = bd.le_controle()
   self.janela = Tk()
   self.cria()
   self.frame()
   self.botoes(home)
   self.janela.mainloop()

  def cria(self)-> None:
   self.janela.title("CRIAR ITEM")
   self.janela.configure(background = '#e1ede0')
   self.janela.geometry("700x500")
   self.janela.resizable(True,True)
   self.janela.maxsize(width=900,height=700)
   self.janela.minsize(width=500,height=400)

  def frame(self):
    self.frame1 = Frame(self.janela, bg='#fffef0')
    self.frame1.place(relx="0.025", rely="0.025", relwidth="0.95", relheight="0.7")

    self.frame2 = Frame(self.janela, bg='#e1ede0')
    self.frame2.place(relx="0", rely="0.75", relwidth="1", relheight="0.25")

  def voltar(self, home: tk.Tk):
   self.janela.destroy()
   home.janela.deiconify()

  def is_int(self,string: str)-> bool:
    try:
      int(string)
      return True
    except:
      return False

  def is_float(self,string: str)-> bool:
    try:
      float(string)
      return True
    except:
      return False
    
  def criarItem(self):
    n = self.getNome.get()
    q = self.getQuant.get()
    c = self.getCategoria.get()
    v = self.getValor.get()

    a=0
    for i in range(len(self.controle_estoque.itens_cadastrados)):
      if(self.controle_estoque.itens_cadastrados[i].nome == n):
        a=1
        break
    if(a==0 and self.is_int(q)== True and c != "" and self.is_float(v)== True):
      item = Item(n,int(q),c,v,True)
      self.controle_estoque.cadastra_item(item)
      bd.salva_controle(self.controle_estoque)
      self.getNome.delete(0,tk.END)
      self.getQuant.delete(0,tk.END)
      self.getCategoria.delete(0,tk.END)
      self.getValor.delete(0,tk.END)
      try:
        self.labelAvisoNome.destroy
      except:
        pass
      try:
        self.labelAvisoQuant.destroy
      except:
        pass
      try:
        self.labelAvisoCategoria.destroy
      except:
        pass
      try:
        self.labelAvisoValor.destroy
      except:
        pass
      
      self.labelItemCriad =  Label(self.frame1,text="ITEM CRIADO COM SUCESSO",bg='#fffef0')
      self.labelItemCriad.place(relx="0.50", rely="0.45",relwidth="0.50", relheight="0.1")


    else:
      if(a == 1):
        self.labelAvisoNome =  Label(self.frame1,text="ESTE ITEM JÁ EXISTE",bg='#fffef0')
        self.labelAvisoNome.place(relx="0.50", rely="0.10",relwidth="0.50", relheight="0.075")
      else:
        try:
          self.labelAvisoNome.destroy
        except:
          pass

      if(self.is_int(q)== False):
        self.labelAvisoQuant =  Label(self.frame1,text="VALOR INVÁLIDO",bg='#fffef0')
        self.labelAvisoQuant.place(relx="0.50", rely="0.20",relwidth="0.50", relheight="0.075")
      else:
        try:
          self.labelAvisoQuant.destroy
        except:
          pass
      if(c == ""):
        self.labelAvisoCategoria =  Label(self.frame1,text="VALOR INVÁLIDO",bg='#fffef0')
        self.labelAvisoCategoria.place(relx="0.50", rely="0.30",relwidth="0.50", relheight="0.075")
      else:
        try:
          self.labelAvisoCategoria.destroy
        except:
          pass
      if(self.is_float(v)== False):
        self.labelAvisoValor =  Label(self.frame1,text="VALOR INVÁLIDO",bg='#fffef0')
        self.labelAvisoValor.place(relx="0.50", rely="0.40",relwidth="0.50", relheight="0.075")
      else:
        try:
          self.labelAvisoValor.destroy
        except:
          pass
          
         
  def botoes(self, home: Type[tk.Tk]):
    self.botaoVoltar = Button(self.frame2, text="VOLTAR", command=lambda:self.voltar(home))
    self.botaoVoltar.place(relx="0.2", rely="0.35",relwidth="0.25", relheight="0.30")

    self.botaoCriar = Button(self.frame2, text="CRIAR ITEM", command=lambda:self.criarItem())
    self.botaoCriar.place(relx="0.55", rely="0.35",relwidth="0.25", relheight="0.30")

    self.labelNome =  Label(self.frame1,text="Item: ",bg='#fffef0')
    self.labelNome.place(relx="0.1", rely="0.10",relwidth="0.10", relheight="0.075")
    self.getNome = Entry(self.frame1)
    self.getNome.place(relx="0.2", rely="0.10",relwidth="0.25", relheight="0.075")

    self.labelQuant =  Label(self.frame1,text="Quantidade: ", bg='#fffef0')
    self.labelQuant.place(relx="0.1", rely="0.20",relwidth="0.10", relheight="0.075")
    self.getQuant = Entry(self.frame1)
    self.getQuant.place(relx="0.2", rely="0.20",relwidth="0.25", relheight="0.075")

    self.labelCategoria =  Label(self.frame1,text="Categoria: ",bg='#fffef0')
    self.labelCategoria.place(relx="0.1", rely="0.30",relwidth="0.10", relheight="0.075")
    self.getCategoria = Entry(self.frame1)
    self.getCategoria.place(relx="0.2", rely="0.30",relwidth="0.25", relheight="0.075")

    self.labelValor =  Label(self.frame1,text="Valor: ",bg='#fffef0')
    self.labelValor.place(relx="0.1", rely="0.40",relwidth="0.10", relheight="0.075")
    self.getValor = Entry(self.frame1)
    self.getValor.place(relx="0.2", rely="0.40",relwidth="0.25", relheight="0.075")

  

  