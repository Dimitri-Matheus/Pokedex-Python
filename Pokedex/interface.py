# Modulos
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

# cores
Preto = "#444466"  # Preta
Branco = "#feffff"  # branca
Azul = "#6f9fbd"  # azul
Vermelho = "#ef5350"   # vermelha
Valor = "#38576b"  # valor
Letra = "#403d3d"   # letra


# Criando a janela
janela = ThemedTk(theme="Breeze")
janela.title('Pokedex')
janela.geometry('550x510')
janela.configure(bg=Branco)

ttk.Separator(janela, orient="horizontal").grid(row=0, columnspan=1, ipadx=272)

# Criando o frame
frame_pokemon = Frame(janela, width=550, height=230, relie='flat')
frame_pokemon.grid(row=1, column=0)

# Nome
poke_nome = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=Branco, fg=Preto)
poke_nome.place(x=12, y=15)

# Tipo
poke_tipo = Label(frame_pokemon, text='Elétrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=Branco, fg=Preto)
poke_tipo.place(x=12, y=50)

# ID
poke_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=Branco, fg=Preto)
poke_id.place(x=12, y=75)

janela.mainloop()