# #Criando e conectando ao banco de dados
# import sqlite3

# #Criar a uma conexão com com banco de dados chamado de "escola.db"
# conexao = sqlite3.connect("escola.db")

# #Criamos um objeto "cursor" vai servir para executar os comandos SQL
# cursor = conexao.cursor()


# #Criando uma tabela no banco chamada de "alunos"
# cursor.execute("""
#  CREATE TABLE IF NOT EXISTS alunos (
#      id INTEGER PRIMARY KEY AUTOINCREMENT,
#      nome TEXT NOT NULL,
#      idade INTEGER,
#      curso TEXT    
#      )                
#  """)
# print("Tabela criada com sucesso!")



# # #Inserindo um valor no banco de dados (aluno)
# cursor.execute("""
#  INSERT INTO alunos (nome, idade, curso)
#  VALUES (?, ?, ?)                          
#  """,
#  ("Laura", 24, "Engenharia")
# )

# lista_alunos = [
#      ("Raul", 20, "Direito"),
#      ("Vinicius", 31, "Computação"),
#      ("Vitoria", 78, "Medicina"),
# ]

# #Executemany permite inserir múltiplas linhas
# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?, ?, ?)                          
# """,
# lista_alunos )


# #Confirmar as alterações do banco
# conexao.commit()
# print("Dados inseridos com sucesso!")


# #Atualizar os dados da tabela alunos
# #Atualizar o nome de um aluno
# #Sempre usar WHERE, senão todos os registros serão alterados!
# cursor.execute("""
#  UPDATE alunos
#  SET nome = ?, curso = ?
#  WHERE id = ?  
#  """, ("Felipe", "ADS", 2)
# )

# conexao.commit()

# print("Dados atualizados com sucesso!")


# #Consultar os dados
# #Selecionando todos os alunos
# cursor.execute("SELECT * FROM alunos")
#  #fetchall traz todas as linhas da consulta
# for linha in cursor.fetchall():
#      print(f"ID {linha[0]} | NOME {linha[1]} | IDADE {linha[2]} | CURSO {linha[3]}")

# curso = input("Qual curso você deseja ver os alunos: ")
#  #Selecionando apenas os alunos do curso Computação
# cursor.execute("SELECT nome, idade FROM alunos WHERE curso = ?", (curso,) )
# for linha in cursor.fetchall():
#      print(linha)


# def deletar_aluno(id_aluno):
#     try:
#         # Conectando ao banco de dados
#         conexao = sqlite3.connect("escola.db")
#         cursor = conexao.cursor()

#         # Deletando o aluno com o ID fornecido
#         cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
       
#         # Confirmando a alteração
#         conexao.commit()

#         # Verificando se algum aluno foi realmente deletado
#         if cursor.rowcount > 0:
#             print("Aluno removido com sucesso!")
#         else:
#             print("Nenhum aluno encontrado com o ID fornecido.")

#     except Exception as erro:
#         # Caso ocorra algum erro relacionado ao banco de dados
#         print(f"Erro ao tentar excluir aluno: {erro}")

#     finally:
#         # Sempre fechar a conexão, independentemente de sucesso ou erro
#         if conexao:
#             conexao.close()

# # Solicitando o ID do aluno para deletar
# deletar = input("Digite o id do aluno que deseja deletar: ")
# deletar_aluno(deletar)