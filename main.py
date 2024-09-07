import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuarios (
    ID_Usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Endereco TEXT NOT NULL,
    Telefone TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Livros (
    ID_Livro INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,
    Ano_Publicacao INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Emprestimos (
    ID_Emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Usuario INTEGER NOT NULL,
    ID_Livro INTEGER NOT NULL,
    Data_Emprestimo TEXT NOT NULL,
    Data_Devolucao TEXT,
    FOREIGN KEY(ID_Usuario) REFERENCES Usuarios(ID_Usuario),
    FOREIGN KEY(ID_Livro) REFERENCES Livros(ID_Livro)
)
''')


