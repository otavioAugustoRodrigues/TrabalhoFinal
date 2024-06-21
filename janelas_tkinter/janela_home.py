from tkinter import *
from controle_estoque import *
from planilha_csv import *
from typing import Type
import tkinter as tk

from datetime import datetime

from janelas_tkinter.janela_itens import *

current_date = datetime.now()
formatted_date = current_date.strftime("%d/%m")

class Home():
  def __init__(self)-> None:
    self.janela = Tk()
    self.home()
    self.frame()
    self.botoes()
    self.janela.mainloop()

  def home(self) -> None:
    self.janela.title(f"SISTEMA DE GERENCIAMENTO DE ESTOQUE - {formatted_date}")
    self.janela.configure(background = '#e1ede0')
    self.janela.geometry("700x500")
    self.janela.resizable(True,True)
    self.janela.maxsize(width=900,height=700)
    self.janela.minsize(width=500,height=400)

  def frame(self)-> None:
    self.frame = Frame(self.janela, bg='#e1ede0')
    self.frame.place(relx="0", rely="0", relwidth="1", relheight="1")

  def botao_estoque(self)->None:
    self.janela.withdraw()
    Estoque(self)
  
  def botao_lista_fornecedores(self)-> None:
    self.janela.withdraw()
    #CriarItem(self)

  def botao_lista_itens(self)-> None:
    self.janela.withdraw()
    #EditarItem(self)

  def botao_cadeira_suprimentos(self)-> None:
    self.janela.withdraw()

  def botao_programador_producao(self) -> None:
    self.janela.withdraw()
  
  def botao_canal_vendas(self) -> None:
    self.janela.withdraw()

  def botao_sair(self) -> None:
    self.janela.withdraw()
    self.janela.destroy()

  def botoes(self)-> None:

    coluna_esquerda_eixo_x = "0.05"
    coluna_direita_eixo_x = "0.55"

    largura_botao_padrao = "0.4"
    altura_botao_padrao = "0.1"

    botao_1_eixo_y = "0.25"
    botao_2_eixo_y = "0.40"
    botao_3_eixo_y = "0.55"

    botao_centralizado_eixo_x = "0.5"
    botao_titulo_eixo_y = "0.05"

    botao_sair_eixo_x = "0.375"
    botao_sair_eixo_y = "0.80"
    botao_sair_largura = "0.25"
    botao_sair_altura = "0.1"


    self.titulo = Label(self.frame, text="GERENCIADOR DE ESTOQUE")
    self.titulo.place(relx = botao_centralizado_eixo_x, rely = botao_titulo_eixo_y, anchor="center")

    self.botaoListItens = Button(self.frame, text="ESTOQUE", command=lambda:self.botao_estoque())
    self.botaoListItens.place(relx = coluna_esquerda_eixo_x, rely = botao_1_eixo_y, relwidth = largura_botao_padrao, relheight = altura_botao_padrao)

    self.botaoCriarItem = Button(self.frame, text="LISTA DE FORNECEDORES", command=lambda:self.botao_lista_fornecedores())
    self.botaoCriarItem.place(relx = coluna_esquerda_eixo_x, rely = botao_2_eixo_y, relwidth = largura_botao_padrao, relheight = altura_botao_padrao)

    self.botaoEditarItem = Button(self.frame, text="LISTA DE ITENS", command=lambda:self.botao_lista_itens())
    self.botaoEditarItem.place(relx = coluna_esquerda_eixo_x, rely= botao_3_eixo_y, relwidth = largura_botao_padrao, relheight = altura_botao_padrao)

    self.botaoListForn = Button(self.frame, text="CADEIA DE SUPRIMENTOS", command=lambda:self.botao_cadeira_suprimentos())
    self.botaoListForn.place(relx = coluna_direita_eixo_x, rely = botao_1_eixo_y, relwidth = largura_botao_padrao, relheight = altura_botao_padrao)

    self.botaoVerifForn = Button(self.frame, text="PROGRAMADOR DE PRODUÇÃO", command=lambda:self.botao_programador_producao())
    self.botaoVerifForn.place(relx = coluna_direita_eixo_x, rely = botao_2_eixo_y, relwidth = largura_botao_padrao, relheight = altura_botao_padrao)

    self.botaoCriarForn = Button(self.frame, text="CANAL DE VENDAS", command=lambda:self.botao_canal_vendas())
    self.botaoCriarForn.place(relx = coluna_direita_eixo_x, rely = botao_3_eixo_y, relwidth = largura_botao_padrao, relheight = altura_botao_padrao)

    self.botaoSair = Button(self.frame, text="SAIR",bg="#ec5353" ,command=lambda:self.botao_sair())
    self.botaoSair.place(relx = botao_sair_eixo_x, rely  = botao_sair_eixo_y, relwidth = botao_sair_largura, relheight = botao_sair_altura)
