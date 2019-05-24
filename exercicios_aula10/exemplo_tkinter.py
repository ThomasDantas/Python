import tkinter as tk
janela = tk.Tk()

janela.title("Olá, Mestre")

janela["bg"] = "green"
janela["background"] = "red"

# Posicionamenrto da tela
# L=Largura A=Altura E=Distancia da borda Esquerda da tela T=Distancia do Topo da Tela
# LXA+E+T

janela.geometry("800x500+100+100")

lb = tk.Label(janela, text="Curso de Informática IFSUL !!")
lb.place(x=300, y=100)

Bt = tk.Button(janela, width=20, text="Confirma")
Bt.place(x=300, y=300)

janela.mainloop()

