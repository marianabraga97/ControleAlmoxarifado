import json

try:
    with open('estoque.json', 'r') as arquivo_estoque:
        estoque = json.load(arquivo_estoque)
except FileNotFoundError:
    estoque = {}

def salvar_estoque():
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo)

def mostrar_menu():
    print('\n' + '=' * 40)
    print('SISTEMA DE ALMOXARIFADO')
    print('=' * 40)
    print('[ 1 ] CADASTRAR PRODUTO')
    print('[ 2 ] RETIRAR PRODUTO')
    print('[ 3 ] EXCLUIR PRODUTO')
    print('[ 4 ] VER ESTOQUE')
    print('[ 5 ] SAIR')
    print('=' * 40)

while True:
    mostrar_menu()
    opcao = input('Escolha a opção que deseja: ')

    if opcao == '1':
        nome = input('Qual nome do produto?: ')
        quantidade = int(input('Qual a quantidade do produto?: '))
        estoque[nome] = quantidade
        salvar_estoque()
        print(f'Produto {nome} cadastrado com sucesso!')

    elif opcao == '2':
        nome = input('Digite o nome do produto: ')
        quantidade = int(input('Quanto será retirado?: '))

        if nome in estoque:
            if estoque[nome] >= quantidade:
                estoque[nome] -= quantidade
                salvar_estoque()
                print(f'Produto {nome} retirado com sucesso!')
                print(f'Estoque atual: {estoque[nome]}')
            else:
                print('Quantidade insuficiente!')
        else:
            print('Produto não encontrado!')

    elif opcao == '3':
        nome = input('Digite o nome do produto: ')

        if nome in estoque:
            del estoque[nome]
            salvar_estoque()
            print(f'Produto {nome} excluído!')
        else:
            print('Produto não encontrado!')

    elif opcao == '4':
        print('\nESTOQUE:')
        for produto, quantidade in estoque.items():
            print(f'{produto} = {quantidade}')

    elif opcao == '5':
        break