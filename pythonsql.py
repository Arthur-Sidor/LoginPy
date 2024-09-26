import pyodbc

# Dados da conexão com o banco de dados
dados_conexao = (
    "Driver={SQL Server};"
    "Server=MTZNOTFS059377;"
    "Database=Fintech;"
    "Trusted_Connection=yes;"
)

# Estabelecendo a conexão com o banco de dados
conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

# Obtendo o cursor para executar comandos SQL
cursor = conexao.cursor()

# Capturando informações do usuário
print("Digite suas informações:")
username = input("Nome de usuário: ")
password = input("Senha: ")
email = input("Email: ")

# Inserindo os dados do usuário na tabela
comando = """
INSERT INTO Users (username, password, email)
VALUES (?, ?, ?)
"""

# Executando o comando com os parâmetros fornecidos pelo usuário
cursor.execute(comando, (username, password, email))

# Confirmando as alterações no banco de dados
conexao.commit()

# Fechando o cursor e a conexão
cursor.close()
conexao.close()

print("Informações inseridas com sucesso!")
