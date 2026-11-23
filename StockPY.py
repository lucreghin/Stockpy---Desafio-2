"""
StockPy - Sistema de Gerenciamento de Estoque e Vendas
Desafio 2 - Lógica de Programação - Tema 3 (Etapa 1)

Requer Python 3.10+ (uso de match ... case).
Os dados ficam em memória: lista de dicionários (produtos) e um
dicionário com os acumuladores de vendas.
"""

LINHA = "=" * 36


# ----------------------------------------------------------------------
# Funções auxiliares (formatação e leitura/validação de dados)
# ----------------------------------------------------------------------
def formatar_moeda(valor):
    """Formata um número como moeda brasileira: R$ 1.234,50"""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def ler_texto_obrigatorio(mensagem):
    """Lê um texto e repete a pergunta enquanto estiver vazio."""
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Erro: este campo é obrigatório.")


def ler_inteiro(mensagem, minimo):
    """Lê um inteiro maior ou igual a 'minimo'."""
    while True:
        entrada = input(mensagem).strip()
        try:
            numero = int(entrada)
        except ValueError:
            print("Erro: informe um número inteiro válido.")
            continue
        if numero < minimo:
            print(f"Erro: o valor deve ser maior ou igual a {minimo}.")
        else:
            return numero


def ler_preco(mensagem):
    """Lê um número real maior que zero (aceita vírgula ou ponto)."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            preco = float(entrada)
        except ValueError:
            print("Erro: informe um valor numérico válido.")
            continue
        if preco <= 0:
            print("Erro: o preço deve ser maior que zero.")
        else:
            return preco


# ----------------------------------------------------------------------
# Funções principais
# ----------------------------------------------------------------------
def exibir_menu():
    """Apresenta o menu principal."""
    print()
    print("STOCKPY | MENU PRINCIPAL")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Registrar entrada no estoque")
    print("5 - Registrar venda")
    print("6 - Consultar produtos com estoque baixo")
    print("7 - Consultar resumo de vendas")
    print("0 - Encerrar aplicação")


def buscar_produto(produtos, codigo):
    """Retorna o produto com o código informado, ou None."""
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def verificar_estoque(quantidade, minimo):
    """Classifica a situação do estoque."""
    if quantidade == 0:
        return "Sem estoque"
    elif quantidade <= minimo:
        return "Estoque baixo"
    else:
        return "Estoque adequado"


def cadastrar_produto(produtos):
    """Cadastra um novo produto aplicando as regras de negócio."""
    print("\n--- CADASTRO DE PRODUTO ---")

    # Código único
    while True:
        codigo = ler_inteiro("Código do produto: ", 1)
        if buscar_produto(produtos, codigo) is None:
            break
        print("Erro: já existe um produto com este código.")

    nome = ler_texto_obrigatorio("Nome do produto: ")
    categoria = ler_texto_obrigatorio("Categoria: ")
    preco = ler_preco("Preço unitário de venda (R$): ")
    quantidade = ler_inteiro("Quantidade inicial em estoque: ", 0)
    minimo = ler_inteiro("Quantidade mínima desejada em estoque: ", 0)

    produtos.append({
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade,
        "minimo": minimo,
        "vendidas": 0,
    })
    print(f"Produto '{nome}' cadastrado com sucesso!")


def listar_produtos(produtos):
    """Exibe todos os produtos cadastrados."""
    print("\n--- LISTA DE PRODUTOS ---")
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    print(f"{'Cód.':<6}{'Nome':<22}{'Categoria':<16}{'Preço':>13}"
          f"{'Qtd':>6}{'Mín':>6}  Situação")
    print("-" * 85)
    for p in produtos:
        situacao = verificar_estoque(p["quantidade"], p["minimo"])
        print(f"{p['codigo']:<6}{p['nome'][:20]:<22}{p['categoria'][:14]:<16}"
              f"{formatar_moeda(p['preco']):>13}{p['quantidade']:>6}"
              f"{p['minimo']:>6}  {situacao}")


def consultar_produto(produtos):
    """Consulta individual de um produto pelo código."""
    codigo = ler_inteiro("Informe o código do produto: ", 1)
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    situacao = verificar_estoque(produto["quantidade"], produto["minimo"])
    print(LINHA)
    print("CONSULTA DE PRODUTO")
    print(LINHA)
    print(f"Código: {produto['codigo']}")
    print(f"Produto: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço unitário: {formatar_moeda(produto['preco'])}")
    print(f"Quantidade atual: {produto['quantidade']}")
    print(f"Estoque mínimo: {produto['minimo']}")
    print(f"Situação: {situacao.upper()}")
    print(f"Unidades vendidas: {produto['vendidas']}")
    print(LINHA)


def registrar_entrada(produtos):
    """Registra entrada de mercadorias no estoque."""
    print("\n--- ENTRADA NO ESTOQUE ---")
    codigo = ler_inteiro("Informe o código do produto: ", 1)
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    adicionada = ler_inteiro("Quantidade a adicionar: ", 1)
    anterior = produto["quantidade"]
    produto["quantidade"] += adicionada

    print(f"Produto: {produto['nome']}")
    print(f"Quantidade anterior: {anterior}")
    print(f"Quantidade adicionada: {adicionada}")
    print(f"Novo saldo disponível: {produto['quantidade']}")


def registrar_venda(produtos, vendas):
    """Processa a venda de um único produto e atualiza os acumuladores."""
    print("\n--- REGISTRO DE VENDA ---")
    codigo = ler_inteiro("Informe o código do produto: ", 1)
    produto = buscar_produto(produtos, codigo)

    if produto is None:
        print("Produto não encontrado.")
        return

    print(f"Produto: {produto['nome']} | Disponível: {produto['quantidade']}")
    if produto["quantidade"] == 0:
        print("Erro: produto sem estoque.")
        return

    quantidade = ler_inteiro("Quantidade a vender: ", 1)
    if quantidade > produto["quantidade"]:
        print(f"Erro: quantidade solicitada ({quantidade}) maior que o "
              f"estoque disponível ({produto['quantidade']}).")
        return

    valor_total = produto["preco"] * quantidade
    produto["quantidade"] -= quantidade
    produto["vendidas"] += quantidade
    vendas["faturamento"] += valor_total
    vendas["unidades"] += quantidade
    vendas["operacoes"] += 1

    print(LINHA)
    print("VENDA REALIZADA")
    print(LINHA)
    print(f"Produto: {produto['nome']}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço unitário: {formatar_moeda(produto['preco'])}")
    print(f"Valor total: {formatar_moeda(valor_total)}")
    print(f"Estoque restante: {produto['quantidade']}")
    print(LINHA)


def contar_alertas(produtos):
    """Conta produtos com quantidade atual <= mínimo."""
    total = 0
    for p in produtos:
        if p["quantidade"] <= p["minimo"]:
            total += 1
    return total


def listar_estoque_baixo(produtos):
    """Lista produtos em situação de alerta (inclui sem estoque)."""
    print("\n--- PRODUTOS COM ESTOQUE BAIXO ---")
    encontrou = False

    for p in produtos:
        if p["quantidade"] <= p["minimo"]:
            if not encontrou:
                print(f"{'Cód.':<6}{'Produto':<24}{'Atual':>7}{'Mínimo':>8}  Situação")
                print("-" * 60)
                encontrou = True
            situacao = verificar_estoque(p["quantidade"], p["minimo"])
            print(f"{p['codigo']:<6}{p['nome'][:22]:<24}{p['quantidade']:>7}"
                  f"{p['minimo']:>8}  {situacao}")

    if not encontrou:
        print("Não existem produtos em situação de alerta.")


def resumo_vendas(produtos, vendas):
    """Apresenta os indicadores comerciais."""
    print(LINHA)
    print("RESUMO GERAL DE VENDAS")
    print(LINHA)
    print(f"Total de produtos: {len(produtos)}")
    print(f"Total de vendas: {vendas['operacoes']}")
    print(f"Unidades vendidas: {vendas['unidades']}")
    print(f"Faturamento: {formatar_moeda(vendas['faturamento'])}")

    if vendas["operacoes"] == 0:
        print("Ticket médio: nenhuma venda realizada até o momento.")
    else:
        ticket = vendas["faturamento"] / vendas["operacoes"]
        print(f"Ticket médio: {formatar_moeda(ticket)}")

    print(f"Produtos em alerta: {contar_alertas(produtos)}")
    print(LINHA)


# ----------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------
def main():
    produtos = []
    vendas = {"faturamento": 0.0, "unidades": 0, "operacoes": 0}

    executando = True
    while executando:
        exibir_menu()
        opcao = input("Informe a opção desejada: ").strip()

        match opcao:
            case "1":
                cadastrar_produto(produtos)
            case "2":
                listar_produtos(produtos)
            case "3":
                consultar_produto(produtos)
            case "4":
                registrar_entrada(produtos)
            case "5":
                registrar_venda(produtos, vendas)
            case "6":
                listar_estoque_baixo(produtos)
            case "7":
                resumo_vendas(produtos, vendas)
            case "0":
                print("Encerrando o StockPy. Até logo!")
                executando = False
            case _:
                print("Opção inválida! Escolha uma das opções do menu.")


if __name__ == "__main__":
    main()