import pandas as pd
import controle_estoque
import csv
 
 
df_new = pd.read_csv('Names.csv')
 
# saving xlsx file
GFG = pd.ExcelWriter('Names.xlsx')
df_new.to_excel(GFG, index=False)
 
GFG.save()

class PlanilhaExcel:
    @staticmethod
    def converte_csv_excel(self, planilha_csv = 'planilha.csv', planilha_excel = 'planilha.xlsx'):
        df_new = pd.read_csv(planilha_csv = 'planilha.csv')
        GFG = pd.ExcelWriter(planilha_excel = 'planilha.xlsx')
        df_new.to_excel(GFG, index = False)
        GFG.save()