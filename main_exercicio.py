import sqlite3


def conectar():

    return sqlite3.connect("biblioteca.db")

def criar_tabela():

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            disponivel TEXT CHECK(disponivel IN ('Sim', 'Não')) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def cadastrar_livro(titulo, autor, ano):

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, 'Sim')
    ''', (titulo, autor, ano))
    conn.commit()
    conn.close()


def listar_livros():

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conn.close()
    return livros

def exibir_livros():

    livros = listar_livros()
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado ainda.")
    for livro in livros:
        print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Disponível: {livro[4]}")
    print()


def atualizar_disponibilidade(id_livro):

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT disponivel FROM livros WHERE id = ?', (id_livro,))
    resultado = cursor.fetchone()
    if resultado:
        novo_status = 'Não' if resultado[0] == 'Sim' else 'Sim'
        cursor.execute('UPDATE livros SET disponivel = ? WHERE id = ?', (novo_status, id_livro))
        conn.commit()
        print(f"Status atualizado para '{novo_status}'!")
    else:
        print("Livro não encontrado.")
    conn.close()


def remover_livro(id_livro):

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))
    conn.commit()
    conn.close()
    print("Livro removido com sucesso!")


def menu():
    criar_tabela()  
    while True:
        print("""
===== MENU BIBLIOTECA =====
1. Cadastrar livro
2. Listar livros
3. Atualizar disponibilidade
4. Remover livro
5. Sair
""")
        escolha = input("Escolhe uma opção (1 a 5): ")

        if escolha == "1":
            print("\n--- Cadastro de Livro ---")
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano = input("Ano de publicação: ")
            cadastrar_livro(titulo, autor, ano)
            print("✅ Livro cadastrado com sucesso!\n")

        elif escolha == "2":
            exibir_livros()

        elif escolha == "3":
            print("\n--- Atualizar Disponibilidade ---")
            try:
                id_livro = int(input("Digite o ID do livro: "))
                atualizar_disponibilidade(id_livro)
            except ValueError:
                print("⚠️ Digita um número válido!")

        elif escolha == "4":
            print("\n--- Remover Livro ---")
            try:
                id_livro = int(input("Digite o ID do livro para remover: "))
                remover_livro(id_livro)
            except ValueError:
                print("⚠️ Digita um número válido!")

        elif escolha == "5":
            print("📚 Encerrando o sistema... Valeu e até a próxima!")
            break

        else:
            print("❌ Opção inválida. Tenta de novo!")

# Roda o menu se o arquivo for executado diretamente
if __name__ == "__main__":
    menu()
