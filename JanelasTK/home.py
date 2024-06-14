from tkinter import *

janela = Tk()

class Aplication():
  def __init__(self):
    self.janela = janela
    self.home()
    self.frame()
    self.botoes()
    janela.mainloop()
  def home(self):
    self.janela.title("HOME")
    self.janela.configure(background = '#e1ede0')
    self.janela.geometry("700x500")
    self.janela.resizable(True,True)
    self.janela.maxsize(width=900,height=700)
    self.janela.minsize(width=500,height=400)
  def frame(self):
    self.frame = Frame(self.janela, bg='#e1ede0')
    self.frame.place(relx="0", rely="0", relwidth="1", relheight="1")
  def botoes(self):

    self.titulo = Label(self.frame, text="GERENCIADOR DE ESTOQUE")
    self.titulo.place(relx="0.5", rely="0.05", anchor="center")

    self.botaoListItens = Button(self.frame, text="LISTA DE ITENS")
    self.botaoListItens.place(relx="0.375", rely="0.15", relwidth="0.25", relheight="0.1")

    self.botaoCriarItem = Button(self.frame, text="CRIAR ITEM")
    self.botaoCriarItem.place(relx="0.375", rely="0.30", relwidth="0.25", relheight="0.1")

    self.botaoListForn = Button(self.frame, text="LISTA DE FORNECEDORES")
    self.botaoListForn.place(relx="0.375", rely="0.45", relwidth="0.25", relheight="0.1")

    self.botaoVerifForn = Button(self.frame, text="VER FORNECEDOR")
    self.botaoVerifForn.place(relx="0.375", rely="0.60", relwidth="0.25", relheight="0.1")

    self.botaoCriarForn = Button(self.frame, text="CRIAR FORNECEDOR")
    self.botaoCriarForn.place(relx="0.375", rely="0.75", relwidth="0.25", relheight="0.1")


Aplication()