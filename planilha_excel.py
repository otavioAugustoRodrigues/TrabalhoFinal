import pandas as pd


class PlanilhaExcel:
    @classmethod
    def converte_csv_excel(self, planilha_csv, planilha_excel):
        df = pd.read_csv(planilha_csv)
        df.to_excel(planilha_excel, index = False)