from tkinter import *
from typing import Type
from item import Item
import tkinter as tk
from bancoDeDados import BancoDados

bd = BancoDados()

class EditarItem():
  def __init__(self, home: tk.Tk)-> None:
   self.controle_estoque = bd.le_controle()
   self.janela = Tk()
   self.edita()
   self.frame()
   self.botoes(home)
   self.janela.mainloop()

  def edita(self)-> None:
   self.janela.title("EDITAR ITEM")
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

  def botoes(self, home: Type[tk.Tk]):
    self.botaoVoltar = Button(self.frame2, text="VOLTAR", command=lambda:self.voltar(home))
    self.botaoVoltar.place(relx="0.2", rely="0.35",relwidth="0.25", relheight="0.30")

    self.botaoCriar = Button(self.frame2, text="SALVAR")
    self.botaoCriar.place(relx="0.55", rely="0.35",relwidth="0.25", relheight="0.30")   