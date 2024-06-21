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
-----------------------------------------------------------------------------

( 1 ) Estoque.
( 2 ) Cadastro.
( 3 ) Cadeia de suprimentos.
( 4 ) Programador de produção.
( 5 ) Canal de Vendas.
( 0 ) Sair.

-----------------------------------------------------------------------------
''')        
    
    # Implementa uma função que irá implementar as funções para visualizar as
    # funções relacionadas ao estoque.
    def funcoes_sistema_estoque(self) -> None:
        print(
'''
-----------------------------------------------------------------------------

( 1 ) Visualizar estoque no dia de hoje.
( 2 ) Filtrar estoque por nome.
( 3 ) Filtrar estoque por categoria.
( 4 ) Filtrar estoque por nome de fornecedor.
( 5 ) Ordenar estoque por nome.
( 6 ) Ordenar estoque por categoria.
( 7 ) Ordenar estoque por nome de fornecedor.
( 0 ) Voltar.

-----------------------------------------------------------------------------
''')        

    # Implementa uma função que irá implementar as funções para visualizar as
    # funções relacionadas ao cadastro.
    def funcoes_cadastro(self) -> None:
        print(
'''
-----------------------------------------------------------------------------

( 1 ) Cadastra novo item.
( 2 ) Cadastra novo fornecedor.
( 3 ) Cadastra um fornecedor para um determinado item.
( 0 ) Voltar.

-----------------------------------------------------------------------------
''')        

    # Implementa uma função que irá implementar as funções para visualizar as
    # funções relacionadas ao cadastro.
    def funcoes_cadeia_suprimentos(self) -> None:
        print(
'''
-----------------------------------------------------------------------------

( 1 ) Compra um item.
( 0 ) Voltar.

-----------------------------------------------------------------------------
''')        
    
    # Implementa uma função que irá implementar as funções para visualizar as
    # funções relacionadas ao cadastro.
    def funcoes_programador_producao(self) -> None:
        print(
'''
-----------------------------------------------------------------------------

( 1 ) Configurar um item como ativo.
( 2 ) Configurar um item como obsoleto.
( 0 ) Voltar.

-----------------------------------------------------------------------------
''')        
            
    # Implementa uma função que irá implementar as funções para visualizar as
    # funções relacionadas ao cadastro.
    def funcoes_canal_vendas(self) -> None:
        print(
'''
-----------------------------------------------------------------------------

( 1 ) Vender um item.
( 0 ) Voltar.

-----------------------------------------------------------------------------
''')        
    # Implementa uma função que irá ditar o funcionamento do sistema.
    def sistema_controle_estoque(self):
        print("inicializando o sistema...")
        controle_estoque = ControleEstoque()
        controle_estoque.inicializa_controle_estoque("teste.csv")

        i = True
        while i:
            self.funcoes_sistema_inicial()
            input_usr = int(input("Informe uma opção."))
            
            match input_usr:
                case 0:
                    print("encerrando o sistema...\n\
                    salvando as alterações feitas...")
                    PlanilhaCSV.escreve_csv_colunas_diferentes("teste.csv", controle_estoque)
                    break

                case 1:
                    while i == True:
                        self.funcoes_sistema_estoque()
                        input_usr = int(input("Informe uma opção."))
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                i = 0
                                break
                            
                            case 1:
                                print("( 1 ) Visualizar estoque no dia de hoje.\n")
                                controle_estoque.padrao_imprime_estoque()
                                break

                            case 2:
                                print("( 2 ) Filtrar estoque por nome.\n")
                                input_parametro = input("Informe o nome para filtrar o estoque: ")
                                print()
                                FiltraEstoque.filtra_controle_estoque_nome(controle_estoque, input_parametro)
                                break

                            case 3:
                                print("( 3 ) Filtrar estoque por categoria.\n")
                                input_parametro = input("Informe a categoria para filtrar o estoque: ")
                                print()
                                FiltraEstoque.filtra_controle_estoque_categoria(controle_estoque, input_parametro)
                                break

                            case 4:
                                print("( 4 ) Filtrar estoque por nome de fornecedor.\n")
                                input_parametro = input("Informe o nome do fornecedor para filtrar o estoque: ")
                                print()
                                FiltraEstoque.filtra_controle_estoque_fornecedor(controle_estoque, input_parametro)
                                break

                            case 5:
                                print("( 5 ) Ordenar estoque por nome.\n")
                                OrdenaEstoque.ordena_estoque_nome(controle_estoque)
                                break

                            case 6:
                                print("( 6 ) Ordenar estoque por categoria.\n")
                                OrdenaEstoque.ordena_estoque_categoria(controle_estoque)
                                break

                            case 7:
                                print("( 7 ) Ordenar estoque por nome de fornecedor.\n")
                                OrdenaEstoque.ordena_estoque_fornecedor(controle_estoque)
                                break
                
                case 2:
                    while i == True:
                        self.funcoes_cadastro()
                        input_usr = int(input("Informe uma opção."))
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                i = 0
                                break
                            case 1:
                                print("( 1 ) Cadastra novo item.\n")
                                input_nome_item = input("Informe o nome do item")
                                input_categoria_item = input("Informe a categoria do item")
                                novo_item = Item(input_nome_item, input_categoria_item)
                                controle_estoque.cadastra_item(novo_item)
                                break

                            case 2:
                                print("( 2 ) Cadastra novo fornecedor.\n")
                                input_nome_fornecedor = input("Informe o nome do fornecedor: ")
                                input_pais_fornecedor = input("Informe o país do fornecedor: ")
                                input_termo_pgto_fornecedor = input("Informe o termo de pagamento do fornecedor: ")
                                novo_fornecedor = Fornecedor(input_nome_fornecedor, input_pais_fornecedor, input_termo_pgto_fornecedor)
                                controle_estoque.cadastra_fornecedor(novo_fornecedor)
                                break
                            
                            case 3:
                                print("( 3 ) Cadastra um fornecedor para um determinado item.\n")
                                input_nome_item = input("Informe o nome do item")
                                input_categoria_item = input("Informe a categoria do item")
                                novo_item = Item(input_nome_item, input_categoria_item)

                                input_nome_item = input("Informe o nome do fornecedor: ")
                                input_pais_fornecedor = input("Informe o país do fornecedor: ")
                                input_termo_pgto_fornecedor = input("Informe o termo de pagamento do fornecedor: ")
                                novo_fornecedor = Fornecedor(input_nome_fornecedor, input_pais_fornecedor, input_termo_pgto_fornecedor)

                                controle_estoque.cadastra_item_fornecedor(novo_item, novo_fornecedor)
                                break


                case 3: 
                    while i == True:
                        self.funcoes_cadeia_suprimentos()
                        input_usr = int(input("Informe uma opção."))
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                i = 0
                                break
                            case 1:
                                print("( 1 ) Compra um item.\n")
                                input_nome_item = input("Informe o nome do item: ")
                                input_fornecedor_item = input("Informe o nome do fornecedor do item: ")
                                input_quantidade_compra = input("Informe a qtd. comprada: ")
                                comprador = Comprador()
                                comprador.opera_material(controle_estoque, input_quantidade_compra, input_nome_item, input_fornecedor_item)
                                break

                case 4: 
                    while i == True:
                        self.funcoes_programador_producao()
                        input_usr = int(input("Informe uma opção."))
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                i = 0
                                break

                            case 1:
                                print("( 1 ) Configurar um item como ativo.\n")
                                input_usr = input("Informe o nome do item que gostaria de transformar em ativo: ")
                                pcp = ProgramadorProducao()
                                pcp.transforma_item_ativo(controle_estoque, input_usr)
                                break
                            case 2:
                                print("( 2 ) Configurar um item como obsoleto.\n")
                                input_usr = input("Informe o nome do item que gostaria de transformar em obsoleto: ")
                                pcp = ProgramadorProducao()
                                pcp.transforma_item_ativo(controle_estoque, input_usr)
                                break

                case 5: 
                    while i == True:
                        self.funcoes_canal_vendas()
                        input_usr = int(input("Informe uma opção."))
                        match input_usr:
                            case 0:
                                print("Voltando...")
                                i = 0
                                break
                            case 1:
                                print("( 1 ) Vender um item.\n")
                                input_nome_item = input("Informe o nome do item: ")
                                input_fornecedor_item = input("Informe o nome do fornecedor do item: ")
                                input_quantidade_venda = input("Informe a qtd. vendida: ")
                                vendedor = Vendedor()
                                vendedor.opera_material(controle_estoque, input_quantidade_venda, input_nome_item, input_fornecedor_item)
                                break