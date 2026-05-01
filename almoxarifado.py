import json

try:
    with open('estoque.json', 'r') as arquivo_estoque:
        estoque = json.load(arquivo_estoque)
except FileNotFoundError:
    estoque = {}

try:
    with open('movimentacoes.json', 'r') as arquivo_movimentacoes:
        movimentacoes = json.load(arquivo_movimentacoes)
except FileNotFoundError:
    movimentacoes = []

def salvar_estoque():
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo)

def salvar_movimentacoes():
    with open('movimentacoes.json', 'w') as arquivo:
        json.dump(movimentacoes, arquivo)

def mostrar_menu():
    print('\n' + '=' * 40)
    print('SISTEMA DE ALMOXARIFADO')
    print('=' * 40)
    print('[ 1 ] CADASTRAR PRODUTO')
    print('[ 2 ] RETIRAR PRODUTO')
    print('[ 3 ] EXCLUIR PRODUTO')
    print('[ 4 ] VER ESTOQUE')
    print('[ 5 ] HISTORICO DE MOVIMENTAÇÕES')
    print('[ 6 ] SAIR')
    print('=' * 40)

movimentacoes = []

def ler_numero(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Digite um numero válido!')

def cadastrar_produto():
    nome_produto = input('Digite o nome do produto para cadastrar: ').lower().strip()
    quantidade_produto = ler_numero('Digite a quantidade do produto: ')
    movimentacoes.append({"tipo": "entrada", "produto": nome_produto, "quantidade": quantidade_produto})
    salvar_movimentacoes()

    if nome_produto in estoque:
        estoque[nome_produto] += quantidade_produto
    else:
        estoque[nome_produto] = quantidade_produto

    salvar_estoque()
    print(f'Produto {nome_produto} cadastrado com sucesso!')

def retirar_produto():
    nome_produto = input('Digite o nome do produto que deseja retirar: ').lower().strip()
    quantidade_ret = ler_numero('Digite a quantidade do produto que irá retirar: ')
    movimentacoes.append({'tipo': 'retirada', 'produto': nome_produto, 'quantidade': quantidade_ret})
    salvar_movimentacoes()

    if quantidade_ret <= 0:
        print('Quantidade inválida!')
        return

    if nome_produto in estoque:
        if estoque[nome_produto] >= quantidade_ret:
            estoque[nome_produto] -= quantidade_ret
            salvar_estoque()
            print(f'Produto {nome_produto} retirado com sucesso!')
        else:
            print('Quantidade insuficiente no estoque!')
    else:
        print('Produto não encontrado!')

def excluir_produto():
    nome = input('Digite o nome do produto para excluir: ').lower().strip()

    if nome in estoque:
        del estoque[nome]
        salvar_estoque()
        print('Produto excluído com sucesso!')
    else:
        print('Produto inexistente!')

def ver_estoque():
    print('\n ESTOQUE: ')
    for produto, quantidade in estoque.items():
        print(f'Produto: {produto} | Quantidade: {quantidade}')

def hist_movimentacoes():
    if len(movimentacoes) == 0:
        print('Não há movimentações registradas!')
    else:
        for item in movimentacoes:
            tipo = item['tipo']
            produto = item['produto']
            quantidade = item['quantidade']
            print(f'{tipo} | {produto} | {quantidade}')

while True:
    mostrar_menu()
    opcao = input('Escolha a opção que deseja: ')

    if opcao == '1':
        cadastrar_produto()

    elif opcao == '2':
        retirar_produto()

    elif opcao == '3':
        excluir_produto()

    elif opcao == '4':
        ver_estoque()

    elif opcao == '5':
        hist_movimentacoes()

    elif opcao == '6':
        break