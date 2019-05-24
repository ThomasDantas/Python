import tkinter as tk


def bt_click():
    # num1 = int(ed1.get())
    # num2 = int(ed2.get())
    # lb2["text"] = num1 + num2

    if str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric():
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb2["text"] = num1 + num2
    else:
        lb2["text"] = "Valor informado não é numerico"


janela = tk.Tk()

janela.title("Olá, Mestre")

janela["bg"] = "green"
janela["background"] = "pink"

janela.geometry('800x600+200+200')

ed1 = tk.Entry(janela, width=20, fg="blue")
ed1.place(x=300, y=100)

ed2 = tk.Entry(janela, width=20, fg="blue")
ed2.place(x=300, y=200)

bt = tk.Button(janela, width=20, text="Calcula", command=bt_click)
bt.place(x=285, y=300)

lb2 = tk.Label(janela, width=30, fg="red", font=("Verdana", 14))
lb2.place(x=200, y=400)

janela.mainloop()
