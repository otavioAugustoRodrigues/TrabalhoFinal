from tkinter import *

janela = Tk()

class ListItens():
  def __init__(self):
   self.janela = janela
   self.listitens()
   self.frame()
   #self.botoes()
   janela.mainloop()

  def listitens(self):
   self.janela.title("LISTA DE ITENS")
   self.janela.configure(background = '#e1ede0')
   self.janela.geometry("700x500")
   self.janela.resizable(True,True)
   self.janela.maxsize(width=900,height=700)
   self.janela.minsize(width=500,height=400)

  def frame(self):
   self.frame = Frame(self.janela, bg='#e1ede0')
   self.frame.place(relx="0", rely="0", relwidth="1", relheight="1")

ListItens()