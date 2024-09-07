import tkinter as tk
from tkinter import messagebox

def cadastrar_usuario():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    telefone = entry_telefone.get()

    query = "INSERT INTO Usuarios (Nome, Endereco, Telefone) VALUES (?, ?, ?)"
    valores = (nome, endereco, telefone)
    cursor.execute(query, valores)
    conexao.commit()

    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")

def cadastrar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()

    query = "INSERT INTO Livros (Titulo, Autor, Ano_Publicacao) VALUES (?, ?, ?)"
    valores = (titulo, autor, ano)
    cursor.execute(query, valores)
    conexao.commit()

    messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")

def registrar_emprestimo():
    usuario_id = entry_id_usuario.get()
    livro_id = entry_id_livro.get()
    data_emprestimo = entry_data_emprestimo.get()
    data_devolucao = entry_data_devolucao.get()

    query = "INSERT INTO Emprestimos (ID_Usuario, ID_Livro, Data_Emprestimo, Data_Devolucao) VALUES (?, ?, ?, ?)"
    valores = (usuario_id, livro_id, data_emprestimo, data_devolucao)
    cursor.execute(query, valores)
    conexao.commit()

    messagebox.showinfo("Sucesso", "Empréstimo registrado com sucesso!")

root = tk.Tk()
root.title("Sistema de Biblioteca")

label_nome = tk.Label(root, text="Nome do Usuário")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_endereco = tk.Label(root, text="Endereço")
label_endereco.pack()
entry_endereco = tk.Entry(root)
entry_endereco.pack()

label_telefone = tk.Label(root, text="Telefone")
label_telefone.pack()
entry_telefone = tk.Entry(root)
entry_telefone.pack()

btn_cadastrar_usuario = tk.Button(root, text="Cadastrar Usuário", command=cadastrar_usuario)
btn_cadastrar_usuario.pack()

# Seção Cadastro de Livros
label_titulo = tk.Label(root, text="Título do Livro")
label_titulo.pack()
entry_titulo = tk.Entry(root)
entry_titulo.pack()

label_autor = tk.Label(root, text="Autor")
label_autor.pack()
entry_autor = tk.Entry(root)
entry_autor.pack()

label_ano = tk.Label(root, text="Ano de Publicação")
label_ano.pack()
entry_ano = tk.Entry(root)
entry_ano.pack()

btn_cadastrar_livro = tk.Button(root, text="Cadastrar Livro", command=cadastrar_livro)
btn_cadastrar_livro.pack()

label_id_usuario = tk.Label(root, text="ID do Usuário")
label_id_usuario.pack()
entry_id_usuario = tk.Entry(root)
entry_id_usuario.pack()

label_id_livro = tk.Label(root, text="ID do Livro")
label_id_livro.pack()
entry_id_livro = tk.Entry(root)
entry_id_livro.pack()

label_data_emprestimo = tk.Label(root, text="Data de Empréstimo (YYYY-MM-DD)")
label_data_emprestimo.pack()
entry_data_emprestimo = tk.Entry(root)
entry_data_emprestimo.pack()

label_data_devolucao = tk.Label(root, text="Data de Devolução (YYYY-MM-DD)")
label_data_devolucao.pack()
entry_data_devolucao = tk.Entry(root)
entry_data_devolucao.pack()

btn_registrar_emprestimo = tk.Button(root, text="Registrar Empréstimo", command=registrar_emprestimo)
btn_registrar_emprestimo.pack()

root.mainloop()

cursor.close()
conexao.close()