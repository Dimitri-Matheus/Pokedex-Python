# Modulos
from tkinter import ttk
from ttkthemes import ThemedTK

# cores
Preto = "#444466"  # Preta
Branco = "#feffff"  # branca
Azul = "#6f9fbd"  # azul
Vermelho = "#ef5350"   # vermelha
Valor = "#38576b"  # valor
Letra = "#403d3d"   # letra


# Criando a janela
janela = ThemedTK(theme="arc")
janela.title('Pokedex')
janela.geometry('550x510')
janela.configure(bg=Branco)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

# Estilo

janela.mainloop()