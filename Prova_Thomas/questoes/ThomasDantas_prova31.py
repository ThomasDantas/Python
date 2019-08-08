from tkinter import *
import tkinter as tk
import sqlite3

janela = tk.Tk()
conexao = sqlite3.connect("biblioteca.db")
Cursor = conexao.cursor()
Cursor.execute('create table if not exists livros(titulo text, autor text, ano_edicao varchar, '
               'editora text, categoria text)')

v = tk.IntVar()


def cadastra():
    tit = titulo.get()
    aut = autor.get()
    a = ano.get()
    var = v.get()
    edit = editora.get()
    cat = ''

    if var == 1:
        cat = 'literatura'
    elif var == 2:
        cat = 'tecnico'
    elif var == 3:
        cat = 'periodico'
    elif var == 4:
        cat = 'didaticos'
    Cursor.execute('insert into livros(titulo, autor, ano_edicao, editora, '
                   'categoria) values(?, ?, ?, ?, ?)', (tit, aut, a, edit, cat))
    conexao.commit()


def consulta():
    Cursor.execute("select * from livros order by titulo")
    resultado = Cursor.fetchall()
    # listbox = Listbox(janela)
    for registro in resultado:
        #  listbox.insert(1, registro)
        print(registro)

    Cursor.execute("select * from livros order by categoria")
    resultado = Cursor.fetchall()
    for registro in resultado:
        print(registro)


janela.title("Cadastro de livros")
janela.geometry('500x400+200+200')

labelTitulo = Label(janela, text="titulo")
labelTitulo.place(x=70, y=100)
titulo = Entry(janela, width=20, fg="blue")
titulo.place(x=120, y=100)

labelAutor = Label(janela, text="autor")
labelAutor.place(x=70, y=130)
autor = Entry(janela, width=20, fg="blue")
autor.place(x=120, y=130)

labelAno = Label(janela, text="ano de edicao")
labelAno.place(x=70, y=160)
ano = Entry(janela, width=15, fg="blue")
ano.place(x=150, y=160)

labelEditora = Label(janela, text="editora")
labelEditora.place(x=70, y=190)
editora = Entry(janela, width=20, fg="blue")
editora.place(x=130, y=190)

tk.Radiobutton(janela, text="literatura", padx=70,  variable=v, value=1, bg="red").pack(anchor=tk.W)
tk.Radiobutton(janela, text="tecnico", padx=70, variable=v, value=2, bg="pink").pack(anchor=tk.W)
tk.Radiobutton(janela, text="periódico", padx=70, variable=v, value=3, bg="green").pack(anchor=tk.W)
tk.Radiobutton(janela, text="didaticos", padx=70, variable=v, value=4, bg="yellow").pack(anchor=tk.W)


bt = Button(janela, width=15, text="Gravar", command=cadastra)
bt.place(x=80, y=220)
lb2 = Label(janela, fg="red", font=("Verdana", 10))
lb2.place(x=100, y=270)

bt = Button(janela, width=15, text="Consultar", command=consulta)
bt.place(x=220, y=220)
lb2 = Label(janela, fg="red", font=("Verdana", 10))
lb2.place(x=100, y=270)


janela.mainloop()
Cursor.close()
conexao.close()
