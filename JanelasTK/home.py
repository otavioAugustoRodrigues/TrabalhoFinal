from tkinter import *
from JanelasTK.ListItens import ListItens
from JanelasTK.criarItem import CriarItem
from controle_estoque import ControleEstoque 
from typing import Type
import tkinter as tk


class Home():
  def __init__(self)-> None:
    self.janela = Tk()
    self.home()
    self.frame()
    self.botoes()
    self.janela.mainloop()

  def home(self) -> None:
    self.janela.title("HOME")
    self.janela.configure(background = '#e1ede0')
    self.janela.geometry("700x500")
    self.janela.resizable(True,True)
    self.janela.maxsize(width=900,height=700)
    self.janela.minsize(width=500,height=400)

  def frame(self)-> None:
    self.frame = Frame(self.janela, bg='#e1ede0')
    self.frame.place(relx="0", rely="0", relwidth="1", relheight="1")

  def abrirListI(self)->None:
    self.janela.withdraw()
    ListItens(self)
  
  def abrirCriarI(self)-> None:
    self.janela.withdraw()
    CriarItem(self)

  def botoes(self)-> None:

    self.titulo = Label(self.frame, text="GERENCIADOR DE ESTOQUE")
    self.titulo.place(relx="0.5", rely="0.05", anchor="center")

    self.botaoListItens = Button(self.frame, text="LISTA DE ITENS", command=lambda:self.abrirListI())
    self.botaoListItens.place(relx="0.375", rely="0.15", relwidth="0.25", relheight="0.1")

    self.botaoCriarItem = Button(self.frame, text="CRIAR ITEM", command=lambda:self.abrirCriarI())
    self.botaoCriarItem.place(relx="0.375", rely="0.275", relwidth="0.25", relheight="0.1")

    self.botaoListForn = Button(self.frame, text="LISTA DE FORNECEDORES")
    self.botaoListForn.place(relx="0.375", rely="0.40", relwidth="0.25", relheight="0.1")

    self.botaoVerifForn = Button(self.frame, text="VER FORNECEDOR")
    self.botaoVerifForn.place(relx="0.375", rely="0.525", relwidth="0.25", relheight="0.1")

    self.botaoCriarForn = Button(self.frame, text="CRIAR FORNECEDOR")
    self.botaoCriarForn.place(relx="0.375", rely="0.65", relwidth="0.25", relheight="0.1")

    self.botaoSair = Button(self.frame, text="SAIR", command=self.janela.destroy)
    self.botaoSair.place(relx="0.375", rely="0.775", relwidth="0.25", relheight="0.1")

