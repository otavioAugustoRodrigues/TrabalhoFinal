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
   self.botoesFrame1()
   self.botoesFrame2(home)
   self.janela.mainloop()

  def edita(self)-> None:
   self.janela.title("EDITAR ITEM")
   self.janela.configure(background = '#e1ede0')
   self.janela.geometry("700x500")
   self.janela.resizable(True,True)
   self.janela.maxsize(width=900,height=700)
   self.janela.minsize(width=500,height=400)

  def frame(self) -> None:
    self.frame1 = Frame(self.janela, bg='#fffef0')
    self.frame1.place(relx="0.025", rely="0.025", relwidth="0.95", relheight="0.7")

    self.frame2 = Frame(self.janela, bg='#e1ede0')
    self.frame2.place(relx="0", rely="0.75", relwidth="1", relheight="0.25")

  def is_int(self, numero):
    try:
      int(numero)
      return True
    except:
      return False

  def validarID(self) -> None:
    verificacao = self.getIdItem.get()
    if(self.is_int(verificacao) == True):
      id = int(self.getIdItem.get())
      a = 0
      for i in range(len(self.controle_estoque.itens_cadastrados)):
        if(self.controle_estoque.itens_cadastrados[i].item_id == id):
          a = 1
          b = i
          
      if(a != 0):
        try:
          self.labelItemNEnc.destroy()
        except:
          pass
        try:
          self.labelIdInvalido.destroy()
        except:
          pass

        textoId = f'VOCÊ ESTÁ EDITANDO O ITEM: {self.controle_estoque.itens_cadastrados[b].nome}'
        textoQuant = f'Alterar Quantidade - a quantidade atual é {self.controle_estoque.itens_cadastrados[b].quantidade}'
        
        self.labelMudarQuantidade.config(text=textoQuant)

        self.labelItemEnc = Label(self.frame1,text=textoId ,bg='#fffef0')
        self.labelItemEnc.place(relx="0.50", rely="0.25",relwidth="1", relheight="0.10", anchor="center")
      else:
        try:
          self.labelItemEnc.destroy()
        except:
          pass
        try:
          self.labelIdInvalido.destroy()
        except:
          pass
        self.labelItemNEnc = Label(self.frame1,text="ITEM NÃO ENCONTRADO" ,bg='#fffef0')
        self.labelItemNEnc.place(relx="0.50", rely="0.25",relwidth="1", relheight="0.10", anchor="center")
    else:
      try:
        self.labelItemEnc.destroy()
      except:
        pass
      try:
        self.labelItemNEnc.destroy()
      except:
        pass
      self.labelIdInvalido = Label(self.frame1,text="ID INVÁLIDO" ,bg='#fffef0')
      self.labelIdInvalido.place(relx="0.50", rely="0.25",relwidth="1", relheight="0.10", anchor="center")

  def botoesFrame1(self) -> None:
    self.labelIdItem =Label(self.frame1,text="ID do Item: ",bg='#fffef0')
    self.labelIdItem.place(relx="0.1", rely="0.10",relwidth="0.15", relheight="0.10")
    self.getIdItem = Entry(self.frame1)
    self.getIdItem.place(relx="0.25", rely="0.10",relwidth="0.10", relheight="0.10")
    self.botaoValidarId = Button(self.frame1, text="VALIDAR ID", command=lambda:self.validarID())
    self.botaoValidarId.place(relx="0.65", rely="0.10",relwidth="0.25", relheight="0.10")

    self.labelMudarCategoria =Label(self.frame1,text="Nova Categoria: ",bg='#fffef0')
    self.labelMudarCategoria.place(relx="0.1", rely="0.35",relwidth="0.15", relheight="0.10")
    self.getNovaCategoria = Entry(self.frame1)
    self.getNovaCategoria.place(relx="0.25", rely="0.35",relwidth="0.30", relheight="0.10")

    self.labelMudarQuantidade = Label(self.frame1,text="Alterar Quantidade",bg='#fffef0')
    self.labelMudarQuantidade.place(relx="0.5", rely="0.60",relwidth="1", relheight="0.10", anchor="center")
    self.getNovaQuantidade = Entry(self.frame1)
    self.getNovaQuantidade.place(relx="0.55", rely="0.75",relwidth="0.30", relheight="0.10")
    self.escolhaQuant = StringVar()
    self.radiousAum = Radiobutton(self.frame1, text="Aumentar", variable=self.escolhaQuant, value=1,bg='#fffef0')
    self.radiousAum.place(relx="0.15", rely="0.75",relwidth="0.15", relheight="0.05", anchor=tk.W)
    self.radiousDim = Radiobutton(self.frame1, text="Diminuir", variable=self.escolhaQuant, value=2,bg='#fffef0')
    self.radiousDim.place(relx="0.15", rely="0.80",relwidth="0.15", relheight="0.05", anchor=tk.W)

  def voltar(self, home: tk.Tk)-> None:
   self.janela.destroy()
   home.janela.deiconify()

  def botoesFrame2(self, home: Type[tk.Tk]) -> None:
    self.botaoVoltar = Button(self.frame2, text="VOLTAR", command=lambda:self.voltar(home))
    self.botaoVoltar.place(relx="0.2", rely="0.35",relwidth="0.25", relheight="0.30")

    self.botaoCriar = Button(self.frame2, text="SALVAR")
    self.botaoCriar.place(relx="0.55", rely="0.35",relwidth="0.25", relheight="0.30")

