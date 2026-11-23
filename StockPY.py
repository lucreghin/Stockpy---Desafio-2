def menu():
    print("STOCKPY - MENU PRINCIPAL")
    print("1 - Cadastrar produto \n2 - Listar produtos")
    print("3 - Consultar produto \n4 - Registrar entrada no estoque \n5 - Registrar venda \n6 - Consultar produtos com estoque baixo \n7 - Consultar resumo de vendas \n0 - Encerrar aplicação")
    while True:
      escolha = int(input("escolha uma opção "))
      if escolha >7:
              print("insira um número correspondente as opções.")
      elif escolha < 0:
              print("insira um número correspondente as opções.")
      else:
              return escolha
produtos = {}
def cadastrar_produto():
     codigo_produto = int(input("Digite o código do produto: "))
     produtos[i].codigo = codigo_produto
    
while True:
    i=0
    escolha = menu()
        
    if escolha == 1:
        print("deu certo")
        cadastrar_produto()
        i += 1
    elif escolha == 2:
        listar_produto()
    elif escolha == 3:
        consultar_produto()
    elif escolha == 4:
         registrar_entrada()
    elif escolha ==5:
         registrar_vendas()
    elif escolha == 6:
         consultar_estoque_baixo()
    elif escolha == 7:
         consltar_resumo_vendas()
    elif escolha == 0:
         print("Encerrando aplicação")
         break