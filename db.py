import sqlite3

from colorama import Style, Fore

con= sqlite3.connect("cadastro.db")
cor= con.cursor()

def criar():
    cor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (id INTEGER
    PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
    )
    ''')
    con.commit()


def cadastrar(produto, quantidade, preco, categoria):
    cor.execute('''
    INSERT INTO produtos (produto, quantidade, preco, categoria)
     VALUES (?, ?, ?, ?)''', (produto, quantidade, preco, categoria))
    con.commit()


def buscar(produto):
    cor.execute('''
    SELECT * FROM produtos
    WHERE produto = ?
    ''', (produto,))

    resultado = cor.fetchone()

    if resultado:
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + f'''
ID: {resultado[0]}
Produto: {resultado[1]}
Quantidade: {resultado[2]}
Preco: {resultado[3]:.2f}
Categoria: {resultado[4]}
''')
    else:
        print(Fore.RED + Style.BRIGHT + f'Produto não encontrado!!!')


def atualizar_produto(produto_antigo, produto, quantidade, preco, categoria):
    cor.execute('''
    UPDATE produtos
    SET produto = ?,
        quantidade = ?,
        preco = ?,
        categoria = ?
    WHERE produto = ?
    ''', (produto, quantidade, preco, categoria, produto_antigo))
    con.commit()
    print(f'Linhas alteradas: {cor.rowcount}')


def listar_produtos():
    cor.execute('SELECT * FROM produtos')
    resultados = cor.fetchall()

    if resultados:
        print('\n' + '=' * 40)
        print('      PRODUTOS CADASTRADOS')
        print('=' * 40)

        for item in resultados:
            print(f'''
ID: {item[0]}
Produto: {item[1]}
Quantidade: {item[2]}
Preço: R$ {item[3]:.2f}
Categoria: {item[4]}
''')
    else:
        print('Nenhum produto cadastrado!')
    con.commit()


def excluir(produto):
    cor.execute('''
    DELETE FROM produtos
    WHERE produto = ?''', (produto,))
    con.commit()
