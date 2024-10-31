import mysql.connector as sql
from biblioteca import User, Livro

conexao = sql.connect (
    host = '10.28.2.61',
    user='suporte',
    password='suporte',
    database='biblioteca'
)
 
cursor = conexao.cursor()

cursor.execute('insert into livro(titulo, autor, genero, status, codigo) values ("O pequeno principe", "Jorjana", "Fantasia", "Disponivel", 123)')
conexao.commit()