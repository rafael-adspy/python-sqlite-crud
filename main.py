from db import *
from menu import *
from colorama import Fore, init, Style
init(autoreset=True)
criar()

while True:
    menu_1()
    while True:
        try:
            op = int(input(Fore.GREEN + Style.BRIGHT + f'    Selecione Uma Opção: '))
            break
        except ValueError:
            print(Fore.RED + Style.BRIGHT + f'ERRO, Digite Apenas Números!!!')

    if op == 1:
        produto = input('Produto: ')
        while True:
            try:
                quantidade = int(input('Quantidade: '))
                break
            except ValueError:
                print('Digite um número inteiro válido!')
        while True:
            try:
                preco = float(input('Preço: '))
                break
            except ValueError:
                print('Digite um preço válido!')
        categoria = input('Categoria: ')

        cadastrar(produto, quantidade, preco, categoria)
        print(Fore.GREEN + Style.BRIGHT + f'Itens cadastrados com sucesso!')

    elif op == 2:
        while True:
            produto = input(Style.BRIGHT + f'Informe o produto: ').strip()
            if not produto:
                print(Fore.RED + Style.BRIGHT + f'O produto não pode ficar vazio!!')
                continue
            if produto.isdigit():
                print(Fore.RED + Style.BRIGHT + f'Nome não pode ter apenas números!!!')
                continue
            break
        buscar(produto)

    elif op == 3:
        while True:
            produto_antigo = input("Produto a ser atualizado: ").strip()
            if not produto_antigo:
                print("Informe o produto que deseja atualizar!")
                continue
            break

        while True:
            produto = input('Informe o produto: ').strip()
            if not produto:
                print('Campo vazio!')
                continue
            break

        while True:
            try:
                quantidade = int(input('Informe a quantidade: '))
                if quantidade < 0:
                    print('Quantidade inválida!')
                    continue
                break
            except ValueError:
                print('Digite apenas números!')

        while True:
            try:
                preco = float(input('Informe o preço: '))
                if preco <= 0:
                    print('Preço inválido!')
                    continue
                break
            except ValueError:
                print('Digite apenas números!')

        while True:
            categoria = input('Informe a categoria: ').strip()
            if not categoria:
                print('Campo vazio!')
                continue
            break
        atualizar_produto(produto_antigo, produto, quantidade, preco, categoria)
        print(Fore.GREEN + Style.BRIGHT + f'Produtos atualizados com sucesso!')

    elif op == 4:
        while True:
            produto = input('Informe o produto: ').strip()
            if not produto:
                print('Campo vazio!')
                continue
            break
        excluir(produto)
        print(Fore.GREEN + Style.BRIGHT + f'Produto excluido com sucesso!')


    elif op == 5:
        listar_produtos()

    elif op == 6:
        print(Fore.RED + Style.BRIGHT + 'ENCERRANDO SISTEMA...')
        break

    else:
        print(Fore.RED + Style.BRIGHT + f'Opção Invalida!!!')








