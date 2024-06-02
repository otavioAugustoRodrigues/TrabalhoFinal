import csv
from controleEstoque import *
from datetime import datetime
import tkinter as tk
from tkinter import ttk

# Class responsável por imprimir o estado atual do estoque.
class GerenciadorPlanilha:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d/%m")
    
    # método responsável por imprimir o estado atual no terminal.
    def le_csv(self, nomearquivo : csv) -> None:
        with open(nomearquivo, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            #spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            print(f"{'Nome':<15}\t{'Qtd.':<5}\t{'Categoria':<25}\t{'Valor':<10}")
            for row in reader:
                print(f"{row['nome']:15}\t{row['quantidade']:5}\t{row['categoria']:25}\t{row['valor']}")
                
    # função responsável por imprimir o estado atual do terminal em um arquivo .csv.
    def escreve_csv_colunas_diferentes(self, nomearquivo : csv, controle_estoque : Type[ControleEstoque]) -> None:
        with open(nomearquivo, 'w', newline='') as csvfile:
            fieldnames = ['nome', 'quantidade', 'categoria', 'valor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for element in controle_estoque.itens_cadastrados:
                writer.writerow({'nome': element.nome, 'quantidade': element.quantidade, 'categoria': element.categoria, 'valor': element.valor})

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
            table.insert("", "end", text=f"{obj.item_id}", values=(obj.nome, obj.quantidade, obj.categoria, obj.valor))

        table.pack(expand=True, fill=tk.BOTH)

        root.mainloop()