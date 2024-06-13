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
    
    # método responsável por adicionar itens em nosso controle de estoque diretamente de uma planilha.
    def adiciona_itens_fornecedor_planilha_csv(self, nomearquivo : str, controle_estoque : ControleEstoque) -> None:
        with open(nomearquivo, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                print(f"Processing row: {row}")  # Debugging: Print each row

                item = Item(row['nome'], row['quantidade'], row['categoria'], float(row['valor']))
                item.nome_fornecedor_item = row['fornecedor']
                controle_estoque.cadastra_item(item)
                
    # função responsável por imprimir o estado atual do terminal em um arquivo .csv.
    def escreve_csv_colunas_diferentes(self, nomearquivo : csv, controle_estoque : Type[ControleEstoque]) -> None:
        with open(nomearquivo, 'w', newline='') as csvfile:
            fieldnames = ['nome', 'quantidade', 'categoria', 'valor', 'fornecedor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in controle_estoque.itens_cadastrados:
                writer.writerow({'nome': i.nome_item, 'quantidade': i.quantidade_item, 'categoria': i.categoria_item, 'valor': i.valor_item, 'fornecedor' : i.nome_fornecedor_item})

    # Método responsável por imprimir uma GUI com informações do controle de estoque no dia atual.
    def escreve_tela_GUI(self, controle_estoque : Type[ControleEstoque]) -> None:
        root = tk.Tk()
        root.title(f"Controle de Estoque - {self.formatted_date}")

        table = ttk.Treeview(root)
        table['columns'] = ['nome', 'qtd.', 'categoria', 'valor']

        table.heading("#0", text="Object")
        table.heading("nome", text="Nome")
        table.heading("qtd.", text="Qtd.")
        table.heading("categoria", text="Categoria")
        table.heading("valor", text="Valor")

        for i, obj in enumerate(controle_estoque.itens_cadastrados, start=1):
            table.insert("", "end", text=f"{obj.item_id}", values=(obj.nome_item, obj.quantidade_item, obj.categoria_item, obj.valor_item))

        table.pack(expand=True, fill=tk.BOTH)

        root.mainloop()