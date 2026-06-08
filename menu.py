from colorama import init, Style, Fore

init(autoreset=True)

def menu_1():
    print(Fore.BLUE + Style.BRIGHT + '=' * 40)
    print(Fore.YELLOW + Style.BRIGHT + '       SISTEMA DE ESTOQUE')
    print(Fore.BLUE + Style.BRIGHT + '=' * 40)

    print(Fore.GREEN + '[1] Cadastrar Produto')
    print(Fore.GREEN + '[2] Buscar Produto')
    print(Fore.GREEN + '[3] Atualizar Produto')
    print(Fore.GREEN + '[4] Excluir Produto')
    print(Fore.GREEN + '[5] Listar Produtos')
    print(Fore.RED + '[6] Sair')

    print(Fore.BLUE + Style.BRIGHT + '=' * 40)

