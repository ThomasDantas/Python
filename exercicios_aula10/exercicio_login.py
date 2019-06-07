import tkinter as tk

# def bt_click():

janela = tk.Tk()

janela.title("Login")

janela["background"] = "orange"


lb = tk.Label(janela, text="Login", fg="blue", font="Helvetica 20 bold italic")
lb.place(x=280, y=100)

janela.geometry('700x500+200+200')


lb = tk.Label(janela, text="User:")
lb.place(x=150, y=200)
ed1 = tk.Entry(janela, width=50, fg="blue")
ed1.place(x=200, y=200)

lb = tk.Label(janela, text="Password:")
lb.place(x=130, y=250)
ed2 = tk.Entry(janela, width=50, fg="blue")
ed2.place(x=200, y=250)

bt = tk.Button(janela, width=10, text="Logar")
bt.place(x=300, y=300)

janela.mainloop()
