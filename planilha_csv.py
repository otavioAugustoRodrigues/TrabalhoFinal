import csv
from controle_estoque import *
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from fornecedor import *

# Class responsável por imprimir o estado atual do estoque.
class PlanilhaCSV:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d/%m")
    
                
    # função responsável por imprimir o estado atual do terminal em um arquivo .csv.
    @classmethod
    def escreve_csv_colunas_diferentes(self, nomearquivo : csv, controle_estoque : Type[ControleEstoque]) -> None:
        with open(nomearquivo, 'w', newline='') as csvfile:
            fieldnames = ['ID','nome', 'quantidade', 'categoria', 'valor', 'Valor total em estoque', 'fornecedor', 'ID do fornecedor', 'pais fornecedor', 'termo pgto fornecedor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in controle_estoque.get_itens_cadastrados:
                if item.fornecedor is not None:
                    writer.writerow({'ID': item.get_id_item, 'nome': item.get_nome_item, 'quantidade': item.get_quantidade_item, 'categoria': item.get_categoria_item, 'valor': item.get_valor_item, 'Valor total em estoque' : item.get_valor_total_estoque(), 'fornecedor' : item.fornecedor.get_nome_fornecedor, 'ID do fornecedor' : item.fornecedor.get_id_fornecedor, 'pais fornecedor' : item.fornecedor.get_pais_fornecedor, 'termo pgto fornecedor' : item.fornecedor.get_termo_pagamento_fornecedor})


    # Método responsável por imprimir uma GUI com informações do controle de estoque no dia atual.
    @classmethod
    def escreve_tela_GUI(self, controle_estoque : Type[ControleEstoque]) -> None:
        root = tk.Tk()
        root.title(f"Controle de Estoque - {self.formatted_date}")

        table = ttk.Treeview(root)
        table['columns'] = ['ID','nome', 'quantidade', 'categoria', 'valor', 'Valor total em estoque', 'fornecedor', 'ID do fornecedor', 'pais fornecedor', 'termo pgto fornecedor']

        table.heading("ID", text="ID")
        table.heading("nome", text="Nome")
        table.heading("quantidade", text="Quantidade")
        table.heading("categoria", text="Categoria")
        table.heading("valor", text="Valor")
        table.heading("Valor total em estoque", text="Valor total em estoque")
        table.heading("fornecedor", text="Fornecedor")
        table.heading("ID do fornecedor", text="ID do fornecedor")
        table.heading("pais fornecedor", text="País do fornecedor")
        table.heading("termo pgto fornecedor", text="Fornecedor")

        for i, item in enumerate(controle_estoque.get_itens_cadastrados, start=1):
            if item.fornecedor is not None:
                table.insert("", "end", values=(item.get_id_item, item.get_nome_item, item.get_quantidade_item, item.get_categoria_item, item.get_valor_item, item.get_valor_total_estoque(), item.fornecedor.get_nome_fornecedor, item.fornecedor.get_id_fornecedor, item.fornecedor.get_pais_fornecedor, item.fornecedor.get_termo_pagamento_fornecedor))

        table.pack(expand=True, fill=tk.BOTH)

        root.mainloop()