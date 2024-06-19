from controle_estoque import *
from filtra_estoque import *
from fornecedor import *
from planilha_csv import *
from item import *
from ordena_estoque import *
from comprador import *
from vendedor import *
from programador_producao import *

# Classe responsável por inicializar o sistema e orientar o usuário 
# ao seu funcionamento.
class Sistema:
    # Implementa uma função que irá implementar as funções do sistema inicial.
    def funcoes_sistema_inicial(self) -> None:
        print(
'''
( 1 ) Visualizar estoque.
( 2 ) Visualizar cadastro de itens/fornecedores.
( 3 ) Comprar/vender um item.
( 0 ) Encerrar o sistema.
''')        
    
    # Implementa uma função que irá implementar as funções para visualizar as
    # funções relacionadas ao estoque.
    def funcoes_sistema_visualizar_estoque(self) -> None:
        print(
'''
( 1 ) Imprimir relatório com todos os itens do estoque.
( 2 ) Imprimir relatório por item específico.
( 0 ) Voltar.
''')        

    # Implementa uma função que irá implementar as funções para visualizar as
    # funções relacionadas ao cadastro.
    def funcoes_sistema_visualizar_cadastro(self) -> None:
        print(
'''
( 1 ) Imprimir relatório com todos os itens/fornecedores cadastrados.
( 2 ) Adicionar um novo item/fornecedor cadastrado.
( 3 ) Tornar um item/fornecedor como 'não ativo'.
( 0 ) Voltar.
''')        
    
    # Implementa uma função que irá ditar o funcionamento do sistema.
    def sistema_controle_estoque(self):
        print("inicializando o sistema...")
        controle_estoque = ControleEstoque()
        gerenciador_planilha = PlanilhaCSV()
        self.funcoes_sistema_inicial()
        input_usr = int(input())

        while True:
            match input_usr:
                case 0:
                    print("encerrando o sistema...\n\
                    salvando as alterações feitas...")
                    # implementar aqui uma função para salvar o sistema
                    break

                case 1:
                    while True:
                        input_usr = int(input())
                        self.funcoes_sistema_visualizar_estoque()
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                break
                            case 1:
                                break
                            case 2:
                                break
                            case 3:
                                break
                
                case 2:
                    while True:
                        input_usr = int(input())
                        self.funcoes_sistema_visualizar_estoque()
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                break
                            case 1:
                                break
                            case 2:
                                break

                case 3: 
                    while True:
                        input_usr = int(input())
                        self.funcoes_sistema_visualizar_cadastro()
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                break
                            case 1:
                                break
                            case 2:
                                break
                            case 3:
                                break