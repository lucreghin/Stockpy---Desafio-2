# StockPy – Sistema de Gerenciamento de Estoque e Vendas

Protótipo de aplicação de terminal em Python para controle de estoque, registro de vendas e geração de indicadores comerciais de uma loja de produtos de informática e acessórios tecnológicos.

> **Desafio 2 – Lógica de Programação – Tema 3 (Etapa 1)**
> Engenharia da Computação / Ciência da Computação – UNIVAP

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Como executar](#como-executar)
- [Menu principal](#menu-principal)
- [Regras de negócio](#regras-de-negócio)
- [Exemplos de saída](#exemplos-de-saída)
- [Estrutura do código](#estrutura-do-código)
- [Estrutura de dados](#estrutura-de-dados)
- [Conceitos de programação utilizados](#conceitos-de-programação-utilizados)
- [Limitações](#limitações)
- [Estrutura da entrega](#estrutura-da-entrega)

---

## Funcionalidades

- Cadastro de produtos com validação de todos os campos
- Listagem de produtos com a situação do estoque
- Consulta individual de produto por código
- Registro de entrada de mercadorias
- Registro de vendas com comprovante
- Relatório de produtos com estoque baixo ou sem estoque
- Resumo geral de vendas (faturamento, ticket médio e outros indicadores)

## Requisitos

- **Python 3.10 ou superior** (o programa usa `match ... case`)
- Nenhuma biblioteca externa é necessária

Para conferir a versão instalada:

```bash
python --version
```

## Como executar

```bash
python stockpy.py
```

Em alguns sistemas o comando pode ser `python3 stockpy.py`.

## Menu principal

```
STOCKPY | MENU PRINCIPAL
1 - Cadastrar produto
2 - Listar produtos
3 - Consultar produto
4 - Registrar entrada no estoque
5 - Registrar venda
6 - Consultar produtos com estoque baixo
7 - Consultar resumo de vendas
0 - Encerrar aplicação
Informe a opção desejada:
```

O menu é exibido novamente após cada operação. Uma opção inexistente gera uma mensagem de erro e o usuário retorna ao menu.

## Regras de negócio

### Cadastro de produto

| Campo | Regra |
|---|---|
| Código | Inteiro positivo e único |
| Nome | Obrigatório |
| Categoria | Obrigatória |
| Preço unitário | Maior que zero (aceita vírgula ou ponto) |
| Quantidade inicial | Inteiro maior ou igual a zero |
| Quantidade mínima | Inteiro maior ou igual a zero |

Ao cadastrar, o sistema guarda a quantidade atual e inicia o contador de unidades vendidas em zero.

### Situação do estoque

| Condição | Situação |
|---|---|
| Quantidade atual = 0 | Sem estoque |
| 0 < quantidade atual ≤ mínimo | Estoque baixo |
| Quantidade atual > mínimo | Estoque adequado |

### Entrada no estoque

- O produto deve existir.
- A quantidade deve ser um inteiro positivo.
- O sistema exibe a quantidade anterior, a quantidade adicionada e o novo saldo.

### Venda

- O produto deve existir.
- A quantidade deve ser um inteiro positivo e não pode ultrapassar o estoque disponível.
- Valor da venda = preço unitário × quantidade.
- Atualiza: estoque do produto, unidades vendidas do produto, faturamento acumulado, total de unidades vendidas e número de operações de venda.
- Cada venda envolve apenas um produto.

### Resumo de vendas

| Indicador | Descrição |
|---|---|
| Total de produtos | Quantidade de produtos cadastrados |
| Total de vendas | Quantidade de operações de venda realizadas |
| Unidades vendidas | Total de unidades comercializadas |
| Faturamento | Soma dos valores das vendas |
| Ticket médio | Faturamento ÷ número de vendas |
| Produtos em alerta | Produtos com quantidade atual ≤ mínimo |

Se nenhuma venda tiver sido realizada, o sistema informa isso em vez de calcular o ticket médio, evitando divisão por zero.

## Exemplos de saída

**Consulta de produto**

```
====================================
CONSULTA DE PRODUTO
====================================
Código: 1001
Produto: Mouse Gamer
Categoria: Periféricos
Preço unitário: R$ 89,90
Quantidade atual: 15
Estoque mínimo: 5
Situação: ESTOQUE ADEQUADO
Unidades vendidas: 10
====================================
```

**Comprovante de venda**

```
====================================
VENDA REALIZADA
====================================
Produto: Mouse Gamer
Quantidade: 3
Preço unitário: R$ 89,90
Valor total: R$ 269,70
Estoque restante: 12
====================================
```

## Estrutura do código

| Função | Responsabilidade |
|---|---|
| `exibir_menu()` | Apresenta o menu principal |
| `cadastrar_produto(produtos)` | Realiza o cadastro com validações |
| `listar_produtos(produtos)` | Exibe os produtos cadastrados |
| `buscar_produto(produtos, codigo)` | Localiza um produto pelo código (retorna `None` se não existir) |
| `consultar_produto(produtos)` | Apresenta as informações individuais |
| `registrar_entrada(produtos)` | Atualiza o estoque por recebimento |
| `registrar_venda(produtos, vendas)` | Processa uma venda |
| `verificar_estoque(quantidade, minimo)` | Classifica a situação do estoque |
| `listar_estoque_baixo(produtos)` | Exibe produtos em situação de alerta |
| `resumo_vendas(produtos, vendas)` | Apresenta os indicadores comerciais |

Funções auxiliares:

| Função | Responsabilidade |
|---|---|
| `formatar_moeda(valor)` | Formata valores como `R$ 1.234,50` |
| `ler_texto_obrigatorio(mensagem)` | Lê texto não vazio |
| `ler_inteiro(mensagem, minimo)` | Lê inteiro com valor mínimo, repetindo em caso de erro |
| `ler_preco(mensagem)` | Lê número real maior que zero |
| `contar_alertas(produtos)` | Conta produtos com estoque ≤ mínimo |
| `main()` | Laço principal do programa |

## Estrutura de dados

Os dados ficam apenas em memória (não há banco de dados nem arquivos).

Os produtos são armazenados em uma **lista de dicionários**:

```python
{
    "codigo": 1001,
    "nome": "Mouse Gamer",
    "categoria": "Periféricos",
    "preco": 89.90,
    "quantidade": 15,
    "minimo": 5,
    "vendidas": 10,
}
```

Os acumuladores de vendas ficam em um dicionário:

```python
vendas = {"faturamento": 0.0, "unidades": 0, "operacoes": 0}
```

## Conceitos de programação utilizados

- Variáveis simples e compostas (listas e dicionários)
- Entrada e saída de dados (`input` e `print`)
- Estruturas condicionais simples e compostas (`if`, `elif`, `else`)
- Múltipla escolha com `match ... case`
- Estruturas de repetição `for` e `while`
- Funções com parâmetros e valores de retorno
- Tratamento de exceções (`try/except`) na leitura de números

## Limitações

- Os dados são perdidos ao encerrar o programa, pois ficam apenas em memória.
- Cada venda aceita apenas um produto.
- Não há edição ou exclusão de produtos nesta etapa.
