import mysql.connector
conexao = mysql.connector.connect( 
    host = 'localhost',
    user ='root',
    password = "Petita@123",
    database = 'bdyoutube', 
)

cursor = conexao.cursor()

nome_produto = "salgadinho"
valor = 2

#comando = f'INSERT INTO vendas (nome_produto, valor) VALUE ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit()

comando = f'SELECT * FROM vendas'

cursor.execute(comando)

resultado = cursor.fetchall() 
print(resultado)

cursor.close()
conexao.close()




#CREATE
""" cursor = conexao.cursor()

nome_produto = "toddynho"
valor = 3

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'


cursor.execute(comando)
conexao.commit() """

#READ
""" comando = f'SELECT * FROM vendas'
cursor.execute(comando)
#conexao.commit()  #edita o banco de dados
resultado = cursor.fetchall() #lendo o banco de dados 
print(resultado) """

#UPDATE
""" valor = 6
nome_produto = "toddynho"

cursor = conexao.cursor()
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close() """

#DELETE
""" cursor = conexao.cursor()

valor = 6
nome_produto = "toddynho"

comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close() """